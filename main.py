import asyncio
import aiohttp
import random
import time
import sys
from datetime import datetime

async def test_weather_endpoint(session):
    # Generate random latitude and longitude
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    
    # Format the URL with the random coordinates
    url = f"http://localhost:8000/weather/{lat}/{lon}"
    
    # Set headers
    headers = {
        "accept": "application/json"
    }
    
    try:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                print(f"Success! [{datetime.now()}] Coordinates: ({lat:.2f}, {lon:.2f})")
            else:
                print(f"Error: Status code {response.status}")
                
    except Exception as e:
        print(f"Request failed: {e}")

async def run_tests(duration, concurrent):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        request_count = 0
        
        while time.time() - start_time < duration:
            # Create a list of concurrent tasks
            tasks = [test_weather_endpoint(session) for _ in range(concurrent)]
            await asyncio.gather(*tasks)
            request_count += concurrent
            
        elapsed_time = time.time() - start_time
        print(f"\nTest Summary:")
        print(f"Duration: {elapsed_time:.2f} seconds")
        print(f"Total Requests: {request_count}")
        print(f"Requests per second: {request_count/elapsed_time:.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <duration_seconds> <concurrent_requests>")
        sys.exit(1)
        
    try:
        duration = int(sys.argv[1])
        concurrent = int(sys.argv[2])
    except ValueError:
        print("Duration and concurrent requests must be integers")
        sys.exit(1)
        
    print(f"Running tests for {duration} seconds with {concurrent} concurrent requests...")
    asyncio.run(run_tests(duration, concurrent))