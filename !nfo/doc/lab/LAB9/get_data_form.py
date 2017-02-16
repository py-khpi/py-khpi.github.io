#!c:/Documents and Settings/ZYKOV/AppData/Local/Programs/Python/Python35-32/python.exe
print("Content-Type: text/html\n") 
import cgi, cgitb, my_cgi
cgitb.enable()
file=cgi.parse()["filename"][0]
try: 
	f=open(file, encoding="utf-8")
	print(my_cgi.H, "CGI: передача содержимого скрипта ",file)
	for el in f: print(my_cgi.D,el)
except FileNotFoundError: print(my_cgi.D, "Файл ", file, " не найден")
    






    




    
