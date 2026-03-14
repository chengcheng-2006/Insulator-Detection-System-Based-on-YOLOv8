import cv2
from ultralytics import YOLO

# 加载模型
model = YOLO("runs/detect/train/weights/best.pt")

# 打开视频
cap = cv2.VideoCapture("test_video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO检测
    results = model(frame)

    # 画检测框
    annotated_frame = results[0].plot()

    # 缩小画面
    resized_frame = cv2.resize(annotated_frame, (800, 600))

    # 显示窗口
    cv2.imshow("YOLO Detection", resized_frame)

    # 按 q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()