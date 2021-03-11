import argparse, sys

parser = argparse.ArgumentParser(usage="prova [-h] src dest lang name [-stats]")
parser.add_argument('source', type=str, nargs='+', help='source image file path, could also be a directory. Only PNG and JPG are accepted.')
parser.add_argument('-dest', '-d', default=".\scans", type=str, help='output file path. Default directory: ".\scans"')
parser.add_argument('-lang', '-l', default="eng", type=str, choices=['eng', 'ita'], help='the language. Choose between it(italian) or en(english). Default is en')
parser.add_argument('-prefix', '-p', default="scan", type=str, help='output file name, if there are more files it defines the prefix')

args = parser.parse_args()
print(f"d[{args.dest}]")

def create_output_file(source, dest, lang, prefix): 
    create_and_change_directory(dest)
    logging.debug(f"src to open: {source}")
    logging.debug(f"img open src: {Image.open(source)}")
    text_to_write = pytesseract.image_to_string(Image.open(source), lang)
    file_name = f"{prefix}.txt"
    fileslist = os.listdir()
    
    if not fileslist:
        write_file(file_name, text_to_write)
        logging.debug(f"w file ok")
    else:
        if all(f in file_name for f in fileslist):
            write_existing_file(file_name, text_to_write)
        else:
            write_file(file_name, text_to_write)

def check_img_type(source, dest, lang, prefix):
    image_ext = os.path.splitext(source)[-1]
    if image_ext.lower() == ".png" or image_ext.lower() == ".jpg":
        create_output_file(source, dest, lang, prefix)
    else:       
        logging.info("Error: Formato non accettato. Inserire immagini di tipo .png e/o .jpg")

def write_stats(dest):
    try:
        handle = open(dest, "w")
    except FileNotFoundError:
        return sys.exit(-1) 

    reliability = "<> %" #"80-90%" ? da controllare
    time = "<> ms" #calcolare tempo
    stats = "Statistiche esecuzione:\n\nQuantita' \nTempo: {}\nAffidabilita': {}"

    if handle.writable():
        handle.write(stats.format(time, reliability))

    handle.close()

write_stats(args.dest)
parser.print_help()