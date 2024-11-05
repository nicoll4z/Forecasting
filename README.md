# Projeto de Previsão Meteorológica Distribuído

Este projeto é uma aplicação distribuída para consultar previsões meteorológicas para uma cidade específica, utilizando gRPC para comunicação entre cliente e servidor e Flask para disponibilizar uma API web. A aplicação se conecta à API AccuWeather para obter os dados de previsão.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o cliente, servidor e API.
- **gRPC**: Comunicação entre cliente e servidor para chamadas de método remoto.
- **Flask**: Framework web para disponibilizar a API REST.
- **Protocol Buffers**: Para definir a interface gRPC.
- **HTML/CSS**: Interface básica de consulta no navegador.

## Estrutura do Projeto

- `cliente.py`: Cliente que solicita previsões ao servidor gRPC.
- `servidor.py`: Servidor gRPC que processa as requisições e consulta a API AccuWeather.
- `previsao.proto`: Define o serviço gRPC e as mensagens de requisição e resposta.
- `web/api.py`: API web construída com Flask para fornecer uma interface HTTP.
- `index.html` e `styles.css`: Interface de usuário básica para consultar a previsão.
- `requirements.txt`: Lista de dependências do projeto.

## Pré-requisitos

- **Python 3.7+**
- **Bibliotecas do projeto**: Listadas em `requirements.txt`.

## Instalação e Configuração

1. Clone o repositório:
    ```bash
    git clone <https://github.com/nicoll4z/Forecasting>
    cd Forecasting
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. (Opcional) Gere o código gRPC a partir do arquivo `.proto`:
    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. previsao.proto
    ```

4. Iniciar o Servidor gRPC: Em um terminal, execute:
    ```bash
    python servidor.py
    ```

5. Iniciar a API Web: Em outro terminal, execute:
    ```bash
    python web/api.py
    ```

6. Executar o Cliente gRPC: Em um terceiro terminal, execute:
    ```bash
    python cliente.py
    ```

Agora, você pode usar a interface web para consultar a previsão ou utilizar o cliente gRPC diretamente.

## Endpoints da API Web

A API web é acessível através do seguinte endpoint:

- **GET** `/previsao?cidade=<NOME_DA_CIDADE>`: Retorna a previsão meteorológica em formato JSON para a cidade especificada.

### Exemplo de Requisição

```bash
curl http://127.0.0.1:5000/previsao?cidade=São%20Paulo
```

### Acesso a interface gráfica 

Para acessar a interface gráfica localmente, recomendamos a utilização da extensão "Live Server" dentro do Visual Studio Code ou navegue até o arquivo index.html e abra utilizando o navegador favorito. 
Caso queira utilizar de forma mais dinamica, ative o servidor.py e a api.py. Após a ativação, acesse o site: https://forecasting-gamma.vercel.app/
