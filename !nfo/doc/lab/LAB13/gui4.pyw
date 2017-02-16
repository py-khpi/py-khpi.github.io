from tkinter import *
class My_frame4(Frame):
        '''  Использование флажков  '''
        def __init__(self,master):
                super(My_frame4, self).__init__(master)
                self.grid()
                self.create_widgets() 
        def create_widgets(self):
                ''' Создает три флажка '''
                #метка-описание
                Label(self,
                	text='Укажите любимые телепередачи', font='arial 13', fg='blue' 
			).grid(row=0, column=0,sticky=W)
                #метка-инструкция
                Label(self,
                        text='Выберете все, что нравится', font='arial 11',
                        fg='blue').grid(row=1, column=0, sticky=W)
                #флажок 'Футбол'
                self.likes_football=BooleanVar()
                Checkbutton(self,text='Футбол', 
                        variable=self.likes_football,
                        command=self.update_text
                        ).grid(row=2, column=0,sticky=W)
                #флажок 'История'
                self.likes_history=BooleanVar()
                Checkbutton(self,
                        text='История', 
                        variable=self.likes_history,
                        command=self.update_text
                        ).grid(row=3, column=0, sticky=W)
                #флажок 'Природа'
                self.likes_nature=BooleanVar()
                Checkbutton(self,
                        text='Природа', 
                        variable=self.likes_nature,
                        command=self.update_text
                        ).grid(row=4, column=0, sticky=W)
                #текстовая область с результатом
                self.results_txt=Text(self, fg='blue', font='11', width=40, height=5, wrap=WORD)
                self.results_txt.grid(row=5, column=0, columnspan=3)
        def update_text(self):
                likes=""
                if self.likes_football.get():
                        likes+='Вам нравится футбол\n'
                if self.likes_history.get():
                        likes+='Вас привлекает история\n'
                if self.likes_nature.get():
                        likes+='Вам небезразлична природа\n'
                self.results_txt.delete(0.0,END)
                self.results_txt.insert(0.0,likes)
                
root=Tk()  
root.title('Использование флажков')
root.geometry('270x185+800+200')
app4=My_frame4(root)
root.mainloop()
          
