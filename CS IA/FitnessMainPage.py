import tkinter as tk

root = tk.Tk()
root.title("Fitness app for teachers")
root.geometry("750x500")

label = tk.Label(root, width=22, text="In this app teachers will be able to document results of students", anchor='w')
label.config(font=("Comic sans",16))
label.pack(side=tk.TOP, pady = 30)

row = tk.Frame(root)
label = tk.Label(row, width=22, text="Number 1", anchor='w')
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

def resultss(char):
 return char.replace(".", "0", 1).isdigit()

 b1 = tk.Button(root, width = 15, text='Add', background = "Grey", command=(lambda: add_val()))
b1.config(font=("Comic sans", 18))   
b1.pack(side=tk.RIGHT, padx=5, pady=5)

