from ...HistorianRequests.historian import *
from ...Classes.cl_zonapressao import ZonaPressao
from ...Classes.cl_metereologia import *
from ...Connection.connection import *

def UpdateResult():
    try:
        zp = ZonaPressao
        objzps = zp.getZP()

    
        tagList = []
        for item in objzps:
            tagList.append([item['tag_ft'],item['idzonapressao']])
            

        for obj in tagList:
            
            
            actualFlow = float(getCurrentValues(tag=obj[0])[0]['Value'])

            myquery = 'SELECT TOP(1) * FROM resultados WHERE(zona_pressao_idzonapressao = ' + str(obj[1]) + ') ORDER BY idresultado DESC'
                
            jsonret = selectArray(database="sis_flow",mytable="resultados", query=myquery)[0]

            percent = format((float(actualFlow) / float(jsonret['valor_calculado']) * 100), '.2f')

            strcmd = 'UPDATE resultados SET valor_atual = ' + str(actualFlow) + ', percentage_value = ' + str(percent) + ' '
            strcmd = strcmd + ' WHERE(idresultado = (select TOP(1) idresultado from resultados where(zona_pressao_idzonapressao = ' + str(obj[1]) + ') order by idresultado desc))'
        
            res = update('sis_flow','resultados',strcmd)

        return 0
    except Exception as e:
        print(e)
        return -1


111