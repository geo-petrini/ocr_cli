import argparse
import logging
# --------------------------------------------------------------
# Questo è il file che si occupa delle statistiche degli scan.
# 
# author: Thaisa De Torre
# version: 25.02.2021
# last modified: 29.04.2021
# --------------------------------------------------------------


# --------------------------------------------------------------
# Conta le parole contenute nel file passato come argomento.
# 
# file: il percorso del file da cui contare le parole
# --------------------------------------------------------------
def count_char(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        qta = 0

        for line in lines:
            words = line.split(" ")
            qta += len(words)

    logging.info(f"parole contate: {qta}")
    return qta

def count_char_str(str):
    qta = str.split(" ")
    logging.info(f"parole contate: {len(qta)}")
    return len(qta)

# --------------------------------------------------------------
# Ritorna le statistiche formattate.
#
# source: il file da cui contare le parole
# time: il tempo impiegato in secondi
# --------------------------------------------------------------
def get_stats(source, time):
    words = count_char(source)
    logging.info("Printing stats")
    return f"\nStatistiche esecuzione:\n\tParole scannerizzate: {words}\n\tTempo totale: {time:.5} s\n"