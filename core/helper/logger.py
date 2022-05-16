log = None

def setupLogging(file):
    global log
    log = open(file, "a")

def log(* msg, **param):
    """
    log given text to the log file
    """
    print(*msg, **param, file=log)
    
def endLogging():
    global log
    if log == None:
        raise ValueError("Log is not open!")
    log.close()
    log = None
    
def isLogOpen():
    return log != None