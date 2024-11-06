import grpc
from concurrent import futures
import requests
import previsao_pb2 as previsao_pb2
import previsao_pb2_grpc
from datetime import datetime
from dateutil import parser


API_KEY = 'O5ZAvp8m27C3s2dJd1cpSO4pAUsPeeNL'
BASE_URL = 'http://dataservice.accuweather.com/'

class PrevisaoService(previsao_pb2_grpc.PrevisaoServiceServicer):
    def GetPrevisao5d(self, request, context):
        city_name = request.city_name
        
        # Primeiro, obter o local (location key) da cidade
        location_url = f"{BASE_URL}locations/v1/cities/search?apikey={API_KEY}&q={city_name}&language=pt-BR"
        location_response = requests.get(location_url)

        if location_response.status_code != 200:
            context.set_details("Erro ao obter a localização.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return previsao_pb2.PrevisaoResponse()

        location_data = location_response.json()
        if not location_data:
            context.set_details("Cidade não encontrada.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return previsao_pb2.PrevisaoResponse()
        

        location_key = location_data[0]['Key']
        country = location_data[0]['Country']['LocalizedName']
        adArea = location_data[0]['AdministrativeArea']['LocalizedName']
        
        forecast_url = f"{BASE_URL}forecasts/v1/daily/5day/{location_key}?apikey={API_KEY}&language=pt-BR&details=true&metric=true"
        forecast_response = requests.get(forecast_url)

        forecast_data = forecast_response.json()
        forecasts = []

        for day in forecast_data['DailyForecasts']:
            date_str = day['Date'] # Data no formato ISO (YYYY-MM-DDTHH:MM:SSZ)
            date_obj = parser.parse(date_str)
            date_frmtd = date_obj.strftime("%H:%M - %d/%m/%Y")
            weather_text = day['Day']['IconPhrase']
            temperature = day['Temperature']['Maximum']['Value']
            real_feel = day['RealFeelTemperature']['Maximum']['Value']  # Sensação térmica
            humidity = day['Day']['RainProbability']  # Umidade relativa
            
            temperature = str(temperature)[:2]
            real_feel= str(real_feel)[:2]

            forecasts.append(previsao_pb2.DailyForecast(
                country = country,
                adArea = adArea,
                date=date_frmtd,
                weather_text=weather_text,
                temperature=float(temperature),
                real_feel=float(real_feel),
                humidity=humidity
            ))

        return previsao_pb2.PrevisaoResponse(forecasts=forecasts)
    
    def GetPrevisao1d(self, request, context):
        city_name = request.city_name
        
        # Primeiro, obter o local (location key) da cidade
        location_url = f"{BASE_URL}locations/v1/cities/search?apikey={API_KEY}&q={city_name}&language=pt-BR"
        location_response = requests.get(location_url)

        if location_response.status_code != 200:
            context.set_details("Erro ao obter a localização.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return previsao_pb2.PrevisaoResponse()

        location_data = location_response.json()
        if not location_data:
            context.set_details("Cidade não encontrada.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return previsao_pb2.PrevisaoResponse()
        
        location_key = location_data[0]['Key']
        country = location_data[0]['Country']['LocalizedName']
        adArea = location_data[0]['AdministrativeArea']['LocalizedName']
      
        forecast_url = f"{BASE_URL}forecasts/v1/daily/1day/{location_key}?apikey={API_KEY}&language=pt-BR&details=true&metric=true"
        forecast_response = requests.get(forecast_url)
        
        if forecast_response.status_code != 200:
            context.set_details("Erro ao obter a previsão do tempo.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return previsao_pb2.PrevisaoResponse()

        forecast_data = forecast_response.json()
        forecasts = []

        for day in forecast_data['DailyForecasts']:
            date_str = day['Date'] # Data no formato ISO (YYYY-MM-DDTHH:MM:SSZ)
            date_obj = parser.parse(date_str)
            date_frmtd = date_obj.strftime("%H:%M - %d/%m/%Y")
            weather_text = day['Day']['IconPhrase']
            temperature = day['Temperature']['Maximum']['Value']
            real_feel = day['RealFeelTemperature']['Maximum']['Value']  # Sensação térmica
            humidity = day['Day']['RainProbability']  # Umidade relativa

            temperature = str(temperature)[:2]
            real_feel= str(real_feel)[:2]

            forecasts.append(previsao_pb2.DailyForecast(
                country=country,
                adArea=adArea,
                date=date_frmtd,
                weather_text=weather_text,
                temperature=float(temperature),
                real_feel=float(real_feel),
                humidity=humidity
            ))

        return previsao_pb2.PrevisaoResponse(forecasts=forecasts)
    
    def GetPrevisao1h(self, request, context):
        city_name = request.city_name
        
        # Primeiro, obter o local (location key) da cidade
        location_url = f"{BASE_URL}locations/v1/cities/search?apikey={API_KEY}&q={city_name}&language=pt-BR"
        location_response = requests.get(location_url)

        if location_response.status_code != 200:
            context.set_details("Erro ao obter a localização.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return previsao_pb2.PrevisaoResponse()

        location_data = location_response.json()
        if not location_data:
            context.set_details("Cidade não encontrada.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return previsao_pb2.PrevisaoResponse()
        
        location_key = location_data[0]['Key']
        country = location_data[0]['Country']['LocalizedName']
        adArea = location_data[0]['AdministrativeArea']['LocalizedName']
        
        forecast_url = f"{BASE_URL}forecasts/v1/hourly/1hour/{location_key}?apikey={API_KEY}&language=pt-BR&details=true&metric=true"
        forecast_response = requests.get(forecast_url)
        
        if forecast_response.status_code != 200:
            context.set_details("Erro ao obter a previsão do tempo.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return previsao_pb2.PrevisaoResponse()

        forecast_data = forecast_response.json()
        forecasts = []

        for hour in forecast_data:
            date_str = hour['DateTime'] # Data no formato ISO (YYYY-MM-DDTHH:MM:SSZ)
            date_obj = parser.parse(date_str)
            date_frmtd = date_obj.strftime("%H:%M - %d/%m/%Y")# Data no formato ISO (YYYY-MM-DDTHH:MM:SSZ)
            weather_text = hour['IconPhrase']
            temperature = hour['Temperature']['Value']
            real_feel = hour['RealFeelTemperature']['Value']  # Sensação térmica
            humidity = hour['RelativeHumidity']  # Usando um valor padrão se não existir

            temperature = str(temperature)[:2]
            real_feel= str(real_feel)[:2]

            forecasts.append(previsao_pb2.DailyForecast(
                country=country,
                adArea=adArea,
                date=date_frmtd,
                weather_text=weather_text,
                temperature=float(temperature),
                real_feel=float(real_feel),
                humidity=humidity
            ))

        return previsao_pb2.PrevisaoResponse(forecasts=forecasts)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))
    previsao_pb2_grpc.add_PrevisaoServiceServicer_to_server(PrevisaoService(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor de previsão do tempo rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
