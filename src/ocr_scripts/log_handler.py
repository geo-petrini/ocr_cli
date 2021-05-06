# ------------------------
# Modifica il logger normale aggiungendo una formattazione e degli handler.
# Questo logger scriverà i messaggi di debug in CLI e nel file /log/app_debug.log, i messaggi di info saranno scritti in /log/app.log.
#  
# original author: Geo Petrini
# modified by: Thaisa De Torre
# version: 25.02.2021
# last modified: 25.02.2021
# ------------------------

import logging, logging.handlers

def get_configure_logger():
    # vado a modificare direttamente il root di logger
    logger = logging.getLogger('')
    if (len(logger.handlers) == 0):
        # This logger has no handlers, so we can assume it hasn't yet been configured
        # Create RotatingFileHandler
        import os
        os.mkdir("./log")

        formatter = "%(asctime)s %(levelname)s %(process)s %(thread)s %(filename)s %(funcName)s():%(lineno)d %(message)s"
        handler = logging.handlers.RotatingFileHandler(os.path.join('.','log/app.log'), maxBytes = 1024*1024*10, backupCount = 6)
        handler.setFormatter(logging.Formatter(formatter))
        handler.setLevel(logging.INFO)

        handler_d = logging.handlers.RotatingFileHandler(os.path.join('.','log/app_debug.log'), maxBytes = 1024*1024*10, backupCount = 2)
        handler_d.setFormatter(logging.Formatter(formatter))
        handler_d.setLevel(logging.DEBUG)        
        
        # formatter = "%(asctime)s %(levelname)s: %(lineno)d  %(message)s"
        formatter = "%(levelname)s: %(message)s"
        handler_cli = logging.StreamHandler()
        handler_cli.setFormatter(logging.Formatter(formatter))
        handler_cli.setLevel(logging.INFO)

        logger.addHandler(handler)
        logger.addHandler(handler_d)
        logger.addHandler(handler_cli)
        logger.setLevel(logging.INFO)

        # Test entry:
        #logger.debug(name + ' logger created')
    else:
        # Test entry:
        #logger.debug(name + ' already exists')
        pass
    return logger
