import datetime
import requests
import numpy as np
from flask import Flask, request, jsonify,make_response
from flask_restful import Resource, Api


class Weather(Resource):
    def get(self):

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
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') #//timestamp da resposta
            }
        return listData
    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response