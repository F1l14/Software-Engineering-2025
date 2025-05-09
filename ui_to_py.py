import os
import subprocess

ui_folder = "ui"
output_folder = "src/GUI"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(ui_folder):
    if filename.endswith(".ui"):
        ui_path = os.path.join(ui_folder, filename)
        py_name = os.path.splitext(filename)[0] + ".py"
        py_path = os.path.join(output_folder, py_name)
        
        subprocess.run(["pyuic6", ui_path, "-o", py_path])
        print(f"Converted: {filename} → {py_path}")
