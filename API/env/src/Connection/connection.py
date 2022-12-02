from unicodedata import name
import pypyodbc
from flask import jsonify
from datetime import datetime
import json
import unidecode  



def myconnection(database):
    server = "localhost"
    user = "your-user"
    pwd = "yourpwd"
    return pypyodbc.connect("DRIVER={SQL Server};Server=127.0.0.1\WINCCPLUSMIG2014;Uid="+ user +";Pwd="+pwd+";Database="+database+";")
def select(database,mytable, **kwargs):
        query = kwargs.get('query', None)
        if query == None:
            sqlcmd = 'SELECT * FROM ' + mytable
        else:
            sqlcmd = query
        theData=[]
        mydict={}
        ret=[]
        fields = []
        try:
            connect = myconnection(database)
            cur = connect.cursor()
            for row in cur.columns(table=mytable):
                mydict.update({""+row[3]+"":""})
                fields.append(row[3])
            for inf in cur.execute(sqlcmd):
                theData.append(inf)    
            for everyrow in theData:
    
                for index, col in  enumerate(everyrow):
                    mystr = str(col)
                    mydict[fields[index]] = unidecode.unidecode(mystr)
        
                ret.append(mydict.copy())
            cur.close()
            connect.close()
        except Exception as e:
            desc=[]
            for d in e.args:
                desc=d
            retf = {
                "status": 500, #//status da resposta
                "method": "GET", # //método da requisição
                "action":"SELECT",
                "path": "/flow-sis/api/v1/"+ mytable , #//caminho da requisição
                "code": desc, #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
            }
            return retf
        return  jsonify(ret)

def selectArray(database,mytable, **kwargs):
    query = kwargs.get('query', None)
    if query == None:
        sqlcmd = 'SELECT * FROM ' + mytable
    else:
        sqlcmd = query
    theData=[]
    mydict={}
    ret=[]
    fields = []
    try:
        connect = myconnection(database)
        cur = connect.cursor()
        for row in cur.columns(table=mytable):
            mydict.update({""+row[3]+"":""})
            fields.append(row[3])
        for inf in cur.execute(sqlcmd):
            theData.append(inf)    
        for everyrow in theData:

            for index, col in  enumerate(everyrow):
                mystr = str(col)
                mydict[fields[index]] = unidecode.unidecode(mystr)
    
            ret.append(mydict.copy())
        cur.close()
        connect.close()
    except Exception as e:
        retf = [-1]
        return retf
    return  ret
def insert( database,mytable,fields="",values="",**kwargs):
        type = kwargs.get('type', None)
        query = kwargs.get('query', None)
        if(query == None):
            sqlcmd = 'INSERT INTO ' + mytable + '(' + fields + ')' + ' VALUES (' + values + ')'
        else:
            sqlcmd=query

        try:
            connect = myconnection(database)
            cur = connect.cursor()
            cur.execute(sqlcmd)
            cur.commit()
            cur.close()
            connect.close()
            idfield = __getId(mytable)
            if idfield != '':
                myQuery = "SELECT TOP(1) * FROM " + str(mytable)   + 'ORDER BY ' + str(idfield) + ' DESC' 

                ret = selectArray(database,mytable,query=myQuery)
            else:
                ret = {"msg":"inpossible get last inserted data due error on define the id field"}

        except Exception as e:
            
            desc=[]
            for d in e.args:
                desc=d
            retf = {
                "status": 500, #//status da resposta
                "action": "INSERT", # //método da requisição
                "path": "/flow-sis/api/v1/"+ mytable , #//caminho da requisição
                "code": desc, #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
            }
            return retf
        if type == None:
            return  jsonify(ret)
        else:
            return ret
def update( database,mytable,query):
        
        sqlcmd = query
        try:
            connect = myconnection(database)
            cur = connect.cursor()
            cur.execute(sqlcmd)
            cur.commit()
            cur.close()
            connect.close()
            myQuery = "SELECT TOP(1) * FROM " + str(mytable) 
            
            ret = selectArray(database,mytable,query=myQuery)


        except Exception as e:
            
            desc=[]
            for d in e.args:
                desc=d
            retf = {
                "status": 500, #//status da resposta
                "action":"UPDATE",
                "query":sqlcmd,
                "path": "/flow-sis/api/v1/"+ mytable , #//caminho da requisição
                "code": desc, #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
            }
            return retf
        if type == None:
            return  jsonify(ret)
        else:
            return ret
def delete( database,mytable,query):
        
        sqlcmd = query
        try:
            connect = myconnection(database)
            cur = connect.cursor()
            cur.execute(sqlcmd)
            cur.commit()
            cur.close()
            connect.close()
            
            ret={"status": 200, #//status da resposta
                "method": "DELETE",
                }
        

        except Exception as e:
            
            desc=[]
            for d in e.args:
                desc=d
            retf = {
                "status": 500, #//status da resposta
                "action":"DELETE",
                "query":sqlcmd,
                "path": "/flow-sis/api/v1/"+ mytable , #//caminho da requisição
                "code": desc, #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
            }
            return retf
        if type == None:
            return  jsonify(ret)
        else:
            return ret

def __getId(table=''):
    dictTable = {'zonas_pressao':'idzonapressao','metereologia':'idmetereologia','usuarios':'idusuarios','resultados':'idresultado'}
    for item in dictTable:
        if(item == table):
            return dictTable[item]
    return ''