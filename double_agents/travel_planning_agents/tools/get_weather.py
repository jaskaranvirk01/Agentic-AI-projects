from langchain_core.tools import tool
from dotenv import load_dotenv
import os
import requests
from schema.research_agent_schemas import WeatherInput, WeatherForecast, WeatherOutput

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')


@tool(args_schema=WeatherInput)
def get_weather(city: str) -> WeatherOutput:
    '''Get 5 days weather forecast for the given city'''
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}

    data = response.json()

    forecasts = []

    for item in data['list'][:8]:
        forecasts.append(
            WeatherForecast(
                datetime=item["dt_txt"],
                temperature=item["main"]["temp"],
                feels_like=item["main"]["feels_like"],
                humidity=item["main"]["humidity"],
                weather=item["weather"][0]["main"],
                description=item["weather"][0]["description"]
            )
        )

    return WeatherOutput(
        city=data["city"]["name"],
        forecasts=forecasts,
    )


response = get_weather.invoke({
    "city": "Tokyo"
})

print(response)
