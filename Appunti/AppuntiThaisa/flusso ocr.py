
START
	inserire param
		!exists(src) -> error printHelp

		checkParam e default value

		#------ read source ------#
		# per ogni elemento della lista source bisogna controllare
		# - se è un file, una dir o un mask; 
		# - bisogna poi guardare se il tipo è valido (png o jpg);
		# - se il percorso esiste;
		# - se si puo accedere in lettura;

		# vedi poi appunti test se necessario -> come gestire mask

		if dir != empty: #vedere se gestisce anche i mask (*.*)
			# metodo-> return lista file contenuti nella dir
		else:
			print Error: cartella vuota

		# se vengono passati file nell'src vengono ciclati qui sotto direttamente
		# fileList è la lista di file da controllare/scannerizzare, se viene passata una dir è la lista dei file della cartella, se invece vengono passati 1 o + file in src fileList è quello.
		for fileList:
			is_valid -> controlla il tipo, se esiste e se si hanno i permessi di lettura, se entrambi i controlli passano return true (check img type; check_path)
			if true:
				add file to validList

		# no file validi -> interrompe ocr
		if validList == null:
			print Error: inserire percorso/i valido/i

		# messaggio file omessi
		if validList.length < fileList.length:
			print Info/Warning: uno o piu file sono stati omessi

	    # ritorna la lista valida di file 
	    return validList


	    #------ scan file ------#
	    # riceve validList

	    for img:
	    	try:
			    # ritorna ogni volta la str dell'img passata
			    txt = pytesseract.image_to_string(Image.open(img), lang) 
				txtList.append(txt)
			catch:
				print Error

		# lista con il contenuto di ogni img passata
		return txtList

	    #---- ev. print stats ----#
	    [...]


	    #---- write output ----#
	    # riceve txtList
	    #
	    # - dest:
	    # 	- permessi w (creare file scan e cartella dest) 
	    #
	    #
	    if dest.exists():
	    	dest.isWritable():
	    		# controllo dir o file
	    		if dest is dir: # se dest è una cartella. es: "./Documents/scan/"
	    			
	    			outName = prefix + ".txt"
	    			if outName.exists():
	    				outName = prefix + "_"+id+".txt"
	    				
	    				fore file in dirContent:
	    					####################

	    			else:
		    			if isWritable:
		    				create file dest/outName
	    				

	    		else: # se dest è un file. es: "./Documents/scan/cane.txt"
	    			# sovrascrive il file ---> ??? richiedere consenso a user ???
	    			check prefix # 
