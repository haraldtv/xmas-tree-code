from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n-seg.pt')  # Segment modellen. Mulig vi måbruke denne

# Train the model
results = model.train(data='/home/harald/git/xmas-tree-decorator/Code/Model/ELVE3610 - Christmas Baubles.v1i.yolov8/data.yaml', epochs=100, imgsz=640)
