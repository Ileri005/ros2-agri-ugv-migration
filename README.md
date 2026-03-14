# ROS 2 Agricultural UGV Migration: Foundational Telemetry

## Project Context
This repository tracks the architectural migration of my agricultural robotics research from static, microcontroller-based firmware into the ROS 2 ecosystem. 

My previous research (such as the CocciCare poultry monitor) relied on standalone embedded systems. However, the unstructured, chaotic nature of Nigerian agricultural environments (uneven terrain, dense canopies, extreme lighting) requires the asynchronous, distributed computing capabilities of ROS 2 for robust autonomy.

## Current Implementation (Phase 1)
Currently, this repository houses the foundational software bridge for sensor telemetry. 
* Custom ROS 2 publishers and subscriber nodes written in Python (`rclpy`).
* Designed to handle basic data streaming from edge-compute hardware (Raspberry Pi/microcontrollers) as the precursor to full sensor fusion.

## Development Roadmap
This project is under active development. My definitive roadmap includes:
1. **LiDAR Integration:** Transitioning away from camera-based perception (which fails under equatorial sun/Harmattan dust) to 2D/3D LiDAR point clouds.
2. **Nav2 & SLAM:** Implementing the ROS 2 Navigation Stack to manage costmaps for non-geometric, off-road farm terrains.
