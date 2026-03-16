import os

# --- CONFIGURATION ---
# Use 'r' for raw strings to handle Windows backslashes
csv_path = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36\my_ios_data3\mav0\cam0\data.csv"
image_dir = r"C:\Study\Purdue\SensorLoggerData\2026-03-16_21-39-36\my_ios_data3\mav0\cam0\data"

def rename_images():
    # 1. Read timestamps from data.csv
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return

    with open(csv_path, 'r') as f:
        # This handles both 'timestamp,filename' and 'timestamp' only formats
        timestamps = [line.strip().split(',')[0] for line in f if line.strip()]

    # 2. Get sorted list of current sequential files (000001.png, 000002.png...)
    current_files = sorted([f for f in os.listdir(image_dir) if f.endswith('.png')])

    # 3. Safety Check: Verify counts match
    if len(timestamps) != len(current_files):
        print(f"Warning: Count mismatch!")
        print(f"Timestamps in CSV: {len(timestamps)}")
        print(f"Images in Folder:  {len(current_files)}")
        # We proceed anyway, but only up to the shortest list length
    
    count = min(len(timestamps), len(current_files))
    print(f"Starting rename of {count} files...")

    # 4. Perform Renaming
    for i in range(count):
        old_name = current_files[i]
        new_name = f"{timestamps[i]}.png"
        
        old_path = os.path.join(image_dir, old_name)
        new_path = os.path.join(image_dir, new_name)
        
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            print(f"Failed to rename {old_name}: {e}")

    print("Done! Your dataset now matches the EuRoC V1_01_easy format.")

if __name__ == "__main__":
    rename_images()