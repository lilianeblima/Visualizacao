file = open('C:/Temp/Liliane/Liliane.csv','r')
lista = []
for line in file:
    info = line.replace('\n','').split(';')
    dic = {}
    dic["text"] = info[0]
    dic["size"] = info[1]
    lista.append(dic)
print(lista)
