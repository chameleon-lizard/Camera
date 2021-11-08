import tkinter as tk
import numpy as np
import datetime
import cv2 as cv

from PIL import Image, ImageTk, ImageDraw, ImageFont

class App():    
    def __init__(self, overlay: str) -> None:
        # Creating the window
        self.window = tk.Tk()
        self.window.geometry("1824x2280")
        
        # Creating a label for video frames
        self.label = tk.Label(self.window)
        self.label.grid(row=0, column=0)
    
        # Creating the capture
        self.capture = cv.VideoCapture()
        self.capture.open("/dev/video0", apiPreference=cv.CAP_V4L2)
        self.capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc("M", "J", "P", "G"))
        self.capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        self.capture.set(cv.CAP_PROP_FRAME_WIDTH, 960)
        self.capture.set(cv.CAP_PROP_FPS, 30)
        self.video()
        self.window.mainloop()
    
    def video(self):
        cap = cv.cvtColor(self.capture.read()[1], cv.COLOR_BGR2RGB)
        cap = cv.resize(cap, (1824, 2280))
        captured_image = Image.fromarray(cap)
        draw = ImageDraw.Draw(captured_image)

        font = ImageFont.truetype("font.ttf", 50)

        exp = 6400
        temp = 25
        x = 0
        y = 0
        offset = 50
        draw.text((x, y + offset * 0), str(datetime.datetime.today().strftime("%d/%m/%Y")), (0, 0, 0), font=font)
        draw.text((x, y + offset * 1), str(datetime.datetime.today().strftime("%H:%M:%S")), (0, 0, 0), font=font)
        draw.text((x, y + offset * 2), f"Exposure: {exp}", (0, 0, 0), font=font)
        draw.text((x, y + offset * 3), f"Temperature: {temp}C", (0, 0, 0), font=font)

        img = ImageTk.PhotoImage(image=captured_image)
        self.label.img = img
        self.label.configure(image=img)
        self.label.after(10, self.video)
    

if __name__ == "__main__":
    app = App(0)
