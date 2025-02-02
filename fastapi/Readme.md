The application will be accessible at `http://localhost:8000`.

## API Endpoints

### Health Check

- **GET** `/health`

  Returns the health status of the application.

  **Response:**

  ```json
  {
    "status": "healthy"
  }
  ```

### Get Weather

- **GET** `/weather/{lat}/{lon}`

  Retrieves the current weather data for the specified latitude and longitude.

  **Parameters:**

  - `lat`: Latitude of the location (float).
  - `lon`: Longitude of the location (float).

  **Response:**

  ```json
  {
    "temperature": 25.0,
    "humidity": 60,
    "description": "clear sky",
    "wind_speed": 5.0
  }
  ```

## Docker Support

To run the application in a Docker container, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t weather-api .
   ```

2. Run the Docker container:

   ```bash
   docker run -d --name weather_app -p 8000:8000 --env-file .env weather-api
   ```

3. Access the application at `http://localhost:8000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
