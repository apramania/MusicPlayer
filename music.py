from tkinter import *
from pygame import mixer

root = Tk()
mixer.init()

root.geometry('400x400')
root.title("Sweetaah")
root.iconbitmap(r'music_icon.ico')

text = Label(root,text='Let the party begin')
text.pack()

photo = PhotoImage(file = 'play-button.png')
photo1 = PhotoImage(file = 'stop.png')

def play_btn():
    mixer.music.load('shape_of_you.mp3')
    mixer.music.play()

def stop_btn():
    mixer.music.stop()

def vol_btn(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)

btn = Button(root, image = photo, command= play_btn)
btn.pack()

btn1 = Button(root, image = photo1, command = stop_btn)
btn1.pack()

pcale = Scale(root, to=100, orient = HORIZONTAL, command = vol_btn)
pcale.set(70)
pcale.pack()
root.mainloop()