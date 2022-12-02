from statistics import linear_regression
from src.Tasks.main import *
from flask import Flask
from flask_restful import  Api
from src.Api.CurrentValue.currentValue import *
from src.Api.Login.login import *
from src.Api.Weather.weather import *
from src.Api.ZonaPressao.zonapressao import *
from src.Api.Resultados.resultados import *
from src.Api.Dashboard.dashboard import *
from src.Tasks.src.linearRegression import CalcLinearRegressions


import threading



def create_app():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 20
    api = Api(app)

        
    api.add_resource(CurrentValues, '/sis-flow/api/v1/currentvalues') 
    api.add_resource(Login, '/sis-flow/api/v1/login') 
    api.add_resource(ZP, '/sis-flow/api/v1/zonapressao') 
    api.add_resource(Results, '/sis-flow/api/v1/resultados') 
    api.add_resource(Dashboard, '/sis-flow/api/v1/dashboard')

  


    def startTasks():
        global calcThread
        calcThread = threading.Thread(target=mainFuntion)
        calcThread.start()
        
    startTasks()
    

    return app

app = create_app()      

app.run(port=8080, host='0.0.0.0', debug=False)