from tkinter import *
class My_frame2(Frame):
        '''  Рамка с кнопкой, подсчитывающей события  '''
        def __init__(self,master):
                super().__init__(master) 
                self.grid()
                self.bt_clicks=0
                self.create_widgets()
        def create_widgets(self):
                ''' Создает кнопку '''
                self.bt1=Button(text='Число щелчков: 0',
                    command=self.count,
                    width='20',
                    height='2',        
                    bg='#efffef',
                    font='arial 14',
                    fg='blue' )
                self.bt1.grid()
        def count(self):
                self.bt_clicks+=1
                self.bt1['text']='Число щелчков: '+str(self.bt_clicks)
		
root=Tk()  
root.title('Обработка событий')
root.geometry('240x60+800+300')
app=My_frame2(root)
root.mainloop()
          
