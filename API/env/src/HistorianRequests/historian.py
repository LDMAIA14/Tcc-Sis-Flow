from datetime import timedelta, datetime
import json
import requests
import numpy as np
from ..Classes.cl_zonapressao import *



def getCurrentValues(tag='all'):
    ## Servidor Historian/RestAPI
    serverRest = 'https://historianserver:4040'
    currentValueEndPoint = '/histgateway/currentvalue?listTags='
   
    tagList = []
    if tag == 'all':
        zp = ZonaPressao
        objzps = zp.getZP()
        for item in objzps:
            tagList.append(item['tag_ft'])
    else:
        tagList.append(tag)
    listReturn=[]
    index = 0
    for tagName in tagList:
    
        
       
        strServerGet = serverRest + currentValueEndPoint + tagName 

        dictData = {}
        
        dictData = requests.get(strServerGet)
        if dictData.status_code == 200:
            listData = dictData.json()
            
            listReturn.append(json.loads('{"TagName": "' + listData[0]['TagName'] 
                + '", "Value":"' + listData[0]['Samples'][0]['Value']  
                    + '", "TimeStamp":"' + listData[0]['Samples'][0]['TimeStamp']
                        + '"}'))
        else:
            listReturn.append('Houve um erro no retorno da tag: ' + str(tagName))
        
        index=index+1
    return listReturn


def getInterpolatedValues():
    ## Servidor Historian/RestAPI
    serverRest = 'https://historianserver:4040'
    interpolatedEndPoint = '/histgateway/interpolated?1tagname='
    currentValueEndPoint = '/histgateway/currentvalue?listTags='
    #
    ## Datas pesquisa 
    DataIni = '01/08/2018 00:00:00'
    DataOut = '31/08/2018 23:59:59'
    
    datesReturnIndex=1
    
    zp = ZonaPressao
    objzps = zp.getZP()

    tagList = []
    for item in objzps:
        tagList.append(item['tag_ft'])
    itemCount = len(tagList)
    listReturn=[]
    print('Quantidade de Tags = ' + str(itemCount))
    for tagName in tagList:
        DataIni = datetime.today() - timedelta(days=datesReturnIndex*7,hours=-3,minutes=30)
        DataOut = datetime.today() - timedelta(days=datesReturnIndex*7,hours=-3,minutes=-30)
        
        strServerGet = serverRest + interpolatedEndPoint + tagName + '&2start=' +  str(DataIni.date()) + 'T' + str(DataIni.hour) + '%3A' + str(DataIni.minute) + '%3A00Z&3end=' + str(DataOut.date()) + 'T' + str(DataOut.hour) + '%3A' + str(DataOut.minute) + '%3A00Z&4count=1&5time=60000'
        #strServerGet = serverRest + currentValueEndPoint + tagName 

        dictData = {}
        
        dictData = requests.get(strServerGet)
        if dictData.status_code == 200:
            listData = dictData.json()
            print(listData)
            listReturn.append(json.loads('{"TagName": "' + listData['Data'][0]['TagName'] 
                + '", "Value":"' + listData['Data'][0]['Samples'][0]['Value']  
                    + '", "TimeStamp":"' + listData['Data'][0]['Samples'][0]['TimeStamp'] + '"}'))
        else:
            listReturn.append('Houve um erro no retorno da tag: ' + str(tagName))
    return listReturn



def getInterpolatedValuesDataFrame(datesToReturn=1, myTagName=''):
    ## Servidor Historian/RestAPI
    serverRest = 'https://historianserver:4040'
    interpolatedEndPoint = '/histgateway/interpolated?1tagname='
    currentValueEndPoint = '/histgateway/currentvalue?listTags='
    #
    ## Datas pesquisa 
    DataIni = '01/08/2018 00:00:00'
    DataOut = '31/08/2018 23:59:59'
    
    datesReturnIndex=1
    
    

    tagList = []
    if myTagName != '':
        tagList.append(myTagName)
    else:
        zp = ZonaPressao
        objzps = zp.getZP().get_json()
        for item in objzps:
           tagList.append(item['tag_ft'])

    listReturn=[]
    for tagName in tagList:
        datesReturnIndex=1
        while datesReturnIndex < (datesToReturn+1):
            DataIni = datetime.today() - timedelta(days=datesReturnIndex*7,hours=-3,minutes=30)
            DataOut = datetime.today() - timedelta(days=datesReturnIndex*7,hours=-3,minutes=-30)
            
            strServerGet = serverRest + interpolatedEndPoint + tagName + '&2start=' +  str(DataIni.date()) + 'T' + str(DataIni.hour) + '%3A' + str(DataIni.minute) + '%3A00Z&3end=' + str(DataOut.date()) + 'T' + str(DataOut.hour) + '%3A' + str(DataOut.minute) + '%3A00Z&4count=1&5time=60000'
            #print(strServerGet)
            #strServerGet = serverRest + currentValueEndPoint + tagName 

            dictData = {}
            
            dictData = requests.get(strServerGet)
            if dictData.status_code == 200:
                listData = dictData.json()
                listReturn.append(json.loads('{"TagName": "' + listData['Data'][0]['TagName'] 
                    + '", "Value":"' + listData['Data'][0]['Samples'][0]['Value']  
                        + '", "TimeStamp":"' + listData['Data'][0]['Samples'][0]['TimeStamp'] + '"}'))
            else:
                listReturn.append('Houve um erro no retorno da tag: ' + str(tagName))
            datesReturnIndex=datesReturnIndex+1
    return listReturn