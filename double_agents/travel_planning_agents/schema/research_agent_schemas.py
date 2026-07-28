from pydantic import BaseModel
from datetime import date, time


class FlightSearchInput(BaseModel):
    departure_id: str
    arrival_id: str
    departure_date: date


class FlightOption(BaseModel):
    airline: str
    price: float
    duration: float
    departure: str
    arrival: str
    layovers: int


class FlightSearchOutput(BaseModel):
    departure_id: str
    arrival_id: str
    departure_date: date
    flights: list[FlightOption]


class TravelDetails(BaseModel):
    departure_city: str
    departure_airport: str
    destination_city: str
    destination_airport: str
    departure_date: date


class WeatherInput(BaseModel):
    city: str


class WeatherForecast(BaseModel):
    datetime: str
    temperature: float
    feels_like: float
    humidity: int
    weather: str
    description: str


class WeatherOutput(BaseModel):
    city: str
    forecasts: list[WeatherForecast]


class ResearchOutput(BaseModel):
    travel_details: TravelDetails
    flight_information: FlightSearchOutput
    weather_information: WeatherOutput
