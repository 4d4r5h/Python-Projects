import pyautogui, math, time

time.sleep(3)       # open paint in this time frame
i = 828
j = 60
print(pyautogui.size())        # For mine, the output is Size(width=1366, height=768)

for radius in range(20, 220, 20):
    pyautogui.click(325, 70)        # click on brush
    pyautogui.moveTo(768, 60)       # pick black color
    pyautogui.click()
    t = 0
    while t <= 360:
        x = 600 + round(radius * math.cos(t * (math.pi / 180)))         # using parametric equation of circle
        y = 400 + round(radius * math.sin(t * (math.pi / 180)))
        if t == 0:
            pyautogui.moveTo(x, y)
        else:
            pyautogui.dragTo(x, y)
        t += 10         # for smooth circle

    pyautogui.click(265, 70)        # click on bucket
    if i < 970:
        pyautogui.moveTo(i, j)      # picking different colors
        i += 21
    else:
        i = 828
        j = 80
    pyautogui.click()
    pyautogui.moveTo(600 + (radius - 5), 400)
    pyautogui.click()
