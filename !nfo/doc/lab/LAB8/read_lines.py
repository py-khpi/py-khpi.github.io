list_lines=['1-alpha\n','2-alpha\n','3-alpha\n','1-beta\n','2-beta\n','3-beta\n']
with open('lines.txt','w') as f:
    f.writelines(list_lines)
f=open('1lines.txt','r')
for line in f:
    if line[0]=='1':
        print(line,end='')
f.close()


    
