

def convertStringToDataArray(stringData):
    retVal = stringData.replace("-","").replace("\"","").replace("Tweet: ","").split('\n')
    retVal = [item for item in retVal if item != ""]
    return retVal