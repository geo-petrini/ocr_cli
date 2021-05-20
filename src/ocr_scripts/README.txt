
Requisiti:

Avere installato python (versione minima 3.6.0) 

-----------------------------------------------------------------------------------
Struttura del programma:

OCR
   |--- ocr.py
   |--- reader.py
   |--- stats.py
   |--- log_handler.py
   |--- installModules.bat
   |--- requirements.txt
   |--- Tesseract-OCR
   |--- README.txt

ocr.py è il file nel quale vengono gestite tutte le operazioni principali: riceve gli argomenti, scannerizza le immagini passate e mette il testo ricavato nel file di testo di output. 

log_handler è il file in cui vengono definiti e gestiti i log per i file (app_debug.log per il livello debug; app.log per il livello info) e il log su cli per l’utente.

I files reader.py e stats.py sono i moduli che contengono i metodi per la scannerizzazione dell’immagine, la gestione dell’output e per le statistiche dell’esecuzione.

Lo script installModules.bat serve ad installare con un click le dipendenze (contenute nel file requirements.txt) che servono all'OCR per funzionare.

Il file di testo README.txt contiene le informazioni principali sull’utilizzo del programma e sulla risoluzione minima delle immagini da scannerizzare.

Dopo la prima esecuzione verranno create le cartelle log e scans (scans no se l’utente specifica una cartella differente) perché sono le cartelle default per salvarci rispettivamente i file di log e i file di testo quando non viene specificato il percorso dell'output.

-----------------------------------------------------------------------------------
Come far partire il programma:

Bisogna andare nel percorso dell'ocr.py e farlo partire con il cmd.
Se mancano le dipendenze basta eseguire "installingModules.bat" che li installerà automaticamente.

-----------------------------------------------------------------------------------
Regole da rispettare per ottenere risultati migliori 

•	Usare immagini con testo scuro su sfondo chiaro
•	Tesseract funziona meglio su immagini che hanno un DPI di almeno 300 dpi
•	I bordi delle immagini scannerizzate possono essere rilevati come caratteri extra
•	È raccomandata una dimensione dei caratteri tra 25 e 40 pixel
•	Le parole con le lettere appiccicate non vengono sempre riconosciute




