# BITS Course MCP Server

A comprehensive **Model Context Protocol (MCP)** server providing detailed information about BITS Pilani 2nd year courses. This server helps students get course details, study tips, grading information, and recommendations based on real student experiences.

## 🌟 Features

- **Course Information**: Detailed content for 10 core 2nd year subjects
- **Study Tips**: Practical advice from student experiences
- **Grading Insights**: Information about grading patterns and scoring strategies
- **Topic Search**: Find courses related to specific topics or keywords
- **Multiple Interfaces**: Both MCP stdio and HTTP REST API implementations

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone and setup
git clone <your-repo-url>
cd learning-mcp-1/bits-course-mcp

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
uv run python bits_mcp.py
```

**Configuration Example** (`~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "bits_course_local": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/learning-mcp-1/bits-course-mcp",
        "run",
        "bits_mcp.py"
      ]
    }
  }
}
```

### 2. HTTP Server
**Best for**: REST API integration, testing

```bash
# Run the HTTP server
uv run python bits_http.py
```

**Endpoints:**
- `GET /` - Health check
- `GET /subjects` - List all available subjects
- `POST /subject-details` - Get detailed information about a specific subject
- `POST /search-topics` - Search for courses by topic/keyword
- `POST /study-tips` - Get study tips for subjects

### 3. SSE Server (Server-Sent Events)
**Best for**: Real-time streaming applications, MCP SSE connections

```bash
# Run the SSE server
PORT=8081 uv run python bits_sse.py
```

**Endpoint:** `http://localhost:8081/sse`

**Features:**
- Real-time study tips streaming
- Connection status updates
- Periodic course advice
- Keep-alive pings

## 🛠️ Tools Available

| Tool | Parameters | Description |
|------|------------|-------------|
| `get_subject_details` | `subject_name` | Get comprehensive details about a specific subject |
| `search_course_topics` | `topic` | Find courses related to a keyword or topic |
| `get_study_tips` | `subject_name` (optional) | Get study recommendations and tips |
| `list_all_subjects` | None | Get complete list of all available subjects |

## 📚 Available Subjects

### Chemical Engineering (8 subjects)
- CHE F211, Chemical process calculations
- CHE F212, Fluid Mechanics
- CHE F213, Chemical Engineering Thermodynamics
- CHE F214, Engineering Chemistry
- CHE F241, Heat Transfer
- CHE F242, Numerical Methods for Chemical Engineering
- CHE F243, Material Science
- CHE F244, Separation Process I

### Mathematics (1 subject)
- MATH F211, Mathematics-III

### Economics (1 subject)
- ECON F211, Principles of Economics

## 📱 Usage Examples

### HTTP API Examples

```bash
# Get details about Fluid Mechanics
curl -X POST http://localhost:8081/subject-details \
  -H "Content-Type: application/json" \
  -d '{"subject_name": "Fluid Mechanics"}'

# Search for courses related to grading
curl -X POST http://localhost:8081/search-topics \
  -H "Content-Type: application/json" \
  -d '{"topic": "grading"}'

# Get study tips for a specific subject
curl -X POST http://localhost:8081/study-tips \
  -H "Content-Type: application/json" \
  -d '{"subject_name": "CHE F213"}'

# List all subjects
curl http://localhost:8081/subjects
```

### In Cursor/Claude Desktop
- "Tell me about Fluid Mechanics course in BITS 2nd year"
- "What are the grading patterns for Chemical Engineering subjects?"
- "Give me study tips for Heat Transfer"
- "Which courses require regular attendance?"
- "What textbooks are recommended for Thermodynamics?"

## 📋 Sample Responses

### Subject Details
```json
{
  "subject": "CHE F212, Fluid Mechanics",
  "content": [
    "This course is the basic introduction to fluid mechanics...",
    "It is an important technical subject which will be taken up during interviews...",
    "Grading is good, in a class of 120 students about 14 students got A grade."
  ],
  "total_points": 11,
  "formatted_content": "• This course is the basic introduction to fluid mechanics..."
}
```

### Topic Search
```json
{
  "topic_searched": "grading",
  "matching_courses": 7,
  "results": [
    {
      "subject": "CHE F212, Fluid Mechanics",
      "relevant_points": ["Grading is good, in a class of 120 students about 14 students got A grade."],
      "total_content_points": 11
    }
  ]
}
```

## 🧪 Testing

### Test MCP Server
```bash
# Test tool listing
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' | uv run python bits_mcp.py

# Test subject details tool
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "get_subject_details", "arguments": {"subject_name": "Fluid Mechanics"}}}' | uv run python bits_mcp.py
```

### Test HTTP Server
```bash
# Health check
curl http://localhost:8081/

# Test subject details
curl -X POST http://localhost:8081/subject-details \
  -H "Content-Type: application/json" \
  -d '{"subject_name": "Mathematics-III"}'
```

## 🎯 Key Features

### Smart Search
- Search by subject code (e.g., "CHE F211")
- Search by partial name (e.g., "Fluid Mechanics")
- Topic-based search across all courses

### Comprehensive Information
- Course content and objectives
- Study strategies and tips
- Grading patterns and expectations
- Textbook recommendations
- Professor insights and teaching styles

### Student-Centric Data
- Real student experiences and advice
- Practical tips for scoring well
- Information about tutorial tests and assignments
- Prerequisites and course connections

## 🔍 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port
   lsof -i :8081
   # Kill the process
   kill -9 <PID>
   ```

2. **MCP Server Not Responding**
   - Use the HTTP server for testing: `uv run python bits_http.py`
   - Check if all dependencies are installed: `uv sync`

3. **Subject Not Found**
   - Use exact subject codes or partial names
   - Check available subjects: `curl http://localhost:8081/subjects`

## 📖 Data Source

The course information is based on real student experiences and feedback from BITS Pilani 2nd year Chemical Engineering students. The data includes:

- Course content and structure
- Study strategies that work
- Grading patterns and expectations
- Professor teaching styles
- Practical tips for success

## 🤝 Contributing

1. Fork the repository
2. Add new course data or improve existing information
3. Test your changes with both MCP and HTTP servers
4. Submit a pull request

---

**Tech Stack:** Python • FastMCP • FastAPI • Uvicorn • JSON Data Processing
