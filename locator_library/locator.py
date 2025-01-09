import pyautogui
from pyautogui import ImageNotFoundException as pyautogui_ImageNotFoundException
import time
from typing import Tuple, Optional
from pyscreeze import ImageNotFoundException


def _wait_until_image_found(image_path, region:Optional[Tuple[int, int, int, int]]=None, confidence=0.7, timeout=10, interval=0.1, grayscale=False):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            if region:
                location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, grayscale=grayscale, region=region)
            else: 
                location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, grayscale=grayscale)
            if location:
                return location
        except ImageNotFoundException:
            continue
        except pyautogui_ImageNotFoundException:
            continue
        except Exception as e:
            print(f"error occured :{e}")
            return None
        time.sleep(interval)
    return None

def locate_and_move_to_image(image_path, confidence=0.5, timeout=10, grayscale=False, region:Optional[Tuple[int, int, int, int]]=None, movement:bool = True) -> bool:
    location = _wait_until_image_found(image_path, confidence=confidence, timeout=timeout, grayscale=grayscale, region=region)
    if location:
        print(f"image found at {location}")
        if movement:
            pyautogui.moveTo(location.x,location.y, duration=0.5)
        return True
    else:
        print("image not found") 
        return False

