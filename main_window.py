from tkinter import*
import second_window
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import xml.etree.ElementTree as ET
import os, fnmatch

root = Tk()
root['bg'] = 'white'
root.title('Узнать данные с Билдов')
root.geometry('750x450')
root.resizable(width=True, height=True)

path = "C:\\testttttt"
files = []
file_names = []

#фрейм для поля парсера
frame_par = Frame(root, bg='snow3', bd=5)
frame_par.place(relx=0.02, rely=0.15, relwidth=0.45, relheight=0.25)
#фрейм для поля коммента
frame_com = Frame(root, bg='snow3', bd=5)
frame_com.place(relx=0.02, rely=0.55, relwidth=0.45, relheight=0.25)
#фрейм для поля пути
frame_way = Frame(root, bg='snow3', bd=5)
frame_way.place(relx=0.53, rely=0.15, relwidth=0.45, relheight=0.25)
#фрейм для canvasa
frame_pic = Frame(root, bg='white', bd=5)
frame_pic.place(relx=0.68, rely=0.88, relwidth=0.45, relheight=0.25)

imageEm =Image.open('emblem1.png')
image1 = ImageTk.PhotoImage(imageEm)


#info
info = Label(frame_par, text='Какой билд будем парсить?', bg='snow3', font=30)
info.pack()
info = Label(frame_com, text='Какие изменения подъехали?', bg='snow3', font=30)
info.pack()
info = Label(frame_way, text='Путь до отчётов', bg='snow3', font=30)
info.pack()
info = Label(frame_pic, image=image1, bg='snow3', font=30)
info.pack()
#устанавливаем привязку к вводным данным
input_parser=StringVar()
input_comment=StringVar()
input_way=StringVar()
#ввод для парсинга
buildPar = Entry(frame_par, bg='white', font=30, textvariable=input_parser )
buildPar.pack()
#ввод для коммента
commentBuild=Entry(frame_com, bg='white', font=30, textvariable=input_comment )
commentBuild.pack()
#ввод пути
wayBuild=Entry(frame_way, bg='white', font=30, textvariable=input_way)
wayBuild.pack()

def xml_parse(xml_file, tag):
    result = {}
    results = xml_file.findall(tag)
    j = -1
    t = True
    for i in results:                          
        while t == True:  
            try:
                j += 1                                    #парсим 35 тегов    
                temp = i[j].text.strip()            #закидваем значение, удаляя пробелы
                name = i[j].tag              
                result[name] = temp                 #добавляем "тег = значение" в словарь
            except:
                AttributeError
                FileNotFoundError
                try:                                #если вдруг в теге есть аттрибуты, то добавляем их
                    j += 1                                      
                    temp = i[j].attrib            
                    name = i[j].tag              
                    result[name] = temp             #добавляем "тег = аттрибут" в словарь    
                except:
                    AttributeError
                    FileNotFoundError
                    t = False
                    pass
                

    for i in result:
        print(i, '=', result[i])              #выводим всё, что распарсили
    print('Файл пропарсен')

def get_map_name(file):                            #вытаскиваем название карты из имени файла
    map_name = ''
    index = file.index('_wotreplay')
    temp = file[index-1]
    while not temp.isdigit():                                       
        temp = file[index-1] 
        index -= 1            
        map_name += temp
    while temp.isdigit():
        temp = file[index-1]
        index -= 1       
        map_name += temp
    map_name = map_name[::-1]
    map_name = map_name[1:]   
    return map_name


def way_input():
    try:
        print('Введите название стенда:')
        dir = input_way.get()                                   #вводим название стенда (папки)
        listOfFiles = os.listdir(path + '\\' + dir)     #добавляем его в путь
        print('Введите расширение файлов для парсинга:')
        pattern_for_file = '*.' + input()               #вводим расширение файла для парсинга(для демо, захардкодим расширение, когда доделаем)

        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern_for_file):
                print('Добавлен файл для парсинга ' + entry)    
                files.append(path + '\\' + dir + '\\' + entry)   #создаем список файлов с полным путем
                file_names.append(entry)                        #создаем отдельно список названий файлов
        if files == []:                                         #если список по итогу пустой, то файлов с нужным расширением у нас нет
            print('Файлов с таким расширением не найдено')
        else:
            print('Введите название тега для парсинга:')        #вводим тег, внутри которого мы будем доставать инфу
            input_tag = input()
    
        for i in files:                                         
            try:
                xml_file = ET.parse(i)
                print('Парсим файл', i)
                print('Название карты: ' + get_map_name(i))     #выводим название карты для каждого файла
                xml_parse(xml_file,input_tag)                   
            except:
                FileNotFoundError
                xml_file = ET.parse(i)                          #except для файлов другой структуры(если нет в имени файла название карты)
                xml_parse(xml_file,input_tag)                   
                pass  
    except:
        FileNotFoundError
        print('Такой дериктории не найдено')
def parser():
  print('скоро мы напишем парсер')
  second_window.second_window_par()
def comment():
  print('скоро мы напишем комментарий')
  messagebox.showinfo('Комментарий отправлен',input_comment.get())
def way():
  print('скоро мы научимся искать')
  file = filedialog.askopenfilename()



#кнопка парсера
btnPar = Button(frame_par, text='Парсить', command=parser)
btnPar.pack()
#кнопка комментария
btnCom = Button(frame_com, text='Добавить комментарий', command=comment)
btnCom.pack()
#кнопка пути
btnWay = Button(frame_way, text='Указать путь', command=way_input)
btnWay.pack()

root.mainloop()
