import tkinter
from tkinter import ttk
import time
import serial

window = tkinter.Tk()
window.geometry("1200x670")
window.title("CONTROLER FOR ARDUINO")
window.resizable(0,0)

arduino = serial.Serial("COM3", 9600, timeout = 0.1)

class CONTROL():
    def __init__(self):
        self.num_zip = 0
        self.img1 = tkinter.PhotoImage(file="src\controller\img\slide1.PNG").subsample(4,4)
        self.img2 = tkinter.PhotoImage(file="src\controller\img\slide2.PNG").subsample(4,4)
        self.img3 = tkinter.PhotoImage(file="src\controller\img\slide3.PNG").subsample(4,4)
        self.img4 = tkinter.PhotoImage(file="src\controller\img\slide4.PNG").subsample(4,4)
        self.img5 = tkinter.PhotoImage(file="src\controller\img\jump.PNG").subsample(4,4)
    def setting(self):
        self.but1 = tkinter.Button(window,relief=tkinter.RAISED,image=self.img1,command=self.forword).place(x=270,y=25)
        self.but2 = tkinter.Button(window,relief=tkinter.RAISED,image=self.img2,command=self.right).place(x=480,y=230)
        self.but3 = tkinter.Button(window,relief=tkinter.RAISED,image=self.img3,command=self.back).place(x=270,y=435)
        self.but4 = tkinter.Button(window,relief=tkinter.RAISED,image=self.img4,command=self.left).place(x=55,y=230)
        self.but_stop = tkinter.Button(window,relief=tkinter.RAISED,image=self.img5,command=self.stop).place(x=270,y=230)
        self.upGoing = tkinter.Button(window,relief=tkinter.RAISED,text="UPUPUP",height=3,command=self.up).place(x=700,y=25)
        self.downGOing = tkinter.Button(window,relief=tkinter.RAISED,text="DOWNDOWN",height=3,command=self.down).place(x=700,y=80)
    def forword(self):
        self.result_forword = '1'
        self.label_forword = tkinter.Label(window,bg="white",text="FORWORD",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_forword))
    def back(self):
        self.result_back = '3'
        self.label_back = tkinter.Label(window,bg="white",text="BACK",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_back))
    def right(self):
        self.result_right = '4'
        self.label_right = tkinter.Label(window,bg="white",text="RIGHT",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_right))
    def left(self):
        self.result_left = '2'
        self.label_left = tkinter.Label(window,bg="white",text="LEFT",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_left))
    def stop(self):
        self.result_jump = '5'
        self.label_jump = tkinter.Label(window,bg="white",text="STOP",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_jump))
    def up(self):
        self.result_jump = '6'
        self.label_jump = tkinter.Label(window,bg="white",text="UP",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_jump))
    def down(self):
        self.result_jump = '7'
        self.label_jump = tkinter.Label(window,bg="white",text="DOWN",font=("","30","bold"),width=15,height=2).place(x=765,y=500)
        arduino.write(str.encode(self.result_jump))

eva = CONTROL()
eva.setting()

window.mainloop()
arduino.close()