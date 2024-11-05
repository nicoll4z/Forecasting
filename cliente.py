import grpc
import previsao_pb2 as previsao_pb2
import previsao_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = previsao_pb2_grpc.PrevisaoServiceStub(channel)
        city_name = input("Digite o nome da cidade: ")
        request = previsao_pb2.PrevisaoRequest(city_name=city_name)
        
        try:
            response = stub.GetPrevisao1h(request)
            print(f"Previsão do tempo para {city_name}:\n")
            for forecast in response.forecasts:
                print(f"Data: {forecast.date}")
                print(f"Condições: {forecast.weather_text}")
                print(f"Temperatura: {forecast.temperature}°C")
                print(f"Sensação Térmica: {forecast.real_feel}°C")
                print(f"Umidade: {forecast.humidity}%")
                print("-" * 30)

        except grpc.RpcError as e:
            print(f"Erro: {e.details()}")

if __name__ == '__main__':
    run()
