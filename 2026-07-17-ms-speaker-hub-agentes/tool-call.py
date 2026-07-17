import json
import requests
from openai import OpenAI

# ==========================
# Configuración
# ==========================

endpoint = input("Endpoint: ").strip()
api_key = input("API Key: ").strip()
deployment = input("Deployment: ").strip()

client = OpenAI(
    base_url=endpoint.rstrip("/") + "/openai/v1/",
    api_key=api_key
)

# ==========================
# Tool
# ==========================

def get_weather(city):
    # Buscar coordenadas
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "language": "es",
            "format": "json"
        }
    ).json()

    if "results" not in geo:
        return {"error": "Ciudad no encontrada"}

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    # Consultar clima
    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,weather_code"
        }
    ).json()

    return {
        "city": city,
        "temperature": weather["current"]["temperature_2m"],
        "weather_code": weather["current"]["weather_code"]
    }

# ==========================
# Llamada al modelo
# ==========================

response = client.responses.create(
    model=deployment,
    input="¿Cuál es el clima actual en Córdoba, Argentina?",
    tools=[
        {
            "type": "function",
            "name": "get_weather",
            "description": "Obtiene el clima actual de una ciudad.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Nombre de la ciudad"
                    }
                },
                "required": ["city"]
            }
        }
    ]
)

# ==========================
# Ejecutar Tool
# ==========================

tool_outputs = []

for item in response.output:

    if item.type == "function_call":

        print("Tool solicitada:", item.name)
        print("Argumentos:", item.arguments)

        args = json.loads(item.arguments)

        result = get_weather(args["city"])

        tool_outputs.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps(result)
        })

# ==========================
# Segunda llamada
# ==========================

response2 = client.responses.create(
    model=deployment,
    previous_response_id=response.id,
    input=tool_outputs
)

print("\n==========================")
print(response2.output_text)
