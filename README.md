# Bot for help in the game Murder by Numbers

<video width="1920" height="1080" controls><source src="./BotVideo6x.mp4" type="video/mp4"></video>

Example video of the bot in the 6x speed

## How to use

First of all, this bot was created in a 1920 for 1080 screen, so it only function in the scale 16:9, and only the minor diference is capable of make it don't function correctly.

For use this bot, download the code, install python if you use Windows (in mac and linux this alredy comes installed), install tesseract (more information in https://github.com/tesseract-ocr/tesseract), and run the following commands:

`pip install pyautogui picross_solver pytesseract cv2 imutils`

Open simultaneously the terminal in the code folder and the game, and run the following command

`python Bot.py`

You need to do this with the game being the last window used

### For Linux Users
If you use linux, you need to install `scrot` to. For example, in a Debian based system:

`sudo apt install scrot`

Note: In linux, the pyautogui, dependenci used for controling the screen, only function in xorg/X11

## FAQ

### Motivation
I'm currently playing the game  [*Murder by Numbers*](https://store.steampowered.com/app/1140290/Murder_by_Numbers/). I’ve really enjoyed the story, but after solving around 100 puzzles, I’ve gotten a bit tired of them. However, I still want to finish the story, so I decided to create this bot to help me out.
