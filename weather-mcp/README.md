# Weather MCP Server

A comprehensive **Model Context Protocol (MCP)** server providing real-time weather data via the US National Weather Service API. This project demonstrates three different MCP transport implementations.

## 🌟 Features

- **Real-time Weather Data**: Current conditions, forecasts, and alerts
- **Multiple Transports**: stdio, HTTP, and SSE implementations
- **US National Weather Service**: Official government weather data
- **Easy Integration**: Works with Cursor, Claude Desktop, and custom MCP clients

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone and setup
git clone <your-repo-url>
cd learning-mcp-1/weather-mcp

# Initialize virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

## 🔧 Available Servers

### 1. MCP Server (stdio) - Recommended
**Best for**: MCP clients like Cursor, Claude Desktop

```bash
# Run the server
python weather_mcp.py
```

**Configuration Example** (`~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "weather_local": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/learning-mcp-1/weather-mcp",
        "run",
        "weather_mcp.py"
      ]
    }
  }
}
```

### 2. HTTP Server
**Best for**: REST API integration, testing

```bash
# Run the HTTP server
python weather_http.py
```

**Endpoints:**
- `GET /` - Health check
- `POST /forecast` - Get weather forecast
- `POST /alerts` - Get weather alerts

**Example Usage:**
```bash
# Get forecast for NYC
curl -X POST http://localhost:8080/forecast \
  -H "Content-Type: application/json" \
  -d '{"latitude": 40.7128, "longitude": -74.006}'

# Get alerts for California
curl -X POST http://localhost:8080/alerts \
  -H "Content-Type: application/json" \
  -d '{"state": "CA"}'
```

### 3. SSE Server (Server-Sent Events)
**Best for**: Real-time streaming applications

```bash
# Run the SSE server
python weather_sse.py
```

**Endpoint:** `http://localhost:8000/sse`

## 🛠️ Tools Available

| Tool | Parameters | Description |
|------|------------|-------------|
| `get_forecast` | `latitude`, `longitude` | Get 5-day weather forecast for coordinates |
| `get_alerts` | `state` (2-letter code) | Get active weather alerts for US state |

## 📱 Client Configuration

### Cursor IDE
Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "weather_local": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/learning-mcp-1/weather-mcp",
        "run",
        "weather_mcp.py"
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
      "args": [
        "--directory",
        "/absolute/path/to/learning-mcp-1/weather-mcp",
        "run",
        "weather_mcp.py"
      ]
    }
  }
}
```

## 🧪 Testing

### Test MCP Server
```bash
# Test tool listing
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' | python weather_mcp.py

# Test forecast tool
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "get_forecast", "arguments": {"latitude": 40.7128, "longitude": -74.006}}}' | python weather_mcp.py
```

### Test HTTP Server
```bash
# Health check
curl http://localhost:8080/

# Test forecast
curl -X POST http://localhost:8080/forecast \
  -H "Content-Type: application/json" \
  -d '{"latitude": 40.7128, "longitude": -74.006}'
```

## 📋 Usage Examples

### In Cursor/Claude Desktop
- "What's the weather in New York City?"
- "Are there any weather alerts for California?"
- "Give me the 5-day forecast for San Francisco"

### Expected Response Format
```
Today:
Temperature: 72°F
Wind: 8 mph SW
Forecast: Partly cloudy with a chance of afternoon showers...
```

## 🔍 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port
   lsof -i :8080
   
   # Kill process if needed
   kill -9 <PID>
   ```

2. **Virtual Environment Issues**
   ```bash
   # Recreate virtual environment
   rm -rf .venv
   uv venv
   source .venv/bin/activate
   uv sync
   ```

3. **Path Issues in MCP Config**
   - Use absolute paths in MCP configuration
   - Ensure the directory path exists
   - Check file permissions

## 🌐 Deployment

### Google Cloud Run
```bash
# Build and deploy
docker build -t gcr.io/PROJECT_ID/mcp-weather-server .
gcloud run deploy mcp-weather-server \
  --image gcr.io/PROJECT_ID/mcp-weather-server \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 📊 Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   MCP Client    │    │  Weather Server  │    │ NWS Weather API │
│  (Cursor/CLI)   │◄──►│   (This Repo)    │◄──►│  (External)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🛡️ API Limits

- **National Weather Service API**: No authentication required
- **Rate Limits**: Reasonable use (no official limits published)
- **Coverage**: United States only

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**Tech Stack:** Python • FastMCP • Uvicorn • HTTPX • National Weather Service API
