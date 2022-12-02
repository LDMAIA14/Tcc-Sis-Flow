from urllib import response
from flask import Flask, request, jsonify,make_response
from flask_restful import Resource, Api
from datetime import datetime
from ...HistorianRequests.historian import *
from ...Connection.connection import *
from ...Connection.connection import *




class Login(Resource):
  def get(self):
    return 0 #select(database="sis_flow",mytable="usuarios")
  def post(self):
    
    res = select('sis_flow', 'usuarios', query = "SELECT * FROM usuarios WHERE(email = '" + request.json['user'] + "' and senha = '" + request.json['pwd'] + "')")
    try:
      myresult = res.get_data()
      myjson = myresult.decode('utf8').replace("'",'"')
      data = json.loads(myjson)
      if data[0]['email'] == request.json['user']:
        print('usuario logado')
        reponse = '{"response":"true", "name": "' + str(data[0]['nome']) + '", "permissao":"' + str(data[0]['permissao']) + '"}'
      else:
        print('usuario login negado')
        reponse = '{"response":"false", "name":""}'
    except: 
      print('usuario login negado')
      reponse = '{"response":"false", "name":"", "permissao":""}' 
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
