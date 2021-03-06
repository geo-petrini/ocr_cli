import  os, argparse, logging, getpass, sys, time
from os import path
try:
    try:
        from PIL import Image
    except ImportError:
        import Image

    import pytesseract, stats, log_handler, reader
except ModuleNotFoundError as m:
    print(f"Error: {m}")
    print("Use 'installModules.bat' to automatically install all the required dependencies")

# --------------------------------------------------------------------
# Questo è il file principale che esegue il programma.
# 
# authors: Thaisa De Torre, Viktorija Tilevska
# version: 25.02.2021
# last modified: 29.04.2021
# -------------------------------------------------------------------
def main():
    start_time = time.time()
    pytesseract.pytesseract.tesseract_cmd = ".\\Tesseract-OCR\\tesseract.exe"
    log_handler.get_configure_logger()
    logging.info("Program started")

    # ------ Creazione parametri -----------
    parser = argparse.ArgumentParser(usage="ocr [-h] source [-dest] [-lang] [-prefix] [--stats]")
    parser.add_argument('source', type=str, nargs='+', help='source image file path, could also be a directory. Only PNG and JPG are accepted.')
    parser.add_argument('-dest', '-d', default=".\scans", type=str, help='output file path. Default directory: ".\scans"')
    parser.add_argument('-lang', '-l', default="eng", type=str, choices=['eng', 'ita'], help='the language. Choose between ita(italian) or eng(english). Default is eng')
    parser.add_argument('-prefix', '-p', default="scan", type=str, help='output file name, if there are more files it defines the prefix')
    parser.add_argument('--stats', action="store_true", default=False, help='to print the execution time and the number of counted word of the scan')
   
    # Debug 
    args = parser.parse_args()
    logging.debug("parametri creati: source={}, dest={}, lang={}, prefix={}, stats={}".format(
        args.source, args.dest, args.lang, args.prefix, args.stats
    ))
    
    error = check_params(args)
    logging.debug(f"checking params, error code: {error}")
    # se i parametri sono vuoti stampa la guida e chiude il programma ritornando l'errore
    if error:
        parser.print_help()
        sys.exit(1)

    #scan, ritorna un dizionario con i file scannerizzati
    output = reader.scan(args.source, args.lang) 
    
    #output, ritorna un 
    dest_file = reader.output(output, args.dest, args.prefix)

    #ev. print stats
    if args.stats:
        print(stats.get_stats(dest_file, (time.time() - start_time)))


# checks if the params are valid. if not throws an error and displays the command usage.
def check_params(args):
    error = 0
    if args.dest == "''" or args.dest == "":
        logging.error(f"Error: {args.dest}, param dest is not valid\n")
        error = 1
    
    if args.lang == "''" or args.lang == "":
        logging.error(f"Error: {args.lang}, param lang is not valid\n")
        error = 1

    if args.prefix == "''" or args.prefix == "":
        logging.error(f"Error: {args.prefix}, param prefix is not valid\n")
        error = 1

    return error


# controlla la versione minima di python installata
def checkPyVersion():
    if sys.version_info.major < 3:
        #logging.debug("vers major: "+ sys.version_info.major)
        print("Error: min Python version is 3.6.0, please upgrade")
        sys.exit(1)
    else:
        if sys.version_info.minor < 6:
            #logging.debug("vers minor: "+ sys.version_info.minor)
            print("Error: min Python version is 3.6.0, please upgrade")
            sys.exit(1)


if __name__ == "__main__":
    checkPyVersion()
    main()