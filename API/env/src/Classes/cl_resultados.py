from ..Connection.connection import *
from ..Classes.cl_zonapressao import *

class Resultados:
    def __init__(self):        
        idresultado=0
        datahora=''
        valor_atual=''
        pressao=''
        valor_calculado=0
        min_calculado=0
        max_calculado=0
        percentage_value=0
        desvio_padrao=0
        r2=0
        mae=0
        media=0
        
    def setResultado():
        return 0
    def getLastResultados():
        try:
            zp = ZonaPressao
            objzps = zp.getZP()
            tagList=[]
            ret = []

            for item in objzps:
                tagList.append([item['idzonapressao'],item['sigla'], item['tag_ft'],item['descricao']])
            for zp in tagList:
                try:
                    myquery = 'SELECT TOP(1) * FROM resultados WHERE(zona_pressao_idzonapressao = ' + str(zp[0]) + ') ORDER BY idresultado DESC'
                    
                    jsonret = selectArray(database="sis_flow",mytable="resultados", query=myquery)[0]
                    nKey = {'sigla': zp[1] }
                    jsonret.update(nKey) 
                    nKey = {'tag_ft': zp[2] }
                    jsonret.update(nKey) 
                    nKey = {'descricao': zp[3] }
                    jsonret.update(nKey)
                    ret.append(json.loads(json.dumps(jsonret)))
                except Exception as e:
                    ex = e
            return ret
        except:
            return []
    def getFilteredResultados(month, year):
        ret=[]
        try:
            myquery = 'SELECT * FROM resultados WHERE ( YEAR(datahora) = ' + year + ' AND MONTH(datahora) = ' + month + ')'
            jsonret = selectArray(database="sis_flow",mytable="resultados", query=myquery)
            ret.append(json.loads(json.dumps(jsonret)))
        except Exception as e:
            ret={
                "erro":"houve um erro na aquisicao dos dados",
                "desc": e.args
            }
        finally:
            return ret