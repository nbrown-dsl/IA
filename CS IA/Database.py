from tkinter import*
import sqlite3

root = tk.Tk()
root.title("Database")
root.geometry("750x500")

conn = sqlite3.connect('TeachersDatabase.db')

conn.cusror()

c.execute(""CREATE TABLE addresses (
   first_name text,
   last_name text,
   year text,
   results text,
   improvements text,
   goals text,
""))
def submit():
 conn = sqlite3.connect('TeachersDatabase.db')

 c = conn.cursor()

 c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :year, :results, :improvements, :goals)",)
          {
              'f_name': f_name.get(),
              'l_name': l_name.get(),
              'year': year.get(),
              'results': results.get(),
              'improvements': improvements.get(),
              'goals': goals.get(),
          }
          f_name.delete(0, END)
          l_name.delete(0, END)
          year.delete(0, END)
          results.delete(0, END)
          improvements.delete(0, END)
          goals.delete(0, END)

def query():
    return

    conn = sqlite3.connect('TeachersDatabase.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()
    print(records)

    for record in records[0]:
        print_records += str(record[0]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()

    conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1,padx20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1,padx20)
year = Entry(root, width=30)
year.grid(row=2, column=1,padx20)
results = Entry(root, width=30)
results.grid(row=3, column=1,padx20)
improvements = Entry(root, width=30)
improvements.grid(row=4, column=1,padx20)
goals = Entry(root, width=30)
goals.grid(row=5, column=1,padx20)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
year_label = Label(root, text="Year")
year_label.grid(row=2, column=0)
results_label = Label(root, text="Results")
results_label.grid(row=3, column=0)
improvements_label = Label(root, text="Improvements")
improvements_label.grid(row=4, column=0)
goals_label = Label(root, text="Goals")
goals_label.grid(row=5, column=0)

submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, cloumn=0, columnspand=2, pady=10, padx=10, ipadx=137)

conn.commit()

conn.close()

root.mainloop()
