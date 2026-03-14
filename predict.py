# from ultralytics import YOLO
#
# # 1 加载训练好的模型
# model = YOLO("runs/detect/train/weights/best.pt")
#
# # 2 进行图片检测
# results = model.predict(
#     source="test",   # test文件夹放测试图片
#     save=True,       # 保存检测结果
#     conf=0.25        # 置信度阈值
# )
#
# print("检测完成！结果保存在 runs/detect/predict 文件夹")
from ultralytics import YOLO

# 加载训练好的模型
model = YOLO("runs/detect/train/weights/best.pt")

# 预测图片
results = model.predict(
    source="test",
    save=True
)

# 统计检测数量
for r in results:
    boxes = r.boxes
    count = len(boxes)

    print("检测到绝缘子数量:", count)

