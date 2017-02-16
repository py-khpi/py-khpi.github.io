class Virt_zoo:
    ''' Виртуальные зверюшки'''
    def __init__(self,name,mood):
        print('Появилась зверюшка.')
        self.name=name
        self.__mood=mood
    def talk(self):
        print('Привет! Меня зовут ', self.name, '. Чустрвую себя ', self.__mood, sep='')

v1=Virt_zoo('Колобок','отлично.')
print(v1.name)        
v1.talk()

class My_pickle:
    import pickle
    def __init__(self,file):
        self.file=file
    def put(self,obj):
        f=open(self.file,'wb')
        My_pickle.pickle.dump(obj,f)
    def get(self):
        with open(self.file,'rb')as f:
               return My_pickle.pickle.load(f)

p1=My_pickle('p.dat')
p1.put(v1)
v_new=p1.get()
print(v_new.name)
v_new.talk()
               
class  Smart_zoo (Virt_zoo):
	def  __init__ (self, name, mood, where):
		print (where, end="")
		super ().__init__(name, mood)
	def  talk (self):
		print ( "Я – "  +self.name+ "."  )
	def  tell (self,obj):
		print ( "А ты кто?"  )
		obj.talk()
		print(obj.name, ",", obj.name,'.',sep='',end='')
		if self.name=="Серый волк":
			print(" А я тебя съем!")
		else:
			print(" А давай дружить!")
               
s1=Smart_zoo( 'Колобок' , 'превосходно.' ,  'Волшебный лес. ' )
s2=Smart_zoo( 'Серый волк' , 'очень голодным.' ,  'Там же. ' )
s1.__class__=Virt_zoo
s2.talk()
s2.tell(s1)
s1.__class__=Smart_zoo
s1.talk()
s1.tell(s2)

class  New_zoo (Smart_zoo, My_pickle):
    def __init__ (self, name, mood, where, file):
        print (where,'Появилалсь зверюшка.')
        self.name=name
        self.file=file
    def tell (self,obj):
        print ( 'А ты кто? ' )
        obj.talk()
        print (obj.name+ ", я сохраню твои данные." )
        self.put(obj)

s1=Smart_zoo( 'Золотая рыбка' , 'чудесно' , 'Море. ' )
n1=New_zoo( 'Колобок' , 'хорошо.' , 'Берег моря.' , 'obj.dat' )
n1.talk()
n1.tell(s1)
s2=n1.get()
print(s2.name)




