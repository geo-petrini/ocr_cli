import argparse
import logging
# --------------------------------------------------------
# Questo è il file che si occupa delle statistiche degli scan.
# 
# author: Thaisa De Torre
# version: 25.02.2021
# last modified: 29.04.2021
# --------------------------------------------------------


# ---------------------------------------------------------
# Conta le parole contenute nel file passato come argomento.
# 
# file: il percorso del file da cui contare le parole
# ---------------------------------------------------------
def count_words(file):
    handle = open(file, "r")

    if handle.readable():
        lines = handle.readlines()
        qta = 0

        for line in lines:
            words = line.split(" ")
            qta += len(words)

    handle.close()
    logging.info(f"parole contate: {qta}")
    return qta

# ---------------------------------
# Ritorna le statistiche.
#
# source: il file da cui contare le parole
# time: il tempo impiegato in secondi
# ---------------------------------  
def get_stats(source, time):
    words = count_words(source)
    time = f"{time:.5} seconds" 

    return f"Statistiche esecuzione:\n\nParole scannerizzate: {words}\nTempo totale: {time} s\n"