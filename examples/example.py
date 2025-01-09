import keyboard
import time

from imagelocatorlib.locator_library import locate_and_move_to_image

def main(image_path, timeout=10):
    # region = (800, 0, 1920, 230)  
    region = None
    print(f' Press "cntrl+shift+x" to locate image')
    while True:
        if keyboard.is_pressed('ctrl+shift+x'):
            _ = locate_and_move_to_image(image_path, confidence=0.65, region=region, grayscale=True)
            time.sleep(1)
        if keyboard.is_pressed('esc'):
            return 

image_path = r"edge_tabs.png"

if __name__ == "__main__":
    main(image_path)