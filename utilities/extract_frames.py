import cv2
import os

# --- CONFIGURATION ---
video_path = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36\Camera\1773697176325.25.mp4"
output_folder = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36\my_ios_data3\mav0\cam0\data"

# Ensure output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()

frame_count = 0
print(f"Starting extraction from {video_path}...")

while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # End of video

    frame_count += 1
    # Save frame as %06d.png to match standard SLAM naming conventions
    file_name = os.path.join(output_folder, f"{frame_count:06d}.png")
    
    # Using quality 2 (standard) - cv2.IMWRITE_PNG_COMPRESSION is 0-9
    cv2.imwrite(file_name, frame, [cv2.IMWRITE_PNG_COMPRESSION, 2])

    if frame_count % 100 == 0:
        print(f"Extracted {frame_count} frames...")

cap.release()
print(f"Done! Extracted total of {frame_count} frames to {output_folder}")