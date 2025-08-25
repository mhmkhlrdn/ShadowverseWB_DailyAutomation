import cv2 as cv
import numpy as np
import pyautogui as gui
import os
import time
import pydirectinput as pdi
import os



def load_image(path):
    return cv.imread(path, cv.IMREAD_COLOR)

def find_image(needle, threshold=0.7):
    screenshot = cv.cvtColor(np.array(gui.screenshot()), cv.COLOR_RGB2BGR)
    result = cv.matchTemplate(screenshot, needle, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)
    return (max_val >= threshold, max_loc, needle.shape)

def click_center(max_loc, shape, offset=(0,0)):
    x = max_loc[0] + shape[1] // 2 + offset[0]
    y = max_loc[1] + shape[0] // 2 + offset[1]
    gui.click(x, y)


os.startfile('D:/alila/Steam/steamapps/common/ShadowverseWB/ShadowverseWB.exe')
base_path = os.path.dirname(os.path.abspath(__file__))

title_indicator   = load_image(os.path.join(base_path, 'TitleScreenIndicator.png'))
park_button       = load_image(os.path.join(base_path, 'ParkButton.png'))
park_indicator    = load_image(os.path.join(base_path, 'ParkIndicator.png'))
battle_indicator  = load_image(os.path.join(base_path, 'BattleScreenIndicator.png'))
mulligan_indicator= load_image(os.path.join(base_path, 'MulliganIndicator.png'))
gameover_indicator= load_image(os.path.join(base_path, 'GameOverIndicator.png'))
confirmation_indicator = load_image(os.path.join(base_path, 'ConfirmationIndicator.png'))
quest_indicator = load_image(os.path.join(base_path, 'QuestIndicator.png'))
pack_indicator = load_image(os.path.join(base_path, 'DailyCardIndicator.png'))
skip_button = load_image(os.path.join(base_path, 'SkipButton.png'))

# Title screen to home
while True:
    found, loc, shape = find_image(title_indicator)
    if found:
        print("Found the title screen indicator!")
        time.sleep(3)
        gui.click(1000, 1000)  

        popup_detected = False
        for i in range(3):
            found_popup, loc_popup, shape_popup = find_image(confirmation_indicator)
            if found_popup:
                print("Popup detected: Clicking No")
                gui.click(774, 783)
                popup_detected = True
                break
            else:
                print(f"No popup detected (attempt {i+1}/3)...")
                time.sleep(5)

        if not popup_detected:
            print("No popup after 3 attempts, continuing...")
        for i in range(3):
            found_popup, loc_popup, shape_popup = find_image(pack_indicator)
            skip_detected, skip_loc, skip_shape = find_image(skip_button)
            if found_popup:
                print("Free pack detected: Clicking redeem")
                gui.click(960, 768)
                time.sleep(2)
                gui.click(960, 768)
                time.sleep(2)
                gui.click(960, 768)
                time.sleep(10)
                if skip_detected:
                    print("Skip button detected: Clicking skip")
                    click_center(skip_loc, skip_shape)
                    time.sleep(15)
                    gui.click(960, 768)
                    time.sleep(5)
                    gui.click(960, 768)
                    break
            else:
                print(f"No free pack detected (attempt {i+1}/3)...")
                time.sleep(5)
        
        break

    print("Title screen not found, retrying in 5s...")
    time.sleep(5)

# Home to park
while True:
    found, loc, shape = find_image(park_button)
    if found:
        print("Found the park button!")
        click_center(loc, shape)
        time.sleep(2)
        gui.click(1000, 580)
        break
    print("Park button not found, retrying in 5s...")
    time.sleep(5)

# Park to battle
while True:
    found, loc, shape = find_image(park_indicator)
    if found:
        print("Found the battle button!")
        time.sleep(4)
        pdi.press('f4') 
        time.sleep(3)
        gui.click(1000,800)     
        break
    print("Battle button not found, retrying in 5s...")
    time.sleep(5)

# Private match setup
while True:
    found, loc, shape = find_image(battle_indicator)
    if found:
        print("Found the game indicator!")
        time.sleep(2)
        gui.click(500, 550)  
        time.sleep(2)
        gui.click(500, 550)   
        time.sleep(2)
        gui.click(1200, 780)  
        time.sleep(2)
        gui.click(962, 717)  
        break
    print("Game indicator not found, retrying in 5s...")
    time.sleep(5)

# Ingame loop
while True:
    found, loc, shape = find_image(mulligan_indicator)
    if found:
        print("Found the mulligan indicator!")
        while True:
            over, _, _ = find_image(gameover_indicator)
            if over:
                print("Game over detected, exiting...")
                time.sleep(2)
                gui.press('esc')
                time.sleep(2)
                break
            else:
                gui.click(1731, 500) 
                time.sleep(2)
        break
    print("Mulligan indicator not found, retrying in 5s...")
    time.sleep(5)

# Claiming rewards
while True:
    found, loc, shape = find_image(quest_indicator)
    if found:
        print("Found the quest indicator!")
        time.sleep(3)
        pdi.press('f3') 
        time.sleep(5)
        gui.click(1587, 519)
        time.sleep(4)
        gui.click(1587, 519)
        time.sleep(4)
        gui.click(1587, 753)
        time.sleep(4)
        gui.click(1587, 753)
        time.sleep(4)
        gui.click(500, 900)
        time.sleep(4)
        gui.click(700, 900)
        time.sleep(4)
        gui.click(900, 900)
        time.sleep(4)
        gui.click(1100, 900)
        time.sleep(4)
        gui.click(1300, 900)
        time.sleep(4)
        # Exiting the game and shutting down PC
        pdi.press('alt', 'f4')
        time.sleep(5)
        pdi.press('windows', 'd')
        time.sleep(2)
        pdi.press('alt', 'f4')
        time.sleep(2)
        gui.click('985', '490')
        break
    print("Quest indicator not found, retrying in 5s...")
    time.sleep(5)