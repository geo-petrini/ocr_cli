# ------------------------
# Questo è il file principale che esegue il programma.
# 
# authors: Thaisa De Torre, Viktorija Tilevska
# version: 25.02.2021
# last modified: 25.02.2021
# ------------------------

#imports
import argparse, logging
import stats.py


def main():
        logging.basicConfig(
        filename='\log\app_debug.log',
        #format='%(asctime)s:  %(message)s', 
        #datefmt='%d/%m/%Y %I:%M:%S', 
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
    logging.debug("parametri creati: source[{}], dest[{}], lang[{}], prefix[{}]".format(
        args.source, args.dest, args.lang, args.prefix
    ))
    #print(args) #debug
    #print(args.dest)#debug

    #read file
    #scan file
    #ev. print stats
    #write output

if __name__ == "__main__":
    main()