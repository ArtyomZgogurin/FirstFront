from tkinter import*
import second_window
from tkinter import messagebox
root = Tk()
root['bg'] = 'gainsboro'
root.title('Узнать данные с Билдов')
root.geometry('750x450')
root.resizable(width=True, height=True)

def parser():
  print('скоро мы напишем парсер')
  second_window.second_window_par()
def comment():
  print('скоро мы напишем комментарий')
  messagebox.showinfo('Комментарий отправлен','Отправленно')
def way():
  print('скоро мы научимся искать')
  second_window.second_window_par()

#фрейм для поля парсера
frame_par = Frame(root, bg='snow3', bd=5)
frame_par.place(relx=0.02, rely=0.15, relwidth=0.45, relheight=0.25)
#фрейм для поля коммента
frame_com = Frame(root, bg='snow3', bd=5)
frame_com.place(relx=0.02, rely=0.55, relwidth=0.45, relheight=0.25)
#фрейм для поля пути
frame_way = Frame(root, bg='snow3', bd=5)
frame_way.place(relx=0.53, rely=0.15, relwidth=0.45, relheight=0.25)

#info
info = Label(frame_par, text='Какой билд будем парсить?', bg='snow3', font=30)
info.pack()
info = Label(frame_com, text='Какие изменения подъехали?', bg='snow3', font=30)
info.pack()
info = Label(frame_way, text='Путь до скрипта', bg='snow3', font=30)
info.pack()

#ввод для парсинга
buildPar = Entry(frame_par, bg='white', font=30)
buildPar.pack()
#ввод для коммента
commentBuild=Entry(frame_com, bg='white', font=30)
commentBuild.pack()
#ввод пути
wayBuild=Entry(frame_way, bg='white', font=30)
wayBuild.pack()

#кнопка парсера
btnPar = Button(frame_par, text='Парсить', command=parser)
btnPar.pack()
#кнопка комментария
btnCom = Button(frame_com, text='Добавить комментарий', command=comment)
btnCom.pack()
#кнопка пути
btnWay = Button(frame_way, text='Указать путь', command=way)
btnWay.pack()

root.mainloop()
