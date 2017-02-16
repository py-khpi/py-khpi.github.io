from tkinter import *
class My_frame(Frame):
        '''  Рамка для работы с текстом  '''
        def __init__(self,master):
                super(My_frame, self).__init__(master)
                self.grid()
                self.create_widgets() 
        def create_widgets(self):
                ''' Создает 2 метки, текстовое поле, текстовую область и кнопку'''
        #метка-инструкция
                self.lb1=Label(self,
                        text='Как прожить до 100 лет?', fg='blue', font='arial 14')  
                self.lb1.grid(row=0, column=0, columnspan=2, sticky=W)
        #метка-пароль
                self.lb2=Label(self, text='Пароль',fg='blue', font='arial 10')
                self.lb2.grid(row=1, column=0, sticky=E) 
        #текстовое поле для ввода пароля
                self.ent=Entry(self,bg='#f0f0ff', font='arial10')
                self.ent.grid(row=1, column=1, sticky=E) 
        #создание текстовой области, куда будет помещен ответ
                self.txt=Text(self, width=30, height=4, wrap=WORD, bg='#f0f0ff',
                              font='arial 10')
                self.txt.grid(row=2, column=0, columnspan=2) 
        #кнопка отправки сообщения
                self.bt=Button(self,
                        text='Узнать секрет',
                        fg='blue', bd='5', font='arial 12',
                        command=self.reveal)
                self.bt.grid(row=3, column=0, sticky=W)
        def reveal(self):
                contents=self.ent.get()
                if contents=='secret':
                        message='Чтобы прожить до 100 лет, надо сначала '\
                        'про;ить 99 лет и 11 месяwев, а потом вести себя '\
                        'очень-очень осторожно.\n'
                else:
                        message='Вы ввели неправильный пароль.'
                self.txt.delete(0.0,END)
                self.txt.insert(0.0,message)


root=Tk()  
root.title('Работа с текстом')
root.geometry('250x160+850+300')
root.resizable(True, False)
app=My_frame(root)
root.mainloop()
          
