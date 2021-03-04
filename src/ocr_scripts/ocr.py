try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract, os, argparse, logging
import stats, log_handler, reader

# ------------------------
# Questo è il file principale che esegue il programma.
# 
# authors: Thaisa De Torre, Viktorija Tilevska
# version: 25.02.2021
# last modified: 25.02.2021
# ------------------------

def main():
    pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'
    log_handler.get_configure_logger()
    logging.info("Program started")

    # ------ Creazione parametri -----------
    parser = argparse.ArgumentParser(usage="stats [-h] src dest lang name [-stats]")
    parser.add_argument('source', type=str, nargs='+', help='source image file path, could also be a directory. Only PNG and JPG are accepted.')
    parser.add_argument('-dest', '-d', default=".\scans", type=str, help='output file path. Default directory: ".\scans"')
    parser.add_argument('-lang', '-l', default="eng", type=str, choices=['eng', 'ita'], help='the language. Choose between it(italian) or en(english). Default is en')
    parser.add_argument('-prefix', '-p', default="scan", type=str, help='output file name, if there are more files it defines the prefix')
   
    args = parser.parse_args()
    logging.debug("parametri creati: source {}, dest {}, lang {}, prefix {}".format(
        args.source, args.dest, args.lang, args.prefix
    ))

    #read file
    #scan file
    for fname in args.source:
        reader.check_img_type(fname, args.dest, args.lang, args.prefix)
    #ev. print stats
    #write output

if __name__ == "__main__":
    main()