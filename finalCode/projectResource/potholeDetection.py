from ultralytics import YOLO

# Load YOLOv8 model (pre-trained weights, or you can start from scratch)
model = YOLO('yolov8n.pt')  # or yolov8s.pt for a small model

# Train the model
results = model.train(
    data='pothole_dataset.yaml',  # Path to your data config file
    epochs=50,                    # Number of epochs
    batch=16,                     # Batch size
    imgsz=640,                    # Image size
    name='pothole_detection'       # Name of the model training run
)

# Save the trained model weights
model.save('pothole_detection_model.pt')
