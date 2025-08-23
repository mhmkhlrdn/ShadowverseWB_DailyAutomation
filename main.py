import cv2 as cv
import numpy as np
import pyautogui as gui
import os
import time
import pydirectinput as pdi

def load_image(path):
    return cv.imread(path, cv.IMREAD_COLOR)

def find_image(needle, threshold=0.8):
    screenshot = cv.cvtColor(np.array(gui.screenshot()), cv.COLOR_RGB2BGR)
    result = cv.matchTemplate(screenshot, needle, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)
    return (max_val >= threshold, max_loc, needle.shape)

def click_center(max_loc, shape, offset=(0,0)):
    x = max_loc[0] + shape[1] // 2 + offset[0]
    y = max_loc[1] + shape[0] // 2 + offset[1]
    gui.click(x, y)


os.startfile('D:/alila/Steam/steamapps/common/ShadowverseWB/ShadowverseWB.exe')

title_indicator   = load_image('TitleScreenIndicator.png')
park_button       = load_image('ParkButton.png')
park_indicator    = load_image('ParkIndicator.png')
battle_indicator  = load_image('BattleScreenIndicator.png')
mulligan_indicator= load_image('MulliganIndicator.png')
gameover_indicator= load_image('GameOverIndicator.png')
confirmation_indicator = load_image('ConfirmationIndicator.png')
quest_indicator = load_image('QuestIndicator.png')

while True:
    found, loc, shape = find_image(title_indicator)
    if found:
        print("Found the title screen indicator!")
        gui.click(1000, 1000)  

        popup_detected = False
        for i in range(3):
            found_popup, loc_popup, shape_popup = find_image(confirmation_indicator)
            if found_popup:
                print("Popup detected: Clicking No")
                gui.click(x=774, y=783)  # adjust coords for "No"
                popup_detected = True
                break
            else:
                print(f"No popup detected (attempt {i+1}/3)...")
                time.sleep(5)

        if not popup_detected:
            print("No popup after 3 attempts, continuing...")

        break  # exit main loop after handling title + popup

    print("Title screen not found, retrying in 5s...")
    time.sleep(5)


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


while True:
    found, loc, shape = find_image(park_indicator)
    if found:
        print("Found the battle button!")
        time.sleep(2)
        pdi.press('f4')  # Press F4 to start the game
        # gui.keyDown("alt")
        # time.sleep(4)
        # gui.keyUp("alt")
        # gui.click(1780,260)     
        time.sleep(2)
        gui.click(1000,800)     
        break
    print("Battle button not found, retrying in 5s...")
    time.sleep(5)


while True:
    found, loc, shape = find_image(battle_indicator)
    if found:
        print("Found the game indicator!")
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

while True:
    found, loc, shape = find_image(mulligan_indicator)
    if found:
        print("Found the mulligan indicator!")
        while True:
            over, _, _ = find_image(gameover_indicator)
            if over:
                print("Game over detected, exiting...")
                gui.hotkey('alt', 'f4')
                break
            else:
                gui.click(1731, 500) 
                time.sleep(2)
        break
    print("Mulligan indicator not found, retrying in 5s...")
    time.sleep(5)

while True:
    found, loc, shape = find_image(quest_indicator)
    if found:
        print("Found the quest indicator!")
        pdi.press('f3') 
        gui.click(1587, 519)
        time.sleep(2)
        gui.click(1587, 753)
        time.sleep(2)
        gui.click(500, 900)
        time.sleep(2)
        gui.click(700, 900)
        time.sleep(2)
        gui.click(900, 900)
        time.sleep(2)
        gui.click(1100, 900)
        time.sleep(2)
        gui.click(1300, 900)
        time.sleep(2)
        break
    print("Quest indicator not found, retrying in 5s...")
    time.sleep(5)