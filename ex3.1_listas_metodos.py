# append
lista = []

lista.append(1)
lista.append("python")
lista.append([40, 30, 20])

print(lista)

#clear
lista = [1, "python", [40, 30, 20]]
print(lista)

lista.clear()
print(lista)

#copy
lista = [1, "python", [40, 30, 20]]
l2 = lista.copy()
l2[0] = 2

print(lista)
print(l2)

#count
cores = ["vermelho", "azul", "verde", "azul"]
cores.count("vermelho")
cores.count("azul")
cores.count("verde")

#extend
linguagens = ["python", "js", "c"]
print(linguagens)

linguagens.extend(["java", "csharp"])
print(linguagens) 

# index
print(linguagens.index("java"))
print(linguagens.index("python"))

#pop
linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0)
print(linguagens)

# remove


# reverse
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)

#sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse = True) 
print(linguagens)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) 
print(linguagens)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse= True)
print(linguagens)
#len
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))

#sorted
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))