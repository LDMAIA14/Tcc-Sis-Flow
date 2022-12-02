from email import headerregistry
from urllib import response
from flask import Flask, request, jsonify,make_response
from flask_restful import Resource, Api
from datetime import datetime
from ...Classes.cl_resultados import *


class Results(Resource):
    def get(self):
        res = Resultados
        data = res.getLastResultados()
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.set_data(str(data))
        return  response
        
        #  request.json['idcidade']
    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response