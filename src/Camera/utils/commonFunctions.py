import numpy as np
import traceback

def saveNParray(filename = "", varArray = None) -> int:
    """
    Args:
        filename (str): should be "something.dat". Defaults to "".
        varArray (array): _description_. Defaults to None.

    Returns:
        rc (int): return code
    """
    try:
        with open(filename, "+wb") as fid: np.save(fid, varArray)
        return 1
    except:
        print(traceback.format_exc())
        return -1
    #end-try-except
#end-def

def readNParray(filename = "") -> int:
    """
    Args:
        filename (str): should be "something.dat". Defaults to "".
        varArray (array): _description_. Defaults to None.

    Returns:
        rc (int): return code
    """
    try:
        with open(filename, 'rb') as fid: variable = np.load(fid)
        return variable
    except:
        print(traceback.format_exc())
        return -1
    #end-try-except
#end-def