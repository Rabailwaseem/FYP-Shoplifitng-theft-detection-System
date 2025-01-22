import argparse
import os
import cv2
import numpy as np
import tensorflow as tf
import winsound  # Import winsound for beep sound (Windows only)

# Define constants
dim = 256
IMAGE_HEIGHT = dim
IMAGE_WIDTH = dim
SEQUENCE_LENGTH = 60
CLASSES_LIST = ["Normal", "Shoplifting"]

def frame_extraction(video_path):
    frame_list = []
    video_capture = cv2.VideoCapture(video_path)
    video_frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    skip_frame_window = max(int(video_frame_count / SEQUENCE_LENGTH), 1)

    for frame_counter in range(SEQUENCE_LENGTH):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frame_window)
        success, frame = video_capture.read()

        if not success:
            break

        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        normalized_frame = resized_frame / 255.0
        frame_list.append(normalized_frame)

    video_capture.release()
    return frame_list
    
def predict(video_path, model):
    video_capture = cv2.VideoCapture(video_path)
    frames_buffer = []  # To hold frames for the sequence

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Process the frame
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        normalized_frame = resized_frame / 255.0

        # Add the processed frame to the buffer
        frames_buffer.append(normalized_frame)

        # If we have enough frames, make a prediction
        if len(frames_buffer) == SEQUENCE_LENGTH:
            input_data = np.asarray(frames_buffer)  # Convert buffer to numpy array
            input_data = np.expand_dims(input_data, axis=0)  # Add batch dimension

            # Make prediction
            prediction = model.predict(input_data)
            predicted_class = np.argmax(prediction, axis=1)[0]  # Get the class with the highest score
            
            # Annotate the frame with the prediction
            label = CLASSES_LIST[predicted_class]
            cv2.putText(frame, f'Predicted: {label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Produce a beep sound if "Shoplifting" is detected
            if label == "Shoplifting":
                frequency = 1000  # Set frequency to 1000 Hz
                duration = 500    # Set duration to 500 ms
                winsound.Beep(frequency, duration)  # Produce the beep sound

            # Remove the first frame from the buffer to keep the sequence moving
            frames_buffer.pop(0)

        # Display the frame
        cv2.imshow('Video', frame)

        # Exit if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description='Test ConvLSTM model on a video file.')
    parser.add_argument('video_path', type=str, help='Path to the input video file')
    args = parser.parse_args()

    # Load the trained model
    model = tf.keras.models.load_model('60_model_bs_256ok.h5')  # Update with your model path

    # Make prediction on the provided video
    predict(args.video_path, model)

if __name__ == "__main__":
    main()
