import argparse
import logging

# ---------------------------------------------------------
# Conta le parole contenute nel file passato come argomento.
# 
# source: il percorso del file da cui contare le parole
# ---------------------------------------------------------
def count_words(source):
    #source = "C:/Users/admin/Documents/loremIpsum.txt"
    #source = "C:/Users/admin/Documents/prova.txt"
    handle = open(source, "r")

    if handle.readable():
        lines = handle.readlines()
        qta = 0

        for line in lines:
            words = line.split(" ")
            qta += len(words)

    handle.close()
    logging.info(f"parole contate: {qta}")
    return qta


# ---------------------------------------------------------
# Scrive nel file passato come parametro le statistiche
# 
# dest: il percorso del file in cui scrivere le statistiche
# ---------------------------------------------------------
def write_stats(dest):
    #path = "{}/{}.txt".format(args.dest, args.prefix) #gestire il '/' !!
    if dest == ".\scans":
        dest = f".\scans\{args.prefix}.txt"
    
    words = count_words(args.source)
    handle = open(dest, "w")

    reliability = "<> %" #"80-90%" ? da controllare
    time = "<> ms" #calcolare tempo

    if handle.writable():
        handle.write(
            f"Statistiche esecuzione:\n\nQuantita' parole scannerizzate: {words}\nTempo: {time}\nAffidabilita': {reliability}"
        )

    handle.close()
    
def get_stats(source, time):
    words = count_words(source)

    reliability = "<> %" #"80-90%" ? da controllare
    time = f"{time} seconds" #calcolare tempo

    return f"Statistiche esecuzione:\n\nQuantita' parole scannerizzate: {words}\nTempo: {time}\nAffidabilita': {reliability}"
        


#x = count_words(args.source)
#write_stats(args.dest)
#print(x)