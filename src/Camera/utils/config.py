import traceback
import yaml

def readConfig(filename = "config.yml", moduleName = ""):
    """
    [INPUTs]: filename {STR}, moduleName = ""
    [OUTPUTs]: moduleContent {DICT}
    
    This function reads the 'config.yml' file that as the structure:

    
    moduleName-1:
        parameter1: value1
        parameter2: value2
    ---
    moduleName-2:
        parameter1: value1
    ---
    moduleName-3:
        parameter1: value1
        parameter2: value2
        parameter3: value3

    
    If we desire the 'moduleName-1' it returns the dictionary:
    moduleContent = readConfig(filename = "config.yml", moduleName = __name__)
    which has content similar to
    moduleContent = {"parameter1": value1, "parameter2": value2, "parameter3": value3}

    The function that calls this, can get the parameter as:

    myVarA = moduleContent["parameter1"] #is equal to 'value1'
    myVarB = moduleContent["parameter2"] #is equal to 'value2'


    """
    print("Running config.yml Parser")
    rc = -1
    try:
        modulesList = []
        with open(filename, 'r') as fid:
            modules = yaml.safe_load_all(fid)
            #We add the modules to a List since they are currently under a generator object
            for module in modules:
                modulesList.append(module)
        #end-with
    except:
        print(traceback.format_exc())
        return None
    #end-try-except
    
    #---------------------------------------------------------------------------------------

    #Find the desired module within the config file
    for module in modulesList:
        try:
            moduleContent = module[moduleName]
            rc = 1
            break
        except:
            pass
        #end-try-except
    #end-for

    #print("Module Content: \n ", moduleContent)
    
    #---------------------------------------------------------------------------------------

    if (rc == -1):
        print(f"Error extracting module config. Check if {moduleName} exists.")
        return None
    else:
        #moduleContent = module[moduleName]
        return moduleContent
    #end-if-else
#end-def