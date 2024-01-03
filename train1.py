from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.yaml")  # build a new model from scratch
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco128.yaml", epochs=20)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://www.youtube.com/watch?v=sF0YQp9nBjA")  # predict on an image
success = model.export(format="onnx")  # export the model to ONNX format