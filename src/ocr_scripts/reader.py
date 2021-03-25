import argparse, pytesseract, logging, sys, os.path
from os import path
try:
    from PIL import Image
except ImportError:
    import Image

"""
Lettura immaggine e scrittura del output nel file.

<<<<<<< Updated upstream
author: Viktorija Tilevska
version: 11.02.2021
=======
author: Viktorija Tilevska, Thaisa De Torre
version: 11.02.2012
>>>>>>> Stashed changes
last change: 25.03.2021
"""
# -----------------------------------------------------------------------
# Controlla se gli elementi passati sono dei file o delle cartelle
#
# source: la lista delle immagini da leggere
#
# test: è il metodo main
# returns: ritorna la lista di file validi per la scansione 
# -----------------------------------------------------------------------
def check_source(source, dest, lang, prefix):
    valid_files = [] #contiene tutti i file validi (jpg, png)

    file_list = len(source)
    logging.info(f"count file: {file_list}")

    for img in source:
        if path.isfile(img):
            logging.debug(f"file {img} e' un file")
            
            if is_valid(img):
                logging.debug("e' valido")
                valid_files.append(img)
                logging.debug("aggiunge alla lista validi")

        elif path.isdir(img):
            logging.debug("e' una dir")
            dir_list = read_dir(img)
            logging.debug(f"dir list: {dir_list}")

            for f in dir_list:
                if is_valid(f):
                    valid_files.append(img)

            logging.debug("tutti i file sono validi")
            logging.debug("aggiunge alla lista validi quelli della cartella")

    logging.debug(f"valid list: {valid_files}")
    return valid_files


def scan(valid_files, lang):
    files_text = {} # files_text = { 'c:\cdscsdkl\img.png':'sopra la panca la capra campa', 'c:\miofile.png':'alsa fa la kalsa', ...}
    #list_of_text = []
    if len(valid_files) != 0:
        for f in valid_files:
            # è una dictionary/classe dove ad ogni file viene associato il contenuto dello stesso,
            # si può anche associare il nome del file di output, delle statistiche (stats), filesize, 
            # cronometrare il tempo di scansione per ogni file, ecc
            files_text[f] = {}
            files_text[f]['txt'] = text_from_file(f, lang)
            logging.info("testi e img associati e aggiunti a al dictionary")
    else:
        logging.info("Program stopped. No valid files were inserted.")
    # controllare se è una mark 


# -----------------------------------------------------------------------
# Controlla se il formato dell'immagine è valido e se il file è accessibile. 
#
# src: il percorso dell'immagine
# return: True se il file è valido, False se il file non è valido
#
# test: passare un'immagine con un formato diverso da .jpg e .png e 
# vedere se appare il messaggio d'erroe, provare ad accedere a un'immagine
# inaccessibile e vedere il messagio di erore che esce. 
# -----------------------------------------------------------------------            
def is_valid(src):
    valid = False
    valid_extensions = ['.png', '.jpg', '.jpeg']
    file_ext = os.path.splitext(src)[-1]
    logging.debug(f"file ext: {file_ext}")
    if file_ext in valid_extensions and check_premissions(src):
        logging.debug(f"checking file {src}")
        valid = True
    else:       
        logging.debug("Errore: Formato non accettato. Inserire immagini di tipo .png e/o .jpg")
        sys.exit(1)
    return valid

# --------------------------------------------------
# Controlla se il file è accessibile in lettura
#
# src: il file da controllare 
# returns: True se il file è accessibile, false se i fale non è accessibile
#
# test: passare un file non accesibile
# -------------------------------------------------
def check_premissions(src):
    valid = False
    try:
        with open(src) as f:
            logging.debug("lo legge")
            valid = True
    except IOError:
        logging.debug(f"Errore: il file {src} non è accessibile")

    return valid

# ------------------------------------------------------------
# Controlla se la cartella passata e vuota e se non lo è 
# ne ritorna il contenuto
#
# img: la cartella con delle immagini
# returns: il contenuto della cartella
#
# test: passa una cartella e fai un print del contenuto, passa
# una cartella vuota e guarda il messaggio d'erroe
# ------------------------------------------------------------
def read_dir(img):
    if len(os.listdir(img)) != 0:
        return os.listdir(img)
    else:
        logging.info(f"Error: la cartella {img} e' vuota")
        return None

# -----------------------------------------------------------------------
# Legge ogni immagine della lista e ne salva il cotenuto in un'altra lista 
#
# f: il percorso del file valido
# lang: la lingua -> farla una var globale se la voglio usare con tutti gli altri argomenti, fare una classe
#
# test: 
# ----------------------------------------------------------------------- 
def text_from_file(f, lang):
    try:
        text = pytesseract.image_to_string(Image.open(f), lang)
        logging.debug("img scanned")
        return text
    except FileNotFoundError as fnf_error:
        logging.exception(f"Error: file {f} not found")
        return None

# # -----------------------------------------------------------------------
# # Controlla se ci sono più immagini come input
# #
# # source: il percorso delle immagini da leggere
# # dest: il percorso dove verranno salvati i file
# # lang: il linguaggio in qui leggere l'immagine
# # prefix: il nome del file
# # -----------------------------------------------------------------------
# def multi_image(source, dest, lang, prefix):
#     if len(source) > 1:
#         for path in source:
#             check_img_type(path, dest, lang, prefix)
#     else:
#         check_img_type(source, dest, lang, prefix)

# # -----------------------------------------------------------------------
# # Controlla se il formato dell'immagine passata dal utente è accettato.
# #
# # path: il percorso della immagine da leggere
# # dest: il percorso dove verranno salvati i file
# # lang: il linguaggio in qui leggere l'immagine
# # prefix: il nome del file
# # -----------------------------------------------------------------------
# def check_img_type(source, dest, lang, prefix):
#     image_ext = os.path.splitext(source)[-1]
#     logging.debug(f"image ext: {image_ext}")
#     if image_ext.lower() == ".png" or image_ext.lower() == ".jpg":
#         create_output_file(source, dest, lang, prefix)
#     else:       
#         logging.info("Errore: Formato non accettato. Inserire immagini di tipo .png e/o .jpg")

# # --------------------------------------------------------------------------
# # Crea la cartella passata dall'utente se essa non esiste.
# # Dopo averla creata, o se esiste già, entra nella cartella di destinazione.
# #
# # dest: il percorso dove verranno salvati i file
# # --------------------------------------------------------------------------
# def create_directory(dest):
#     try:
#         os.mkdir(dest)
#     except OSError:
#         logging.info(f"La cartella {dest} esiste gia")
#     else:
#         logging.info(f"La cartella {dest} e' stata creata")

# # -----------------------------------------------------------
# # Crea il file e scrive nell'esso il contenuto dell'immagine.
# #
# # file_name: il nome del file da creare
# # text_to_write: il testo da inserire nel file 
# # -----------------------------------------------------------
# def write_file(file_name, text_to_write):
#     with open(file_name, 'a+') as outfile:
#         outfile.write(text_to_write)
#         logging.info(f"Il file {file_name} e' stato creato")

# # -----------------------------------------------------------
# # Crea il file e scrive nell'esso il contenuto dell'immagine.
# #
# # file_name: il nome del file da creare
# # text_to_write: il testo da inserire nel file 
# # -----------------------------------------------------------
# def write_list_of_text_in_file(file_name, list_of_text):
#     with open(file_name, 'a+') as outfile:
#         for text in list_of_text:
#             outfile.write(text)
#     logging.info(f"Il file {file_name} e' stato creato")

# # -----------------------------------------------------------
# # Se c'è un file con lo stesso nome dentro la cartella, crea il file aggiungendogli,
# # alla fine, un numero in base al numero degli file con lo stesso nome.
# # ex: scan.txt, scan_1.txt, scan_2.txt, ecc...
# #
# # file_name: il nome del file da creare
# # text_to_write: il testo da inserire nel file 
# # prefix: il nome del file
# # -----------------------------------------------------------

# def write_existing_file(file_name, text_to_write, prefix):
#     # if len(source) is 1:
#     existing_file_name = os.path.splitext(file_name)
#     name_id = existing_file_name[0]
#     id = name_id[-1]

#     # e se ci sono 2 file che si chiamano 492850.png ? ->  492850_<>.png
#     # 492851 -> 492850_1
#     if id.isdigit():
#         id = id + 1
#     else:
#         id = 1

#     logging.debug(f"id: {id}")
#     out_file_name = prefix + f"_{id}.txt"
#     logging.debug(f"out name: {out_file_name}")

#     write_file(out_file_name, text_to_write)
#     # else:
#     #     write_file(file_name, text_to_write)

# # -----------------------------------------------------------
# # Se c'è un file con lo stesso nome dentro la cartella, crea il file aggiungendogli,
# # alla fine, un numero in base al numero degli file con lo stesso nome.
# # ex: scan.txt, scan_1.txt, scan_2.txt, ecc...
# #
# # file_name: il nome del file da creare
# # text_to_write: il testo da inserire nel file 
# # prefix: il nome del file
# # -----------------------------------------------------------
# def write_list_of_text_in_existing_file(file_name, text_to_write, prefix):
#     # if len(source) is 1:
#     existing_file_name = os.path.splitext(file_name)
#     name_id = existing_file_name[0]
#     id = name_id[-1]

#     # e se ci sono 2 file che si chiamano 492850.png ? ->  492850_<>.png
#     # 492851 -> 492850_1
#     if id.isdigit():
#         id = id + 1
#     else:
#         id = 1

#     logging.debug(f"id: {id}")
#     out_file_name = prefix + f"_{id}.txt"
#     logging.debug(f"out name: {out_file_name}")

#     write_list_of_text_in_file(out_file_name, text_to_write)


# # ---------------------------------------------------------
# # Crea il file di output nella cartella specificata dall'utente,
# # nella ligua specificata dall'utente e con il nome specificato dall'utente.
# # 
# # source: il percorso dell'immagine da leggere
# # dest: il percorso dove verranno salvati i file
# # lang: il linguaggio in qui leggere l'immagine
# # prefix: il nome del file
# # ---------------------------------------------------------
# def create_output_file(source, dest, lang, prefix): 
#     create_directory(dest)
#     os.chdir(dest)
#     logging.debug(f"source to open: {source}")
#     logging.debug(f"img open source: {Image.open(source)}")
#     file_name = f"{prefix}.txt"
#     fileslist = os.listdir()
#     # text_to_write = pytesseract.image_to_string(cv2.imread(source), lang)

#     if len(source) > 1:
#         logging.debug() 
#         list_of_text = list()
#         for path in source:
#             try:
#                 text_to_write = pytesseract.image_to_string(Image.open(source), lang)
#                 list_of_text.append(text_to_write)
#             except FileNotFoundError as fnf_error:
#                 logging.error("Error: file {source} not found, {fnf_error} ")
        
#         if not fileslist:
#             write_list_of_text_in_file(file_name, list_of_text)
#         else:
#             if (f in file_name for f in fileslist):
#                 write_list_of_text_in_existing_file(file_name, text_to_write, prefix)
#                 logging.debug(f"writes existing file")
#             else:
#                 write_list_of_text_in_file(file_name, text_to_write)
#     else: 
#         if not fileslist:
#             write_file(file_name, text_to_write)
#         else:
#             # entra qua solo 1 volta
#             # if all(f in file_name for f in fileslist):
#             if (f in file_name for f in fileslist):
#                 write_existing_file(file_name, text_to_write, prefix)
#                 logging.debug(f"writes existing file")
#             else:
#                 write_file(file_name, text_to_write)
            
#     os.chdir("../")
