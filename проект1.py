from tkinter import *
from tkinter import filedialog

def clicked():  
    file=filedialog.askopenfilename()
    
    

window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('500x500')

lbl = Label(window, text="Файл:", font=("Arial Bold", 10))  
lbl.grid(column=0, row=0)

file = Entry(window, width=50)
file.grid(column=5, row=0)

btn = Button(window, text="найти", command=clicked)  # кнопка
btn.grid(column=50, row=0)



from tkinter.ttk import Checkbutton  
  
  

chk1_state = BooleanVar()  
chk1_state.set(True)  # задайте проверку состояния чекбокса  

chk2_state = BooleanVar()  
chk2_state.set(True)

chk3_state = BooleanVar()  
chk3_state.set(True)

chk4_state = BooleanVar()  
chk4_state.set(True)

chk5_state = BooleanVar()  
chk5_state.set(True)  

chk1 = Checkbutton(window, text='Выбрать', var=chk1_state)  
chk1.grid(column=0, row=10)

chk2= Checkbutton(window, text='Выбрать', var=chk2_state)  
chk2.grid(column=0, row=15)

chk3= Checkbutton(window, text='Выбрать', var=chk3_state)  
chk3.grid(column=0, row=20)

chk4= Checkbutton(window, text='Выбрать', var=chk4_state)  
chk4.grid(column=0, row=25)

chk5= Checkbutton(window, text='Выбрать', var=chk5_state)  
chk5.grid(column=0, row=30)






from tkinter.ttk import Radiobutton  
  
 

rad1 = Radiobutton(window, text='сравнить', value=1)  

rad1.grid(column=0, row=5)  
 






window.mainloop()
