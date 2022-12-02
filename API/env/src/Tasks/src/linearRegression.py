import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from ...HistorianRequests.historian import *
from ...Classes.cl_zonapressao import ZonaPressao
from ...Classes.cl_metereologia import *
from ...Connection.connection import insert

def CalcLinearRegressions():
    try:
        backWeeks = 40
        zp = ZonaPressao
        objzps = zp.getZP()
        met = Metereologia
        listTemperature = []
        listHumidity = []
        metData = met.getData(type='array', datesback=backWeeks)
        acttualMetData = met.setData()
        metLastData = met.getData(type='last')
        for result in metData:
            try:
                temp = result[0]['temperatura']
                humidity = result[0]['umidade']
                listTemperature.append(temp)    
                listHumidity.append(humidity)
            except:
                listTemperature.append(0)    
                listHumidity.append(0)
        arrTemperatura = np.array(listTemperature)
        arrHumidade = np.array(listHumidity)
        tagList = []
        listFlowValue = []
        listPressureValue = []
        for item in objzps:
            tagList.append([item['tag_ft'],item['tag_pt'],item['idzonapressao']])
            #ptTagList.append(item['tag_pt'])

        for obj in tagList:
            listFlowData = []
            listPressureData = []
            
            listFlowData = getInterpolatedValuesDataFrame(backWeeks,obj[0])
            listPressureData = getInterpolatedValuesDataFrame(backWeeks,obj[1])
            listFlowValue=[]
            listPressureValue=[]
            for item in listFlowData:
                listFlowValue.append(format(float(item['Value']),'.2f'))
            for item in listPressureData:
                listPressureValue.append(format(float(item['Value']),'.2f'))
            arrFlow = np.array(listFlowValue)
            arrPressure = np.array(listPressureValue)
            dfData = pd.DataFrame()
            dfData[obj[0]] = arrFlow
            dfData[obj[1]] = arrPressure
            dfData['Temperatura'] = arrTemperatura
            dfData['Umidade'] = arrHumidade
        
            
            y = dfData[obj[0]]
            X = dfData.drop(obj[0],axis=1)

            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

            myModel = LinearRegression()
            myModel.fit(X_train,y_train)

            
            actualPressure = float(getCurrentValues(tag=obj[1])[0]['Value'])
            actualFlow = float(getCurrentValues(tag=obj[0])[0]['Value'])
            resultado = myModel.intercept_ + (actualPressure * myModel.coef_[0]) + (float(metLastData[0]['temperatura']) *  myModel.coef_[1]) + (float(metLastData[0]['umidade']) *  myModel.coef_[2])
            y_pred = myModel.predict(X_test)
            convertedArr = arrFlow.astype(np.float)
            mean = format(np.mean(convertedArr),'.2f')
            stdDeviation = format(np.std(convertedArr,axis = 0),'.2f')
            maeCalculated = format(mean_absolute_error(y_test, y_pred),'.2f')
            r2Calculated = format(r2_score(y_test, y_pred),'.2f')
            minCalculated= format(float(resultado) - float(maeCalculated),'.2f')
            maxCalculated= format(float(resultado) + float(maeCalculated),'.2f')
            percent = format((float(actualFlow) / float(resultado) * 100), '.2f')


            print(dfData)
            print ( X_train)
            print( X_test)
            print(y_train)
            print(y_test)
            print(obj[0])
            print(myModel.score(X,y))
            print(myModel.intercept_)
            print(myModel.coef_)
            print(actualPressure)
            print(acttualMetData)
            print(metLastData)
            print(metLastData[0]['temperatura'] + ' graus celcius')
            print('Intercepto: ' + str(myModel.intercept_)  + ' ActualPressure:  ' + str(actualPressure) + 'coef: ' + str(myModel.coef_[0]) + ' +   temp: ' + str(metLastData[0]['temperatura']) + ' Coef2: ' + str(myModel.coef_[1]) + ' umidade: ' + str(metLastData[0]['umidade']) + ' Coef 3: ' + str(myModel.coef_[2]))
            
            print('PREDIÇÃO PARA PRESSÃO = ' + str(actualPressure) + " RESULTADO ESPERADO = " + str(resultado) + " l/s")        
            print('VAZÃO ATUAL = ' + str(actualFlow))
            
            print('MAE: %.2f' % mean_absolute_error(y_test, y_pred))
            print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
            print('R2 Score: %.2f' % r2_score(y_test, y_pred))
            print(metLastData[0])
            print(metLastData[0]['idmetereologia'])
            


            queryField = 'valor_atual,pressao, valor_calculado,  min_calculado,  max_calculado,  desvio_padrao,  r2,' 
            queryField = queryField + 'mae , media, percentage_value,'
            queryField =queryField + ' metereologia_idmetereologia,zona_pressao_idzonapressao'
            queryValues = str(format(actualFlow,'.2f')) + ',' + str(format(actualPressure,'.2f')) +  ',' + str(format(resultado,'.2f')) + ',' + str(minCalculated) + ','
            queryValues = queryValues + str(maxCalculated) + ',' + str(stdDeviation) + ',' + str(r2Calculated) + ','
            queryValues = queryValues + str(maeCalculated) + ',' + str(mean) + ',' + str(percent) + ',' + str(metLastData[0]['idmetereologia']) + ',' + obj[2]
            
            # print('Query Fields : ' + queryField)
            # print('Query Values : ' + queryValues)
        
            res = insert(database='sis_flow', mytable='resultados', fields=queryField,values=queryValues,type="1")
    except Exception as e:
        print(e)

    return 0



