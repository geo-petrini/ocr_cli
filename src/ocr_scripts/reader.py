import argparse, pytesseract, logging, sys, os.path, glob
from pathlib import Path
from os import path
try:
    from PIL import Image
except ImportError:
    import Image

"""
Lettura immaggine e scrittura del output nel file.

author: Viktorija Tilevska, Thaisa De Torre
version: 11.02.2012
last change: 15.04.2021
"""

# -----------------------------------------------------------------------
# Fa lo scan di tutti i file validi. Se non ci sono file validi il programma finisce
#
# args: dizionario di argomenti da controllare
# -----------------------------------------------------------------------
def scan(args):
    valid_files = validate_source(args.source)
    files_text = {}

    if len(valid_files) != 0:
        for f in valid_files:
            files_text[f] = {}
            files_text[f]['txt'] = img_to_text(f, args.lang)

        return files_text
    else:
        logging.error("Program stopped. No valid files were inserted.")
        sys.exit(1)
    
# -----------------------------------------------------------------------
# Fa tutti i controlli e i cambiamenti in modo da avere una lista con solamente
# i file validi da scannerizzare.
#
# source: lista con i percorsi sorgente
# return: una lista con tutti i percorsi validi per l'ocr
# -----------------------------------------------------------------------
def validate_source(source):
    valid_files = [] #contiene tutti i file validi (jpg, png)
    file_list = len(source)
    logging.debug(f"Files inserted: {file_list}")

    for img in source:
        # mask
        f = glob.glob(img)
        source.extend(f)
        source.pop(source.index(img))

    logging.debug(f"Source after mask: {source}")

    for img in source:    
        if check_permission(img):     
            if path.isfile(img):
                if has_valid_ext(img):
                    valid_files.append(img)
                else:
                    logging.debug(f"file {img} not valid")
                    #sys.exit(1)
            elif path.isdir(img):
                dir_list = get_dir_content(img)
                logging.debug(f"dir list: {dir_list}")

                for f in dir_list:
                    if has_valid_ext(f):
                        valid_files.append(img)

    logging.info(f"List of valid files ({len(valid_files)}): {valid_files}")
    logging.info("scanning files...")
    return valid_files

# -----------------------------------------------------------------------
# Controlla se il formato del file al percorso path sia accettato dall'ocr (png o jpg o jpeg). 
#
# src: percorso del file da controllare
# return: true se il formato è accettato, altrimenti false
# -----------------------------------------------------------------------            
def has_valid_ext(src):
    valid = False
    valid_extensions = ['.png', '.jpg', '.jpeg']
    file_ext = os.path.splitext(src)[-1]
    #if file_ext in valid_extensions and check_permission(src):
    if file_ext.lower() in valid_extensions:
        valid = True
        logging.debug(f"File {src} is valid")
    else:       
        #sys.exit(1) #per il TC-001.bat
        logging.warning("Error: A file has not been accepted. Please insert PNG and/or JPG/JPEG files")
    return valid

# --------------------------------------------------
# Controlla se il file è accessibile in lettura
#
# path: il percorso del file da controllare 
# returns: true se il file è accessibile, altrimenti ritorna false
# -------------------------------------------------
def check_permission(path):
    valid = False
    try:
        with open(path, 'r') as outfile:
            valid = True
    except OSError:
        logging.warning(f"File {path} is not readable")
   
    # if os.access(path, os.R_OK):
    #     valid = True
    # else:
    #     logging.warning(f"File {path} is not readable")

    return valid

# ------------------------------------------------------------
# Prende e ritorna il contenuto della cartella nel percorso path.
#
# path: percorso della cartella
# returns: una lista con i file contenuti nella cartella
# ------------------------------------------------------------
def get_dir_content(path):
    if len(os.listdir(path)) != 0:
        return os.listdir(path)
    else:
        logging.debug(f"The directory {path} is empty")
        return None

# -----------------------------------------------------------------------
# Passa un'immagine all'ocr che la legge e ne ritorna il testo.
#
# file: il percorso del file
# lang: la lingua
# return: una stringa con il contenuto dell'immagine
# ----------------------------------------------------------------------- 
def img_to_text(img, lang):
    # logging.info("scanning file")
    try:
        text = pytesseract.image_to_string(Image.open(img), lang)
        return text
    except FileNotFoundError:
        logging.exception(f"Error: file {img} not found")
        return None

# ----------------------------------------------------------
# Scrive il contenuto text nel file al percorso path in utf-8.
#
# text: il testo da scrivere nel file
# path: il percorso del file
# ----------------------------------------------------------
def write_output(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ----------------------------------------------------------------------- 
# Gestisce tutta la parte di output, controlla che la destinazione esista e che si possa scrivere
# Se è un file scrive direttamente (sovrascrive se gia esiste) mentre se è una cartella gestisce eventuali duplicati.
#
# output: è un dizionario contente l'associazione tra immagine e testo
#   scannerizzato insieme ad altre info.
# dest: la destinazione in cui scrivere l'output. Se è un file scrive tutto li,
#    se è una cartella salverà le scansioni in quella dir.
# prefix: il prefisso che avrà il file di output per evitare duplicati
#    nella stessa cartella.
# ----------------------------------------------------------------------- 
def output(output, dest, prefix):
    logging.info("checking output")
    dir = os.path.dirname(dest)
    logging.info(f"basename: {path.basename(dest)}")
    logging.info(f"dirname: {dir}")
    logging.info(f"common path: {path.normpath(dest)}")

    p = dest
    # dirname empty = no parent dir
    if dir == "" or dir == ".": 
        logging.debug(f"dirname empty. path to check = dest")
    # dirname parent
    else: 
        logging.debug(f"dirname: {dir}, path to check = dir")
        p = dir

    if path.isdir(p): 
        if not path.basename(dest) == dest:
            dest_file = dest
        else:
            dest_file = validate_dest(p, prefix) 
            logging.debug(f"DIR: dest [{p}] exists. dest_file: {dest_file}")
    # dest dir. es: dest = "Dnd"
    elif (path.splitext(p)[-1] == "") and not (path.exists(p)):
        create_dir(p)
        dest_file = dest
        logging.debug(f"DIR: dest [{p}] exists. dest_file: {dest_file}")
    # dest file (indifferente se esiste o meno). es: dest = "intro.txt"
    else:
        dest_file = dest
        logging.debug(f"FILE: dest [{p}] exists. dest_file: {dest_file}")

    try:
        write_output(merge_output(output), dest_file)
    except PermissionError:
        logging.exception(f"Permission error on {path}")
    except FileNotFoundError:
        logging.exception(f"Error file not found on {path}")


# --------------------------------------------------------------------------
# Prende il testo scannerizzato da ogni elemento del dizionario (da ogni immagine)
# e lo mette in un unico testo per poi ritornarlo.
#
# output: il dizionario con associate le immagini con il testo
# --------------------------------------------------------------------------
def merge_output(output):
    logging.info("merging scanned output")
    text = ""
    for key, value in output.items():
        text += f"\n-----{key}-----\n\n" + value["txt"]

    return text

# --------------------------------------------------------------------------
# Crea una cartella al percorso passato se essa non esiste già.
#
# path: il percorso in cui creare la cartella
# --------------------------------------------------------------------------
def create_dir(path):
    path = os.path.normpath(path)
    try:
        os.mkdir(path)
        logging.info(f"Created directory {path}")
    except OSError as e:
        logging.exception(f"Directory {path} already exists")
    except FileNotFoundError:
        logging.exception(f"Error file not found: {path}")        

# -------------------------------
# Gestisce il prefisso del file di destinazione per non avere duplicati.
#
# dest: la destinazione in cui scrivere l'output. Se è un file scrive tutto li,
#    se è una cartella salverà le scansioni in quella dir.
# prefix: il prefisso che avrà il file di output per evitare duplicati
#    nella stessa cartella.
# -------------------------------
def validate_dest(dest, prefix):
    output_file_name = prefix + ".txt"
    dest_file = f"{dest}\{output_file_name}"
    logging.debug(f"path dest file: {dest_file}")

    if path.exists(dest_file):
        dir_content =  get_dir_content(dest)
        logging.debug(f"dir content: {dir_content}")
        id = 1
        output_file_name = f"{prefix}_{id}.txt"

        for file in dir_content:
            if file == output_file_name:
                id = id +1
            output_file_name = f"{prefix}_{id}.txt"
                
        dest_file = f"{dest}\{output_file_name}"
        logging.debug(f"dest file: {dest_file}")

    return dest_file
