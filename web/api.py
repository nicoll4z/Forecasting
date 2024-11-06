from flask import Flask, request, jsonify
from flask_cors import CORS
import grpc
import sys
import os
sys.path.append(os.path.abspath(".."))
import previsao_pb2 as previsao_pb2
import previsao_pb2_grpc

app = Flask(__name__)
CORS(app)  # Ativa o CORS para todas as rotas

@app.route('/previsao5d')
def get_previsao5d():
    city_name = request.args.get("city") 
    if not city_name:
        return jsonify({"error": "Nome da cidade não fornecido"}), 400

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = previsao_pb2_grpc.PrevisaoServiceStub(channel)
        request_data = previsao_pb2.PrevisaoRequest(city_name=city_name)

        try:
            response = stub.GetPrevisao5d(request_data)
            forecasts = [
                {
                    "country": forecast.country,
                    "adArea": forecast.adArea,
                    "date": forecast.date,
                    "weather_text": forecast.weather_text,
                    "temperature": forecast.temperature,
                    "real_feel": forecast.real_feel,
                    "humidity": forecast.humidity,
                }
                for forecast in response.forecasts
            ]
            return jsonify({"forecasts": forecasts})

        except grpc.RpcError as e:
            print(f"Erro ao obter dados gRPC: {e.details()}")
            return jsonify({"error": f"Erro ao obter dados: {e.details()}"}), 500

@app.route('/previsao1d')
def get_previsao1d():
    city_name = request.args.get("city")
    if not city_name:
        return jsonify({"error": "Nome da cidade não fornecido"}), 400

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = previsao_pb2_grpc.PrevisaoServiceStub(channel)
        request_data = previsao_pb2.PrevisaoRequest(city_name=city_name)

        try:
            response = stub.GetPrevisao1d(request_data)
            forecasts = [
                {
                    "country": forecast.country,
                    "adArea": forecast.adArea,
                    "date": forecast.date,
                    "weather_text": forecast.weather_text,
                    "temperature": forecast.temperature,
                    "real_feel": forecast.real_feel,
                    "humidity": forecast.humidity,
                }
                for forecast in response.forecasts
            ]
            return jsonify({"forecasts": forecasts})

        except grpc.RpcError as e:
            print(f"Erro ao obter dados gRPC: {e.details()}")
            return jsonify({"error": f"Erro ao obter dados: {e.details()}"}), 500
        
@app.route('/previsao1h')
def get_previsao12h():
    city_name = request.args.get("city")
    if not city_name:
        return jsonify({"error": "Nome da cidade não fornecido"}), 400

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = previsao_pb2_grpc.PrevisaoServiceStub(channel)
        request_data = previsao_pb2.PrevisaoRequest(city_name=city_name)

        try:
            response = stub.GetPrevisao1h(request_data)
            forecasts = [
                {
                    "country": forecast.country,
                    "adArea": forecast.adArea,
                    "date": forecast.date,
                    "weather_text": forecast.weather_text,
                    "temperature": forecast.temperature,
                    "real_feel": forecast.real_feel,
                    "humidity": forecast.humidity,
                }
                for forecast in response.forecasts
            ]
            return jsonify({"forecasts": forecasts})

        except grpc.RpcError as e:
            print(f"Erro ao obter dados gRPC: {e.details()}")
            return jsonify({"error": f"Erro ao obter dados: {e.details()}"}), 500

if __name__ == '__main__':
    app.run(port=5000)
