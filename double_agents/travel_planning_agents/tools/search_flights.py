from langchain_core.tools import tool
from schema.research_agent_schemas import FlightSearchInput,  FlightOption, FlightSearchOutput
import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
from datetime import date
load_dotenv()


SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')


@tool(args_schema=FlightSearchInput)
def search_flights(
    departure_id: str,
    arrival_id: str,
    departure_date: date,
) -> FlightSearchOutput:
    '''Search Google flights based on the input data'''
    params = {
        'engine': 'google_flights',
        'departure_id': departure_id,
        'arrival_id': arrival_id,
        'outbound_date': departure_date,
        "currency": "INR",
        "type": 2,  # One-way
        "hl": "en",
        "api_key": SERPAPI_API_KEY,
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
    except Exception as e:
        return {"error": str(e)}

    best_flights = results.get('best_flights', [])
    flights = []

    for flight in best_flights:
        flights.append(FlightOption(
            airline=flight['flights'][0]['airline'],
            price=flight['price'],
            duration=flight['total_duration'],
            departure=flight["flights"][0]["departure_airport"]["time"],
            arrival=flight["flights"][-1]["arrival_airport"]["time"],
            layovers=len(flight["flights"]) - 1,

        ))

    return FlightSearchOutput(
        departure_id=departure_id,
        arrival_id=arrival_id,
        departure_date=departure_date,
        flights=flights
    )


response = search_flights.invoke({
    "departure_id": "DEL",
    "arrival_id": "NRT",
    "departure_date": "2026-09-15"
})

print(response)
