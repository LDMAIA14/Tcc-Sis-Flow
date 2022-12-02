from ..Connection.connection import *


class ZonaPressao:
    def __init__(self):        
        idzonapressao=0
        sigla=''
        descricao=''
        tag_ft=''
        id_usuario=0
    def incluirZP():
        return 0
    def getZP():
        jsonRet =  selectArray(database="sis_flow",mytable="zonas_pressao")
        return jsonRet
