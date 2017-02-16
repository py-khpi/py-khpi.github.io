class My_list:
    ''' Пользовательский класс, напоминающий список ''' 
    def __init__(self,values=None):
        if values is None:
            self.values=[]
        else:
              self.values=values
    def __getitem__(self,key):
        ''' Получить значение по ключу '''
        return self.values[key]
    def __setitem__(self,key,value):
        ''' Установить значение по ключу '''
        self.values[key]=value
    def first(self):
        ''' Получить значение первого элемента '''
        return self.values[0]
    def last(self):
        ''' Получить значение последнего элемента '''
        return self.values[-1]
    def __iter__(self):
        ''' Сделать последовательность итерабельной '''
        return iter(self.values)
    def __str__(self):
        ''' Возвратить строковое представление объекта '''
        return 'My_list: '+str(self.values)
    def __len__(self):
        ''' Возвратить длину последовательности '''
        return len(self.values)
    def __add__(self,value):
        ''' Добавить элемент '''
        self.values[len(self):len(self)]=value
    def __delitem__(self,key):
        ''' Удалить элемент '''
        del self.values[key]
    def push(self,value):
        ''' Добавить элемент в конец последовательности '''
        self.values[len(self):len(self)]=value
    def pop(self):
        l=self.values[-1]
        del self.values[-1]
        return l
m1=My_list([1,2,3,4,5,6,7,8])
print(m1[3])
m1[3]=777
print(m1)
print(m1.first())       
print(m1.last())   
for i in m1:
    print(i,end=' ')
    
print('\n',m1)
m1+[55]
print(m1)
print(len(m1))
del m1[1]
print(m1)
m1.push('cat')
print(m1)
print(m1.pop())
print(m1)
