from ultralytics import YOLO

# 加载模型
model = YOLO("yolov8n.pt")

# 训练模型
model.train(
    data="data.yaml",
    epochs=200,
    imgsz=640
)