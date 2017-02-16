WORDS='компьютер',
      'программа',
      'протокол',
      'спецификация'
from random import choice,randrange
word=choice(WORDS)
correct=word
ana=''
while word:
    pos=randrange(len(word))
    ana+=word[pos]
    word=word[:pos]+word[pos+1:]
print('''
       Игра "АНАГРАММА"
       Для выхода - нажмите клавишу Enter''')
print('Вот анаграмма', ana.upper())
ans=input('Попробуй отгадать слово  ')
while ans !=correct and ans !='':
      print('Ответ неверный')
      ans=input('Попробуй еще раз ')
if ans==correct:
      print('Молодец!')
print('Спасибо за игру')      
input()
