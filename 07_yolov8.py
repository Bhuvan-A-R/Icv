# pip install ultralytics
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # weights download on first run
results = model('image.jpg')
results[0].show()
