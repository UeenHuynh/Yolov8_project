# Yolov8_project
# labelImg
Cách sử dụng Yolvo8 
B1: Tạo môi trường ảo python -m venv yolov8-env

B2: Activate yolov8-env\Scripts\activate

B3: Tải cái này xuống nè https://github.com/ultralytics/ultralytics

B4: Giải nén và sao chép thư mục vừa giải nén vào thư mục có chứa thư viện yolov8-env

B5: Tải thư viện xuống pip install ultralytics

pip install pafy

pip install youtube_dl==2020.12.2

B6: Tải dataset

Tạo data bằng file python rồi run ra file data.yaml
 
B7: Train model 

from ultralytics import YOLO

# Load a model

model = YOLO("yolov8n.yaml")  # build a new model from scratch

model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model

model.train(data="data.yaml", epochs=3)  # train the model

metrics = model.val()  # evaluate model performance on the validation set

results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image

success = model.export(format="onnx")  # export the model to ONNX format

Fix bug:

results = model("D:/AI project/datasets/coco128/images/train2017/000000000009.jpg")

results = model("D:\\AI project\\datasets\\coco128\\images\\train2017\\000000000009.jpg") 

B8: Predict model 

Chạy ở terminal hoặc cmd

yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'

yolo predict model=yolov8n.pt source='https://www.youtube.com/watch?v=sF0YQp9nBjA'

yolo predict model=yolov8n.pt = ‘https://www.youtube.com/watch?v=aQj5qTFhdZ0’


yolo predict model="D:\AI project\runs\detect\train\weights\best.pt" source="D:\AI project\human_detection_dataset\train\images\frame72007.20.00-07.25.00.jpg"
					Source ảnh video

yolo predict model="D:\AI project\runs\detect\train5\weights\best.pt" source = ‘https://www.youtube.com/watch?v=aQj5qTFhdZ0’

chạy theo từng step này nha

cd labelImg

pip install lxml pyqt5

pyrcc5 -o libs/resources.py resources.qrc

python labelImg.py
