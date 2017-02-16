from tkinter import *
class My_frame1(Frame):
        '''  Рамка с тремя кнопками  '''
        def __init__(self,master):
                super().__init__(master)
                self.grid()
                self.create_widgets() 
        def create_widgets(self):
                ''' Создает три кнопки '''
                self.bt1=Button(self,text='Кнопка №1', fg='blue', font='12')
                self.bt1.grid()
                self.bt2=Button(self)
                self.bt2.grid()
                self.bt2['text']='Кнопка №2'
                self.bt2['fg']='blue'
                self.bt2['font']='12'  
                self.bt3=Button(self)
                self.bt3.grid()
                self.bt3.config(text='Кнопка №3', fg='blue', font='12')
		
root=Tk()  #Создание базового окна
root.title('Рамка с кнопками')
root.geometry('230x95+800+200')
app=My_frame1(root)
root.mainloop()
