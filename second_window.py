from tkinter import*

def second_window_par():
  root = Tk()
  root['bg'] = 'gainsboro'
  root.title('Результаты')
  root.geometry('750x500')
  root.resizable(width=True, height=True)
  
  #Первый показатель
  frame_par = Frame(root, bg='cornsilk3', bd=5)
  frame_par.place(relx=0.02, rely=0.15, relwidth=0.3, relheight=0.5)
  #Второй показатель
  frame_com = Frame(root, bg='cornsilk3', bd=5)
  frame_com.place(relx=0.34, rely=0.15, relwidth=0.3, relheight=0.5)
  #Третий показатель
  frame_way = Frame(root, bg='cornsilk3', bd=5)
  frame_way.place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.5)
  #info
  info = Label(frame_par, text='Первый показатель', font=30)
  info.pack()
  info = Label(frame_com, text='Второй показатель', font=30)
  info.pack()
  info = Label(frame_way, text='Третий показатель', font=30)
  info.pack()
  root.mainloop()

