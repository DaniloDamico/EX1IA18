import time
import random
from customDictionary import CustomDictionary
from fillCSV import FillCSV


'''
Caricare una lista di elementi casuali e testarla per ogni tipo
di struttura dictionary presa in esame.
Ripetere per n volte e confrontare le miedie dei tempi al
variare degli algoritmi e dei parametri
'''

x = 100         #   numero di test da eseguire
y = 100         #   numero di elementi su cui opera l'array
z = 0.001       #   indice di dispersione

def input():
    """
    la probabilità che esistano due elementi identici nella lista è dello 0.001%
    gli input variano da -50*y a 50*y
    """
    random.seed(time.time())
    l = []
    for i in range (0, y):
        l.append(int(random.random() * z * y * 1000) - y * z * 500)
    return l

def testSwag(b, v2, v3):

    """

    :param b:
    :param v2: parametro per calcolare il massimo
    :param v3: parametro per calcolare il minimo
    :return:
    """
    elapsed = 0

    for i in range(0, x):           #   numero di test

        v = input()
        M = b + b * int(v2 / b)     # max
        m = b * int(v3 / b)         # min

        d = CustomDictionary(M, m, b)
        start = time.time()
        for j in range(0, y):
            d.insert(v[j], v[j])
        for j in range(0, y):
            d.search(v[j])
        for j in range(0, y):
            d.delete(v[j])
        elapsed = elapsed + (time.time() - start)

    tempoMedio = elapsed/x
    FillCSV(str (b), str(tempoMedio), "customDictionary")
    print ("CustomDictionary\t" + "(b : " + str(b) + "\tmax : " + str(M) + "\tmin : " + str(m) + ")\t:\t" +str(tempoMedio))

def testDictionary():
    t = 0
    for i in range(0, x):
        v = input()
        d = {}
        start = time.time()
        for j in range(0, y):
            d[v[j]] = v[j]
        for j in range(0, y):
            d.get(v[j])
        for j in range(0, y):
            try:
                d.pop(v[j])
            except:
                None
        t = t + (time.time() - start)
    print ("PyDictionary\t :\t\t\t" +str(t / x))



if __name__ == "__main__":
    testDictionary()

    print("primo test: molta dispersione\n") # uso lo z definito in alto: z = 0.001
    for i in range(1,4):
        y = 10*(10**i)
        print("test con\t" + str(y) + "\telementi\n")
        testSwag(6 + 2**i, 500*y, -500*y)

    print("secondo test: poca dispersione\n")
    z = 1.0
    for i in range(1,4):
        print("test con\t" + str(y) + "\telementi\n")
        testSwag(6 + 2**i, 50*y, -50*y)
