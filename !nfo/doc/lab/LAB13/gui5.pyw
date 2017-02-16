from tkinter import *
class My_frame5(Frame):
        '''  Использование флажков  '''
        def __init__(self,master):
                super(My_frame5, self).__init__(master)
                self.grid()
                self.create_widgets() 
        def create_widgets(self):
                ''' Создает переключатель '''
                #метка-инструкция
                Label(self,
                        text='Укажите любимую телепередачу', font='arial 13', fg='blue'
                        ).grid(row=0, column=0,sticky=W)
                self.favorite=StringVar()
                self.favorite.set(None)
                #положение переключателя 'Футбол'
                Radiobutton(self,
                        text='Футбол',
                        variable=self.favorite,
                        value='о футболе',
                        command=self.update_text
                        ).grid(row=1, column=0,sticky=W)
                #положение переключателя 'История' 
                Radiobutton(self,
                        text='История',
                        variable=self.favorite,
                        value='об истории',                            
                        command=self.update_text
                        ).grid(row=2, column=0,sticky=W)
                #положение переключателя 'Природа'
                Radiobutton(self,
                        text='Природа',
                        variable=self.favorite,
                        value='о природе',    
                        command=self.update_text
                        ).grid(row=3, column=0,sticky=W)
                #текстовая область для результата
                self.results_txt=Text(self, fg='blue', font='10', width=40, height=5, wrap=WORD)
                self.results_txt.grid(row=4, column=0, columnspan=3)
        def update_text(self):
                message="Ваша любимая телепередача - "
                message+=self.favorite.get()
                self.results_txt.delete(0.0,END)
                self.results_txt.insert(0.0,message)
                
root=Tk()  
root.title('Использование переключателя')
root.geometry('310x120+800+200')
app4=My_frame5(root)
root.mainloop()
          
