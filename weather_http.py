from typing import Any
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI(title="MCP Weather Server", description="Weather API using National Weather Service")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

# Request models
class AlertsRequest(BaseModel):
    state: str

class ForecastRequest(BaseModel):
    latitude: float
    longitude: float

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "MCP Weather Server is running", "status": "healthy"}

@app.get("/health")
async def health():
    """Health check endpoint for Cloud Run."""
    return {"status": "healthy"}

@app.post("/alerts")
async def get_alerts(request: AlertsRequest):
    """Get weather alerts for a US state."""
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        raise HTTPException(status_code=404, detail="Unable to fetch alerts or no alerts found.")

    if not data["features"]:
        return {"message": "No active alerts for this state.", "alerts": []}

    alerts = [format_alert(feature) for feature in data["features"]]
    return {"alerts": alerts, "formatted": "\n---\n".join(alerts)}

@app.post("/forecast")
async def get_forecast(request: ForecastRequest):
    """Get weather forecast for a location."""
    points_url = f"{NWS_API_BASE}/points/{request.latitude},{request.longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        raise HTTPException(status_code=404, detail="Unable to fetch forecast data for this location.")

    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        raise HTTPException(status_code=404, detail="Unable to fetch detailed forecast.")

    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append({
            "name": period['name'],
            "temperature": f"{period['temperature']}°{period['temperatureUnit']}",
            "wind": f"{period['windSpeed']} {period['windDirection']}",
            "forecast": period['detailedForecast'],
            "formatted": forecast.strip()
        })

    return {"forecasts": forecasts, "formatted": "\n---\n".join([f["formatted"] for f in forecasts])}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port) 