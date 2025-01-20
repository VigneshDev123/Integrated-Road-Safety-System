import cv2
import numpy as np
from ultralytics import YOLO
from tensorflow.keras.models import load_model

# Load the trained YOLOv8 model for pothole detection
pothole_model = YOLO('pothole_detection_model.pt')

# Load the depth estimation model (the .h5 file)
depth_model = load_model('depth_estimation_model.h5')

def estimate_depth(image):
    # Preprocess the image as required by your depth model
    # Assume the depth model takes 128x128 input and outputs a depth map
    input_image = cv2.resize(image, (128, 128))
    input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension

    # Predict the depth map
    depth_map = depth_model.predict(input_image)
    depth_map = np.squeeze(depth_map, axis=0)  # Remove batch dimension

    return depth_map

def detect_and_estimate_depth(image):
    # Run YOLOv8 detection
    results = pothole_model(image)
    detections = results[0].boxes.xyxy  # Detected bounding boxes

    for det in detections:
        x1, y1, x2, y2 = map(int, det[:4])  # Coordinates of the detected object

        # Crop the pothole region from the image
        pothole_region = image[y1:y2, x1:x2]

        # Estimate depth for the pothole region
        depth_map = estimate_depth(pothole_region)

        # Visualize the detection and depth estimation
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        depth_value = np.mean(depth_map)  # Example: Taking the average depth
        cv2.putText(image, f'Depth: {depth_value:.2f}m', (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    return image

# Load a test image
image = cv2.imread('test_image.jpg')

# Detect potholes and estimate depth
output_image = detect_and_estimate_depth(image)

# Show the result
cv2.imshow('Pothole Detection and Depth Estimation', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
