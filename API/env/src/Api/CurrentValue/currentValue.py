from email import headerregistry
from urllib import response
from flask import Flask, request, jsonify,make_response
from flask_restful import Resource, Api
from datetime import datetime
from ...HistorianRequests.historian import *




class CurrentValues(Resource):
    def get(self):
      data = getCurrentValues()
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