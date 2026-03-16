import pandas as pd
import numpy as np
import os

# --- CONFIGURATION ---
DATA_DIR = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36"  # Where your CSVs are
OUTPUT_DIR = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36\my_ios_data3\mav0"
VIDEO_START_TIME_NS = 1773697176404582000  # From your filename
FPS = 30.0

# Create directory structure
os.makedirs(f"{OUTPUT_DIR}/cam0/data", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/imu0", exist_ok=True)

print("Starting Synchronization...")

# --- 1. PROCESS IMU DATA ---
print("Merging Accel and Gyro...")
accel = pd.read_csv(os.path.join(DATA_DIR, 'Accelerometer.csv'))
gyro = pd.read_csv(os.path.join(DATA_DIR, 'Gyroscope.csv'))

# Standardize to nanoseconds and sort
accel = accel.sort_values('time')
gyro = gyro.sort_values('time')

# Merge and Interpolate so every Gyro timestamp has a corresponding Accel value
# This is critical for the IMU pre-integration in ORB-SLAM3
imu_combined = pd.merge_asof(
    gyro, accel, on='time', 
    suffixes=('_g', '_a'), 
    direction='nearest'
)

# Format for ORB-SLAM3: timestamp(ns), wx, wy, wz, ax, ay, az
# Sensor Logger uses 'x', 'y', 'z' for both. Merged suffixes are _g and _a.
imu_final = imu_combined[['time', 'x_g', 'y_g', 'z_g', 'x_a', 'y_a', 'z_a']]

# Save as data.csv (no header, as required by the Euroc format)
imu_final.to_csv(f"{OUTPUT_DIR}/imu0/data.csv", index=False, header=False)
print(f"IMU data synchronized: {len(imu_final)} samples.")

# --- 2. PROCESS CAMERA TIMESTAMPS ---
print("Generating Camera timestamps...")
# List frames extracted by FFmpeg (assumes names like 000001.png)
image_folder = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36\my_ios_data3\mav0\cam0\data"
images = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])

if not images:
    print("ERROR: No images found in /mav0/cam0/data. Run FFmpeg first!")
else:
    frame_interval_ns = int(1e9 / FPS)
    cam_data = []
    
    for i, img_name in enumerate(images):
        timestamp = VIDEO_START_TIME_NS + (i * frame_interval_ns)
        cam_data.append([timestamp, img_name])
    
    # Save camera data.csv
    pd.DataFrame(cam_data).to_csv(f"{OUTPUT_DIR}/cam0/data.csv", index=False, header=False)
    print(f"Camera data mapped: {len(images)} frames.")

print("\nSUCCESS: Data is ready for ORB-SLAM3 in the /mav0 folder.")