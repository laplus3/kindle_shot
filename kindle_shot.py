import subprocess
import os
import time

def take_screenshot(file_path):
    subprocess.run(["adb", "shell", "screencap", "/sdcard/screenshot.png"])
    subprocess.run(["adb", "pull", "/sdcard/screenshot.png", file_path])

def swipe(direction, start_x, start_y, end_x, end_y, duration):
    if direction == "right":
        subprocess.run(["adb", "shell", "input", "touchscreen", "swipe", str(start_x), str(start_y), str(end_x), str(end_y), str(duration)])
    elif direction == "left":
        subprocess.run(["adb", "shell", "input", "touchscreen", "swipe", str(end_x), str(end_y), str(start_x), str(start_y), str(duration)])
    else:
        raise ValueError("Invalid swipe direction. Use 'right' or 'left'.")

def capture_swipe_and_save(num_pages, direction, save_location="Screenshots", file_prefix="screenshot", swipe_duration=0.2):
    if not os.path.exists(save_location):
        os.makedirs(save_location)

    start_x, start_y, end_x, end_y, duration = 500, 1000, 100, 1000, 200  # Default swipe values

    for i in range(num_pages):
        file_path = f"{save_location}/{file_prefix}_{i}.png"
        
        take_screenshot(file_path)

        # スワイプの方向に基づいて実行
        swipe(direction, start_x, start_y, end_x, end_y, duration)

        time.sleep(swipe_duration)

# 218ページ分のスクリーンショットを指定された方向にスワイプして取得（例: 右にスワイプ）
capture_swipe_and_save(0, direction="left", save_location="", file_prefix="ページ", swipe_duration=0.1)
