# Multi-Level Car Parking SLAM 🚗💨
**User-Participatory Visual-Inertial Mapping for Complex Environments**

This project proposes a user-participatory visual SLAM system designed to create accurate, up-to-date 3D maps of multi-level car parking garages. By crowdsourcing camera and IMU data from smartphones (e.g., iPhone 16) and vehicle-mounted sensors, we aim to solve the localization challenge in GPS-denied, multi-story structures.

---

## 🛠 Project Overview
* **Core Engine**: ORB-SLAM3 (Monocular-Inertial)
* **Target Hardware**: iPhone 16, NVIDIA RTX 4050, Jetson Orin 8GB
* **Primary Objective**: Thesis research for Purdue University - Master's in AI/ML

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have the following dependencies installed in your Docker environment:
* **Pangolin**: For 3D visualization
* **OpenCV**: For image processing and frame extraction
* **Eigen3 & g2o**: For backend optimization

### 2. Dataset Setup
We currently use the **EuRoC MAV** dataset for benchmarking and custom data from **Sensor Logger (iOS)**.

* **Tested Dataset**: V1_01_easy (Vicon Room 1)
* **Download**: [ETH Zurich Research Collection](https://www.research-collection.ethz.ch/entities/researchdata/bcaf173e-5dac-484b-bc37-faf97a594f1f)
* **Structure**: Place the `V1_01_easy` folder inside your `/datasets/` directory.

### 3. Execution Command
To run the Monocular-Inertial pipeline on the benchmark dataset:

```bash
cd ORB_SLAM3
./Examples/Monocular-Inertial/mono_inertial_euroc \
    ./Vocabulary/ORBvoc.txt \
    ./Examples/Monocular-Inertial/EuRoC.yaml \
    /workspace/datasets/V1_01_easy \
    /workspace/datasets/V1_01_easy/mav0/cam0/data.csv \
    /workspace/datasets/V1_01_easy/mav0/imu0/data.csv ; sync
```
### 📂 Dataset Directory Structure
ORB-SLAM3 expects the following hierarchy for Monocular-Inertial sequences:

```text
V1_01_easy/
└── mav0/                         # MAV sensor root
    ├── cam0/                     # Left Camera
    │   ├── data/                 # Raw .png image frames
    │   ├── sensor.yaml           # Camera intrinsics & distortion
    │   └── data.csv              # [timestamp_ns, filename]
    └── imu0/                     # IMU Sensor
        ├── sensor.yaml           # Noise & Bias parameters
        └── data.csv              # [timestamp_ns, w, a]
```

### Custom Sensor Integration (iPhone 16)
This project includes specialized configuration for mobile sensors to handle the transition from controlled datasets to real-world parking garages.

* Resolution: TBD (refer yaml)

* IMU TBD (refer yaml)

* Calibration: Custom iPhone16.yaml with scaled intrinsics and calibrated IMU noise parameters.
### 📊 Results & Visualization
The system generates the following outputs for analysis:

Camera Trajectory: Saved as forced_trajectory.txt for ATE (Absolute Trajectory Error) evaluation.

Keyframe Map: 3D point cloud reconstruction of the parking environment visible in the Pangolin viewer.

### 🎓 Academic Credit
This work is part of a Master's Thesis at Purdue University.

Authors: Shrirang Bhadgaonkar and Trevor Neri.

Original Framework: ORB-SLAM3 by UZ-SLAMLab.