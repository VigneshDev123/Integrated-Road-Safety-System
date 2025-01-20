# Integrated Road Safety System for Real-Time Waterlogging Detection and Traffic Management using Google maps API 
## Overview
This project focuses on detecting potholes and waterlogging on roads using camera-based sensors and machine learning techniques. The system processes real-time road images to identify potholes, estimate their depth, and assess waterlogging severity. It then integrates with Google Maps API to reroute traffic dynamically, ensuring safer and more efficient navigation. Additionally, the project includes an electric current leakage detection mechanism to warn users about potential hazards from submerged live wires.
This solution aims to enhance road safety, minimize vehicle damage, and prevent accidents caused by poor road conditions. 🚦📍

## Features
- **Real-time detection** of potholes and waterlogging.
- **Depth estimation** to assess the severity.
- **Traffic rerouting** based on detected obstacles.
- **Electric current leakage detection** in waterlogged areas.
- **Web/Mobile interface** for visualization and reporting.

## Technologies Used
- Python
- OpenCV
- TensorFlow/PyTorch (for AI models)
- YOLO (for object detection)
- Google Maps API (for navigation and rerouting)
- Django/Flask (for backend)
- Raspberry Pi (for IoT implementation)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VigneshDev123/Integrated-Road-Safety-System
   ```
2. Navigate to the project directory:
   ```bash
   cd Integrated-Road-Safety-System
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables if needed:
   ```bash
   export API_KEY=your_api_key
   ```
5. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Run the script to capture and process images for pothole detection.
- The system will analyze the images and provide severity levels.
- If integrated with Google Maps API, it will suggest alternate routes.
- View results in the web/mobile dashboard.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

