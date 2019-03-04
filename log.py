import logging,os
def get_logger():
    global logPath
    try:
         if not os.path.exists('./Logs'):
            os.makedirs('./Logs')
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S', filename='./Logs/Hgo.log',
                        filemode='w')
    return logging