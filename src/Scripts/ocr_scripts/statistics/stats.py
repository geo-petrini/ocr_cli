import argparse
import logging

"""
Lettura file e stampa qta parole.

author: Thaisa De Torre
version: 04.02.2021
last change: 11.02.2021
"""

logging.basicConfig(
    #filename='\log\debug.log', filemode='a',
    format='%(asctime)s:  %(message)s', 
    datefmt='%d/%m/%Y %I:%M:%S', 
    level=logging.DEBUG
)
logging.info("Start logging")

# ------ Creazione parametri -----------
parser = argparse.ArgumentParser(usage="stats [-h] src dest lang name [-stats]")
parser.add_argument('source', type=str, help='source file path, could also be a directory')
parser.add_argument('-dest', default=".\scans", type=str, help='output file path. Default directory: <.\scans>')
parser.add_argument('-lang', default="en", type=str, choices=['en', 'it'], help='the language. Choose between it(italian) or en(english). Default is en')
parser.add_argument('-prefix', default="scan", type=str, help='output file name, if there are more files it defines the prefix')

args = parser.parse_args()
logging.info("parametri creati:")
logging.debug("source[{}], dest[{}], lang[{}], prefix[{}]".format(
    args.source, args.dest, args.lang, args.prefix
))
#print(args) #debug
#print(args.dest)#debug


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
    logging.info("parole contate")
    return qta


# ---------------------------------------------------------
# Scrive nel file passato come parametro le statistiche
# 
# dest: il percorso del file in cui scrivere le statistiche
# ---------------------------------------------------------
def write_stats(dest):
    #path = "{}/{}.txt".format(args.dest, args.prefix) #gestire il '/' !!
    if dest == ".\scans":
        dest = ".\scans\{}.txt".format(args.prefix)
    
    words = count_words(args.source)
    handle = open(dest, "w")

    reliability = "<> %" #"80-90%" ? da controllare
    time = "<> ms" #calcolare tempo
    stats = "Statistiche esecuzione:\n\nQuantita' parole scannerizzate: {}\nTempo: {}\nAffidabilita': {}"

    if handle.writable():
        handle.write(stats.format(words, time, reliability))

    handle.close()
    

#x = count_words(args.source)
write_stats(args.dest)
#print(x)