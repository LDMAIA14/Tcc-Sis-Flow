from ..Connection.connection import *
from datetime import timedelta, datetime
import requests
class Metereologia:
    def __init__(self):        
        idmetereologia=0
        datahora=''
        temperatura=0
        umidade=0
        preciptacao=0.0
        velocidade_vento = 0.0

    def setData():
        response={}
        response = Metereologia.getActualWeather()
        queryField = 'datahora, temperatura, umidade, velocidade_vento'
        now = datetime.now()
        formatted_date = str(now.date()) +   " " +  str(now.hour) + ":00"

        queryValues = " '" + str(formatted_date) + "', " + str(response['Temperatura']) + ", " +  str(response['Umidade']) + ", " +  str(response['VelocidadeVento']) + " "

        res = insert(database='sis_flow', mytable='metereologia', fields=queryField,values=queryValues,type="1")
        return res[0]
    def getData( **kwargs):
        type = kwargs.get('type', 'all')
        datesBack = kwargs.get('datesback', 20)
        ind = 1
        listRet = []
        if type == 'all':
             listRet = selectArray(database="sis_flow",mytable="metereologia")
        if type == "array":
            while ind < (datesBack+1):
                dateQuery = datetime.now() - timedelta(days=ind*7)
                myQuery = "SELECT TOP(1) * FROM metereologia WHERE(datahora = '" + str(dateQuery.date()) + " " + str(dateQuery.hour) + ":00')"  
            
                arrRet = selectArray(database="sis_flow",mytable="metereologia", query=myQuery)
             
                listRet.append(arrRet.copy())
                ind =ind + 1
        if type == "last":
            myQuery = "SELECT TOP(1) * FROM metereologia ORDER BY idmetereologia DESC"  
        
            arrRet = selectArray(database="sis_flow",mytable="metereologia", query=myQuery)
            
            listRet = arrRet.copy()
            
        return listRet 
    
    def getActualWeather():
        serverRest = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/6731/current?token=75c489a72d4ea844508a20fee0241c3d'
        
        dictData = requests.get(serverRest)
        listData = {}
        if dictData.status_code == 200:
            listData = dictData.json()
        else:
            listData = {
                "status": 500, #//status da resposta
                "method": "GET", # //método da requisição
                "path": "/flow-sis/api/v1/weather" , #//caminho da requisição
                "code": dictData.text, #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.now().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
        }
       
        res = { "Temperatura": str(listData['data']['temperature']) , "Umidade": str(listData['data']['humidity']) , "VelocidadeVento": str(listData['data']['wind_velocity'])}

        return res

