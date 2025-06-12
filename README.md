## 📝 System Overview

The **Shoplifting Theft Detection System** is an intelligent surveillance solution that utilizes computer vision and AI to monitor retail store environments. It is designed to detect suspicious behavior that may indicate potential shoplifting activity and raise alerts in real time. The system can analyze live camera feeds or pre-recorded video footage.

### 🎯 Objectives

- Automatically detect and track individuals in a retail setting.
- Identify suspicious actions such as hiding items, loitering, or leaving with unpaid goods.
- Provide real-time alerts or logs for store personnel to review.
- Improve loss prevention by minimizing human monitoring errors.

### 🔍 How It Works

1. **Input Feed**  
   - Accepts video input from live CCTV cameras or video files.

2. **Object & Person Detection**  
   - Uses deep learning models (e.g., YOLO, SSD, or custom CNNs) to detect humans and relevant store items.

3. **Behavior Analysis**  
   - Monitors patterns like:
     - hiding items in pocket
     - hiding items in abaya,shawl


4. **Suspicion Scoring (Optional)**  
   - Assigns a suspicion level to individuals based on actions and time spent.
   - High scores trigger alerts.

5. **Logging & Alerts**  
   - Logs suspicious events with timestamps.
   - Sends console alerts, notifications, or stores events in a local/remote database.

6. **Dashboard/Output (Optional)**  
   - Shows detection results, video highlights, and logs in a user-friendly UI.

### 📸 Example Workflow

```text
Video Feed → Object Detection → Behavior Tracking → Suspicion Score → Log/Alert

