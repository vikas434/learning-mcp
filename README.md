# MCP Weather Server

A **Model Context Protocol (MCP)** server that provides real-time weather data from the US National Weather Service API.

## What is MCP?

**Model Context Protocol** is a standard that allows AI assistants to securely connect to external data sources and tools. Think of it as a bridge between your AI and the real world.

### MCP Transport Types

| Transport | Use Case | Example |
|-----------|----------|---------|
| **stdio** | Local development, CLI tools | `uv run weather.py` |
| **SSE** | Web-based, real-time streaming | `http://localhost:8080/sse` |
| **HTTP** | REST APIs, web services | `POST /forecast` |

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- `uv` package manager

### Installation
```bash
git clone <repo>
cd weather
uv sync
```

### Run MCP Server (stdio)
```bash
uv run weather.py
```

### Test with MCP Client
```bash
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' | uv run weather.py
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_forecast",
        "description": "Get weather forecast for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
          }
        }
      },
      {
        "name": "get_alerts",
        "description": "Get weather alerts for a US state",
        "inputSchema": {
          "type": "object",
          "properties": {
            "state": {"type": "string"}
          }
        }
      }
    ]
  }
}
```

## 🌐 HTTP API (Deployed)

**Live API:** https://mcp-weather-server-720482586237.us-central1.run.app

### Get Weather Forecast
```bash
curl -X POST https://mcp-weather-server-720482586237.us-central1.run.app/forecast \
  -H "Content-Type: application/json" \
  -d '{"latitude": 40.7128, "longitude": -74.006}'
```

**Response:**
```json
{
  "forecasts": [
    {
      "name": "Today",
      "temperature": "64°F",
      "wind": "12 mph NE",
      "forecast": "Rain showers likely..."
    }
  ],
  "formatted": "Today:\nTemperature: 64°F\nWind: 12 mph NE..."
}
```

### Get Weather Alerts
```bash
curl -X POST https://mcp-weather-server-720482586237.us-central1.run.app/alerts \
  -H "Content-Type: application/json" \
  -d '{"state": "CA"}'
```

## 🔧 MCP Client Configuration

### Cursor IDE
Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

### Claude Desktop
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["--directory", "/path/to/weather", "run", "weather.py"]
    }
  }
}
```

## 🛠️ Available Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `get_forecast` | `latitude`, `longitude` | 5-day weather forecast |
| `get_alerts` | `state` (2-letter code) | Active weather alerts |

## 🌍 Deploy to Google Cloud

```bash
# Build and deploy
docker build -t gcr.io/PROJECT_ID/mcp-weather-server .
docker push gcr.io/PROJECT_ID/mcp-weather-server
gcloud run deploy mcp-weather-server --image gcr.io/PROJECT_ID/mcp-weather-server
```

## 📝 Example Usage

**In AI Chat:**
> "What's the weather in New York City?"

**MCP Tool Call:**
```json
{
  "tool": "get_forecast",
  "arguments": {
    "latitude": 40.7128,
    "longitude": -74.006
  }
}
```

**Result:**
```
Today: 64°F, Rain showers likely, 70% chance
Tonight: 60°F, Rain likely, 60% chance
Sunday: 65°F, Chance of rain, 40% chance
```

## 🔍 Troubleshooting

- **"No such file"**: Run from correct directory with `--directory` flag
- **"Unable to fetch"**: Coordinates must be within US territory
- **Rate limiting**: NWS API has usage limits

---

**Built with:** Python, FastMCP, National Weather Service API  
**License:** MIT
