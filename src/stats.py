import re
import argparse

"""
Lettura file e stampa qta parole.

author: Thaisa De Torre
version: 04.02.2021

"""
# creare parametri necessari
parser = argparse.ArgumentParser(usage="stats [-h] src dest lang name [-stats]")
parser.add_argument('source', type=str, help='source file path, could also be a directory')
parser.add_argument('-dest', default="./dest", type=str, help='output file path')
parser.add_argument('-lang', default="en", type=str, choices=['en', 'it'], help='the language. it = italian, en = english')
parser.add_argument('-prefix', default="scan", type=str, help='output file name, if there are more files it defines the prefix')


args = parser.parse_args()
#print(args) #debug
#print(args.dest)#debug

reliability = "<> %" #"80-90%" ? da controllare
time = "<> ms" #calcolare tempo
stats = "Statistiche esecuzione:\nQuantità parole scannerizzate: {}\nTempo: {}\nAffidabilità: {}"

# gersione file - lettura
#path = "C:/Users/admin/Documents/loremIpsum.txt"
#path = "C:/Users/admin/Documents/prova.txt"
path = args.source
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
path = "{}/{}.txt".format(args.dest, args.prefix) #gestire il '/' !!
handle = open(path, "w")

if handle.writable():
    handle.write(stats.format(qta, time, reliability))

handle.close()