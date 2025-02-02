from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Get API key from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

class WeatherResponse(BaseModel):
    temperature: float
    humidity: float
    description: str
    wind_speed: float

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/weather/{lat}/{lon}", response_model=WeatherResponse)
async def get_weather(lat: float, lon: float):
    # Validate coordinates
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise HTTPException(status_code=400, detail="Invalid coordinates")
    
    # OpenWeatherMap API URL
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Use metric units for temperature
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            return WeatherResponse(
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"],
                description=data["weather"][0]["description"],
                wind_speed=data["wind"]["speed"]
            )
            
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Failed to fetch weather data")