try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract, os, argparse, logging, getpass, sys
import stats, log_handler, reader


# ------------------------
# Questo è il file principale che esegue il programma.
# 
# authors: Thaisa De Torre, Viktorija Tilevska
# version: 25.02.2021
# last modified: 11.03.2021
# ------------------------

def main():
    username = getpass.getuser()
    # pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\"+username+"\\Documenti\\ocr_cli\\src\\ocr_scripts\\Tesseract-OCR\\tesseract.exe"
    log_handler.get_configure_logger()
    logging.info("Program started")

    # ------ Creazione parametri -----------
    parser = argparse.ArgumentParser(usage="ocr [-h] source [-dest] [-lang] [-prefix] [-stats]")
    parser.add_argument('source', type=str, nargs='+', help='source image file path, could also be a directory. Only PNG and JPG are accepted.')
    parser.add_argument('-dest', '-d', default=".\scans", type=str, help='output file path. Default directory: ".\scans"')
    parser.add_argument('-lang', '-l', default="eng", type=str, choices=['eng', 'ita'], help='the language. Choose between it(italian) or en(english). Default is en')
    parser.add_argument('-prefix', '-p', default="scan", type=str, help='output file name, if there are more files it defines the prefix')
   
    args = parser.parse_args()
    logging.debug("parametri creati: source={}, dest={}, lang={}, prefix={}".format(
        args.source, args.dest, args.lang, args.prefix
    ))
    
    er_code = check_params(args)
    logging.debug(f"checking params, error code: {er_code}")
    if er_code:
        parser.print_help()
        sys.exit(1)

    #read file
    #scan file
    for fname in args.source:
        reader.check_img_type(fname, args.dest, args.lang, args.prefix)
    #ev. print stats
    #write output


# checks if the params are valid. if not throws an error and displays the command usage.
def check_params(args):
    error = 0
    if args.dest == "''":
        logging.error(f"Errore: il percoro {args.dest} non e' valido")
        error = 1
    
    if args.lang == "''":
        logging.error(f"Errore: la lingua {args.lang} non e' valido")
        error = 1

    if args.prefix == "''":
        logging.error(f"Errore: il prefisso {args.prefix} non e' valido")
        error = 1

    return error
    

if __name__ == "__main__":
    main()