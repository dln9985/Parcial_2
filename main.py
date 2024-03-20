from lib import *
import sys

print("")

arrayNum=[69,75,173,34,7,54,55,185,165,169,8,96, 104,37,188,106,98,156,179,29,70,93,36,147,89,6,178,15,137,142,78,32,187,168,6,136,82,123,63,57,114,18,51,172,124,11,99,2,25,74,112,127,159,88,22,33,83,44,197,185,1,92,181,9,77,60,166,128,195,84,200,138,138,5,42,55,36,139,93,106,196,75,135,132,87,169,7,134,127,123,185,155,19,110,193,29,66,109,3,100]

nodoRaiz = nodo(arrayNum[0])

for i in range(1, len(arrayNum), 1):
    agregaNodos(nodoRaiz,arrayNum[i])
    
#for i in arrayNum:
    #agregaNodos(nodoRaiz, i)
    
#j=1
#while arrayNum:
    #agregaNodos(nodoRaiz, arrayNum[j])
    #j+=1
    
printThree(nodoRaiz)

inOrderArr = []
PreOrderArr = []
PostOrderArr = []

LVR(nodoRaiz, inOrderArr)
print("In Order:", end=" ")
print(inOrderArr)

VLR(nodoRaiz, PreOrderArr)
print("PreOrder:", end=" ")
print(PreOrderArr)

LRV(nodoRaiz, PostOrderArr)
print("PostOrder:", end=" ")
print(PostOrderArr)

sys.exit("Fin del programa")

print("---------------------------------------")
print("") 

arrNodos=[16,5,7,12,9,20,18,3,10,14]
nodoraiz = None

for i in range(0, len(arrNodos), 1):
    if i == 0:
        nodoraiz = nodo(arrNodos[i])
    else:
        NodosOrdenados(nodoraiz, nodo(arrNodos[i]))
    pass

printThree(nodoraiz)

print("")