from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.yaml")  # build a new model from scratch
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="D:\AI project\human_detection_dataset\data.yaml", epochs=5)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("D:/AI/cutest-dog-breeds-jpg.jpg")
success = model.export(format="onnx")  # export the model to ONNX format