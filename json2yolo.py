import os
import json

json_folder = "dataset/images"
image_folder = "dataset/images"
label_folder = "dataset/labels"

os.makedirs(label_folder, exist_ok=True)

for file in os.listdir(json_folder):
    if file.endswith(".json"):

        json_path = os.path.join(json_folder, file)

        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        txt_name = file.replace(".json", ".txt")
        txt_path = os.path.join(label_folder, txt_name)

        with open(txt_path, "w") as txt:

            for shape in data["shapes"]:

                label = shape["label"]
                points = shape["points"]

                x1, y1 = points[0]
                x2, y2 = points[1]

                img_w = data["imageWidth"]
                img_h = data["imageHeight"]

                x_center = ((x1 + x2) / 2) / img_w
                y_center = ((y1 + y2) / 2) / img_h
                w = abs(x2 - x1) / img_w
                h = abs(y2 - y1) / img_h

                txt.write(f"0 {x_center} {y_center} {w} {h}\n")

print("转换完成")