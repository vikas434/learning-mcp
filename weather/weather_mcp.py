from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
import sys

# Initialize FastMCP server
mcp = FastMCP("weather")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

def debug_print(message: str):
    """Print debug messages to stderr to avoid interfering with MCP stdio."""
    print(message, file=sys.stderr)

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
        except Exception as e:
            debug_print(f"NWS API request failed: {e}")
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

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. MA)
    """
    debug_print(f"Getting alerts for {state}")
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    debug_print(f"Found {len(alerts)} alerts for {state}")
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float = 42.3601, longitude: float = -71.0589) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location (default Boston)
        longitude: Longitude of the location (default Boston)
    """
    debug_print(f"Getting forecast for {latitude}, {longitude}")
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    debug_print(f"Generated forecast with {len(forecasts)} periods")
    return "\n---\n".join(forecasts)

if __name__ == "__main__":
    debug_print("Starting MCP server")
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        debug_print(f"MCP server error: {e}")
    finally:
        debug_print("MCP server stopped")