from cmath import e
from flask import Flask, request, jsonify,make_response
from flask_restful import Resource, Api
from ...Connection.connection import *

class ZP(Resource):
    def get(self):
        try:
            data = selectArray(database="sis_flow",mytable="zonas_pressao")
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.set_data(json.dumps(data))
            return  response
        except:
            return []
    def post(self):
        mytable = 'zonas_pressao'
        try:
            myValues="'" + str(request.json['sigla']) + "','" + str(request.json['descricao']) + "','" + str(request.json['tag_ft']) + "','" + str(request.json['tag_pt']) + "'" 
            myquery = 'INSERT INTO ' + str(mytable) + '(sigla,descricao,tag_ft,tag_pt) VALUES(' + myValues + ')' 
            
            reponse = insert('sis_flow',mytable,query=myquery,type=1)

        except: 
            reponse = {
                "status": 500, #//status da resposta
                "method": "POST", # //método da requisição
                "path": "/flow-sis/api/v1/"+ mytable , #//caminho da requisição
                "code": 'Erro Tentativa de Inserir Novo Registro', #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
        }
        finally:
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.set_data(str(reponse))
            return  response
    def delete(self):
        mytable = 'zonas_pressao'
        try:
            sigla = request.json['sigla']
            id = request.json['id']
            if sigla!='' and id!='':
                q = "DELETE FROM resultados WHERE(zona_pressao_idzonapressao = '" + str(id) + "' )"
                reponse = delete(database='sis_flow',mytable='resultados',query=q)
                q = "DELETE FROM zonas_pressao WHERE(sigla = '" + str(sigla) + "' )"
                reponse = delete(database='sis_flow',mytable=mytable,query=q)
            else:
                reponse={"status":500, "description":"error on deleting pressure zone " + str(sigla)}
            
        except: 
            reponse = {
                "status": 500, #//status da resposta
                "method": "POST", # //método da requisição
                "path": "/flow-sis/api/v1/"+ mytable , #//caminho da requisição
                "code": 'Erro Tentativa de Inserir Novo Registro', #//GUID para rastreio da stack de erro nos logs
                "title": "Erro", #//opcional: mensagem simplificada, indica-se tamanho reduzido (até 20 caracteres)
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", #//mensagem detalhada
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
        }
        finally:
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.set_data(str(reponse))
            return  response
    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response