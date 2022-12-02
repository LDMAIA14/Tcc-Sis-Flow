from email import headerregistry
from urllib import response
from flask import Flask, request, jsonify,make_response
from flask_restful import Resource, Api
from datetime import datetime
from ...Classes.cl_resultados import *


class Dashboard(Resource):
    def post(self):
        data=[]
        try:
            res = Resultados
            month = str(request.json['month'])
            year = str(request.json['year'])
            

            typeLow = 0
            typeOk = 0
            typeHi = 0
            typeHiHi = 0
            filteredResults = res.getFilteredResultados(month=month,year=year)[0]
       
            for result in filteredResults:
                min = float(result['min_calculado'])
                max = float(result['max_calculado'])
                actualValue = float(result['valor_atual'])
                limit = max * 1.1
                if actualValue < min:
                    typeLow = typeLow + 1
                if actualValue >= min and actualValue <= max:
                    typeOk = typeOk + 1
                if actualValue > max and actualValue <= limit:
                    typeHi = typeHi + 1
                if actualValue > limit:
                    typeHiHi = typeHiHi + 1
            
            data.append({
                
                "low": typeLow,
                "ok": typeOk,
                "hi": typeHi,
                "hihi": typeHiHi,
            })

           
        except Exception as e:
            desc=[]
            for d in e.args:
                desc.append(d)
            data.append({
                "status": 500, 
                "method": "POST", 
                "action":"SELECT",
                "path": "/flow-sis/api/v1/dashboard" ,
                "code": str(desc),
                "title": "Erro", 
                "message": "Um erro inesperado ocorreu. Por favor, entre em contato com o suporte.", 
                "ts": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
            })
            
        finally:
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