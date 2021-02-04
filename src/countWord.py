import re


reliability = "%" #"80-90%" ? da controllare
time = "20sec" #calcolare tempo
stats = "Statistiche esecuzione:\nQuantità parole scannerizzate: {}\nTempo: {}\nAffidabilità: {}"

# gersione file - lettura
#path = "C:/Users/admin/Documents/loremIpsum.txt"
path = "C:/Users/admin/Documents/prova.txt"
handle = open(path, "r")

if handle.readable():
    lines = handle.readlines()
    qta = 0

    for line in lines:
        words = line.split(" ")
        qta += len(words)


    print(stats.format(qta, time, reliability))
handle.close()

# gestione file - scrittura
path = ""
handle = open(path, "w")
if handle.writable():
    handle.write(stats.format(qta, time, reliability))
handle.close()
