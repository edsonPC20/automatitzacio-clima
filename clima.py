import requests
import json
from datetime import datetime

def obtener_datos():
    # Usamos la API de Open-Meteo para Manresa (puedes cambiar lat/long)
    url = "https://api.open-meteo.com/v1/forecast?latitude=41.7287&longitude=1.8244&hourly=temperature_2m"
    respuesta = requests.get(url)
    # Retornamos solo la lista de temperaturas horarias
    return respuesta.json()['hourly']['temperature_2m']

def calcular_estadisticas(temperaturas):
    # El enunciado prohíbe usar la API para estos cálculos; deben ser manuales
    max_t = max(temperaturas)
    min_t = min(temperaturas)
    mitjana_t = sum(temperaturas) / len(temperaturas)
    
    return {
        "temperatura_maxima": max_t,
        "temperatura_minima": min_t,
        "temperatura_mitjana": round(mitjana_t, 2)
    }

if __name__ == "__main__":
    lista_temps = obtener_datos()
    metricas = calcular_estadisticas(lista_temps)
    
    # Nombre del archivo con la fecha actual: temp_YYYYMMDD.json
    fecha_str = datetime.now().strftime("%Y%m%d")
    nombre_archivo = f"temp_{fecha_str}.json"
    
    with open(nombre_archivo, 'w') as f:
        json.dump(metricas, f, indent=4)
        
    print(f"Archivo {nombre_archivo} generado con éxito.")