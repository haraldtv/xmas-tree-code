from ultralytics import YOLO
import pandas as pd

# Load a model
model = YOLO('yolov8n-seg.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image

f = open("results.txt", "w")
f.write("")
f.close()

f = open("results.txt", "a")

print(results[0])

for r in results:
    #print(r.probs)
    print(type(r.masks))
    #f.write(str(r.probs))
    #print(r.masks)
    f.write(str(r.masks))

f.close()