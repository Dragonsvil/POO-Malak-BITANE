from tkinter import * 
window = Tk()
window.title("tk")
window.geometry("400x300")

#numero 1
name_label1 = Label(window, text = "Enter Num 1 : ")
name_label1.grid(column = 0, row = 0, sticky='w')
v1 = StringVar()

name_entry1 = Entry(window, textvariable = v1, width=20)
name_entry1.focus_set()
name_entry1.grid(column=1, row=0, sticky='sw', columnspan=1, padx=10)


#numero 2
name_label2 = Label(window, text = "Enter Num 2 : ")
name_label2.grid(column = 0, row = 1, sticky='w')
v2 = StringVar()

name_entry2 = Entry(window, textvariable = v2, width=20)
name_entry2.focus_set()
name_entry2.grid(column=1, row=1, sticky='sw', columnspan=1, padx=10)


#numero 3
name_label3 = Label(window, text = "The Sum is : ")
name_label3.grid(column = 0, row = 2, sticky='w')
v3 = StringVar()

Entry(window, textvariable=v3, state="readonly").grid(row=2, column=1)

send_button = Button(window, text = "Show", pady=2, command=lambda: v3.set(int(v1.get()) + int((v2.get()))))
send_button.grid(column=1, row=3, sticky='sw', pady=20)

send_button = Button(window, text = "Quit", pady=2, command=window.quit)
send_button.grid(column=0, row=3, sticky='sw', pady=20)

window.mainloop()