from tkinter import * 
window = Tk()

window.title("Test")
window.geometry("300x300")
window.minsize(200, 200)
window.config(background="sky blue")

label = Label(window, text='Bonjour Python', font=("courrier",20), bg='lavender', fg='black')

bouton = Button (window, text = "Close", command = window.quit)
bouton.pack()

window.mainloop()


