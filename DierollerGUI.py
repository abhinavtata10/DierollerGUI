from tkinter import *
import random

counts = [0,0,0,0,0,0]
rolls = []

window=Tk()
window.geometry("300x300")
window.configure(bg="pink", padx=10, pady=10)
window.title("Die Roller GUI")

def roll():
 randNum = random.randrange(1,7)
 rolls.append(randNum)
 counts[randNum-1] += 1
 label0.configure(text=f"Roll: {randNum}")
 label1.configure(text=f"1: {(counts[0])}")
 label2.configure(text=f"2: {(counts[1])}")
 label3.configure(text=f"3: {(counts[2])}")
 label4.configure(text=f"4: {(counts[3])}")
 label5.configure(text=f"5: {(counts[4])}")
 label6.configure(text=f"6: {(counts[5])}")

frame1 = Frame(window, bg="magenta", height=200, width=200, padx=10, pady=10)
frame1.pack()
frame2 = Frame(window, bg="magenta", height=200, width=200, padx=10, pady=10)
frame2.pack()

label0 = Label(frame1, bg="magenta", fg="white", text="Roll: ", font = ("Courier",17))
label0.pack()

label1 = Label(frame1, bg="magenta", fg="white", text="1: 0", font = ("Courier",17))
label1.pack()

label2 = Label(frame1, bg="magenta", fg="white", text="2: 0", font = ("Courier",17))
label2.pack()

label3 = Label(frame1, bg="magenta", fg="white", text="3: 0", font = ("Courier",17))
label3.pack()

label4 = Label(frame1, bg="magenta", fg="white", text="4: 0", font = ("Courier",17))
label4.pack()

label5 = Label(frame1, bg="magenta", fg="white", text="5: 0", font = ("Courier",17))
label5.pack()

label6 = Label(frame1, bg="magenta", fg="white", text="6: 0", font = ("Courier",17))
label6.pack()

button = Button(frame2, bg= "purple", fg="purple", text="Click Here", height=1, width=5, font = ("",14), command = roll)
button.pack()


window.mainloop()




