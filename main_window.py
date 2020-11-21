from tkinter import*
import second_window
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import xml.etree.ElementTree as ET
import os, fnmatch
import time


root = Tk()
root['bg'] = 'white'
root.title('Узнать данные с Билдов')
root.geometry('750x450')
root.resizable(width=True, height=True)

comment = ''                                      #КОММЕНТ ДЛЯ АРТЕМА  
start_time = time.time()                          #засекаем время
path = "C:\\testttttt"                            #задаем корневаю папку (тут будет инфа от GUI)
pattern_for_file = '*.btl'                        #задаем расширение файлов, которые будем парсить

#фрейм для поля парсера
frame_par = Frame(root, bg='snow3', bd=5)
frame_par.place(relx=0.02, rely=0.10, relwidth=0.45, relheight=0.25)
#фрейм для поля коммента
frame_com = Frame(root, bg='snow3', bd=5)
frame_com.place(relx=0.02, rely=0.35, relwidth=0.45, relheight=0.25)
#фрейм для поля пути
frame_build = Frame(root, bg='snow3', bd=5)
frame_build.place(relx=0.02, rely=0.6, relwidth=0.45, relheight=0.25)
#фрейм для canvasa
frame_pic = Frame(root, bg='white', bd=5)
frame_pic.place(relx=0.68, rely=0.88, relwidth=0.45, relheight=0.25)

imageEm =Image.open('emblem1.png')
image1 = ImageTk.PhotoImage(imageEm)


#info
info = Label(frame_par, text='Ревизия билда', bg='snow3', font=30)
info.pack()
info = Label(frame_com, text='Комментарий', bg='snow3', font=30)
info.pack()
info = Label(frame_build, text='Путь до отчётов', bg='snow3', font=30)
info.pack()
info = Label(frame_pic, image=image1, bg='snow3', font=30)
info.pack()
#устанавливаем привязку к вводным данным

path_roots=StringVar()
input_comment=StringVar()
input_build=StringVar()
def xml_parse(xml_file):
    result = []
    #result = {}                                    #словарь на случай словаря)
    results = xml_file.findall('results')           #находим тег <results>
    j = -1
    t = True
    for i in results:                      
        while t == True:  
            try:
                j += 1                                      
                temp = i[j].text.strip()            #закидваем значение, удаляя пробелы
                #name = i[j].tag                    #берем имя каждого тега на всякий случай
                result.append(temp)                 #ДОБАВЛЯЕМ КАЖДОЕ ЗНАЧЕНИЕ В СПИСОК result[]
            except IndexError:
                t = False
                pass
                
    #for i in result:
        print(result)              #выводим всё, что распарсили (А КОНКРЕТНЕЕ СПИСОК СО ВСЕМИ ЗНАЧЕНИЯМИ ПО ПОРЯДКУ)
    print('Файл пропарсен')

def get_map_name(file):                            #вытаскиваем название карты из имени файла
    index = file.index('.wotreplay')
    temp = file[0:index]
    return temp

def get_stand_name(folder):
    stand_name = folder[0:-19]
    return stand_name

def main_parsing():
    print('введите')
    path_root = path_roots.get()
    build_number = input_build.get()
    comment = input_comment.get()
    files = []                                      #список файлов с полным путем
    file_names = []                                 #список названий файлов                                  
    list_of_folders = os.listdir(path_root)         #список имен папок 
    count_d = 0                                     #каунтер папок
    count_f = 0                                     #каунтер файлов
    print('Список папок в корне:')
    for dir in list_of_folders:                                         #выводим список папок в корне с нумерацией
        count_d += 1
        print(str(count_d) + '. ' + dir)

    try:
        for dir in list_of_folders:                                     #идем по каждой папке в корне
            new_path = path_root + '\\' + dir                                             
            listOfFiles = os.listdir(new_path)     
            print('Добавлена директория для парсинга ' + new_path)             

            for entry in listOfFiles:                                      #идем по каждому файлу в папке
                if fnmatch.fnmatch(entry, pattern_for_file):
                    print('Добавлен файл для парсинга ' + dir + '\\' + entry)    
                    files.append(new_path + '\\' + entry)           #создаем список файлов с полным путем
                    file_names.append(entry)                        #создаем отдельно список названий файлов
                    get_table_name = get_stand_name(dir) + get_map_name(entry)         #СОЗДАЕМ TABLE_NAME
                    print('Название таблицы: ' + get_table_name)            
    

            if files == []:                                         
                print('Файлов в папке', dir, 'не найдено')
    
            for i in files:                                #парсим все каждый файл в папке         
                try:
                    xml_file = ET.parse(i)
                    print('Парсим файл', i)                    
                    xml_parse(xml_file)
                    count_f += 1
                    
                except FileNotFoundError:           
                    print('Ошибка в файле ' + xml_file)         #если название файла корявое, то скипаем его         
                    pass
            files = []                                          #обнуляем список файлов

    except FileNotFoundError:    
        print('Такой дериктории не найдено')

    print('Пропарсено папок: ' + str(count_d))
    print('Пропарсено файлов: ' + str(count_f))
    print("за %s seconds" % (time.time() - start_time))



#ввод для парсинга
buildPar = Entry(frame_par, bg='white', font=30, textvariable=input_build)
buildPar.pack()
#ввод для коммента
commentBuild=Entry(frame_com, bg='white', font=30, textvariable=input_comment)
commentBuild.pack()
#ввод пути
wayBuild=Entry(frame_build, bg='white', font=30, textvariable=path_roots)
wayBuild.pack()


#кнопка парсера
btnPar = Button(frame_build, text='Парсить', command=main_parsing)
btnPar.pack()
#кнопка комментария
#btnCom = Button(frame_com, text='Добавить комментарий', command=comment)
#btnCom.pack()
#кнопка пути
#btnWay = Button(frame_build, text='Указать путь', command=build_input)
#btnWay.pack()

root.mainloop()
