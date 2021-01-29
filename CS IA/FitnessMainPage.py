import tkinter as tk
import tkMessageBox

root = tk.Tk()
root.title("Fitness app for teachers")
root.geometry("750x500")

label = tk.Label(root, width=22, text="In this app teachers will be able to document results of students", anchor='w')
label.config(font=("Comic sans",16))
label.pack(side=tk.TOP, pady = 30)

row = tk.Frame(root)
label = tk.Label(row, width=22, text="To document results go to the results page", anchor='w')
label.config(font=("Comic sans",16))
 
validation = row.register(results)
number1 = tk.Entry(row, validate="key", validatecommand=('validation, %S'))
number1.config(font=("Comic sans",16))
 
row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
label.pack(side=tk.LEFT)
number1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
 
row2 = tk.Frame(root)
label2 = tk.Label(row2, width=22, text="Here is where teachers will document the results ", anchor='w')
label2.config(font=("Comic sans",16))
validation = row2.register(results)
number2 = tk.Entry(row2, validate="key", validatecommand=(validation, '%S'))
number2.config(font=("Comic sans",16))
 
row2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
label2.pack(side=tk.LEFT)
number2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

def Resultspage():
   tkMessageBox.showinfo( "ChanigngPage", "Going to the results page")

B = Tkinter.Button(top, text ="You are being sent to the results page. Here you will give the results for your students", command = Resultspage)

B.pack()

def Improvementspage():
   tkMessageBox.showinfo( "ChanigngPage", "Going to the Improvementss page")

B = Tkinter.Button(top, text ="You are being sent to the Improvements page. Here you will give the improvements for your students", command = Resultspage)

B.pack()

def Goalspage():
   tkMessageBox.showinfo( "ChanigngPage", "Going to the goals page")

B = Tkinter.Button(top, text ="You are being sent to the goals page. Here you will set the goals for your students", command = Resultspage)

B.pack()
tk.mainloop()
