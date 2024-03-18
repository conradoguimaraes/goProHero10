import os
import traceback
import shutil
import logging

from utils.config import readConfig

def setupLogger(configModuleName = "logger"):
    #Instantiate the logger
    try:
      config = readConfig(moduleName = configModuleName)
      #config = readConfig(moduleName=__name__)
      logSubfolder = config["logSubfolder"]
      logFilename = config["logFilename"]
      logFormat = config["logFormat"]
      
      logsFilePath = os.path.join(os.getcwd(), logSubfolder, logFilename)


      #If the logger path exists, delete it along with all childs
      if (os.path.isdir(logSubfolder) is True): shutil.rmtree(logSubfolder)

      #Create the logs folder & file
      os.mkdir(logSubfolder)
      with open(logsFilePath, "w") as fid: fid.write("LOGs File.\n")
          
      logger = logging.getLogger()

      logging.basicConfig(filename=logsFilePath,
                          format=logFormat,
                          level=logging.DEBUG)
      logging.info("Logger initialized.")
      return logger
    except:
      print(traceback.format_exc())
      return None
    #end-try-except
    


def displayLoggerContent(filePath = "") -> None:
  try:
    with open(filePath,'r',) as fid:
      print(fid.readlines())
  except FileNotFoundError:
      print("Logger filepath '", filePath, "' does not exist.")
  except:
      print(traceback.format_exc())
  
  return None