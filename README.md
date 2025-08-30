# Learning MCP - Model Context Protocol Examples

This repository contains multiple MCP (Model Context Protocol) server implementations for learning and experimentation.

## 📁 Project Structure

```
learning-mcp-1/
├── weather-mcp/          # Weather MCP Server implementation
│   ├── weather_mcp.py    # MCP stdio server
│   ├── weather_http.py   # HTTP REST API server
│   ├── weather_sse.py    # Server-Sent Events server
│   └── README.md         # Weather-specific documentation
├── bits-course-mcp/      # BITS Course MCP Server (coming soon)
└── README.md             # This file
```

## 🚀 Projects

### 1. Weather MCP Server
A comprehensive weather data server using the US National Weather Service API.

**Features:**
- Real-time weather forecasts
- Weather alerts by state
- Multiple transport implementations (stdio, HTTP, SSE)

**Location:** `./weather-mcp/`
**Documentation:** [Weather MCP README](./weather-mcp/README.md)

### 2. BITS Course MCP Server
A comprehensive course guide for BITS Pilani 2nd year students with detailed information about subjects, study tips, and grading patterns.

**Features:**
- Course details for 10 core 2nd year subjects
- Study tips and recommendations from student experiences
- Grading insights and scoring strategies
- Topic-based search across all courses

**Location:** `./bits-course-mcp/`
**Documentation:** [BITS Course MCP README](./bits-course-mcp/README.md)

## 🛠️ Getting Started

Each project has its own dependencies and setup instructions. Navigate to the specific project folder and follow the README instructions.

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Quick Start
```bash
# Clone the repository
git clone <your-repo-url>
cd learning-mcp-1

# Navigate to a specific project
cd weather-mcp
# Follow the project-specific README
```

## 📚 About MCP

The Model Context Protocol (MCP) is an open protocol that enables AI assistants to securely connect to external data sources and tools. These examples demonstrate different ways to implement MCP servers.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**Tech Stack:** Python • FastMCP • FastAPI • Uvicorn • HTTPX