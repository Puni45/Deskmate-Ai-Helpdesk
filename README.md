# DeskMate AI Helpdesk

An AI-powered IT helpdesk assistant that handles employee IT support requests using natural language. DeskMate uses an LLM to understand user intent, orchestrate internal IT workflows, interact with mock enterprise systems, and provide intelligent responses through a chat interface.

---

## Features

- Password reset assistance
- Software access requests
- VPN troubleshooting
- Ticket status lookup
- Out-of-scope request handling
- AI-powered intent extraction
- Mock internal IT systems
- Real-time chat interface
- Observable backend execution logs

---

## Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- FastAPI
- Python

### LLM
- Groq API
- Llama 3.3 70B Versatile

---

## Architecture

```text
┌─────────────────────┐
│   Employee/User     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   React Frontend    │
│  (Chat Interface)   │
└─────────┬───────────┘
          │ HTTP API
          ▼
┌─────────────────────┐
│   FastAPI Backend   │
│   (Orchestration)   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│      LLM Layer      │
│  Groq + Llama 3.3   │
│ Intent Extraction   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Tool Orchestration │
│  Deterministic Flow │
└─────────┬───────────┘
          │
 ┌────────┼───────────┬────────────┐
 ▼        ▼           ▼            ▼
Password  Software   Ticket       VPN
Reset     Access     System       Support
Mock DB   Mock DB    Mock DB      Mock DB
```

---

## Key Design Decisions

- Deterministic orchestration instead of autonomous agents
- Structured JSON outputs from the LLM
- Explicit tool routing for observability and debugging
- Mock internal systems to simulate enterprise workflows
- Focus on reliability, traceability, and operational clarity

---

## Installation

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn openai python-dotenv fastapi[all]

python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm install axios

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## Environment Variables

Create a `.env` file inside the `backend/` folder:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Project Structure

```text
deskmate-ai-helpdesk/
│
├── backend/
│   ├── main.py              <- FastAPI entry point
│   ├── llm.py               <- LLM integration and intent extraction
│   ├── tools.py             <- IT workflow tools and orchestration
│   ├── mock_db.py           <- Mock enterprise IT systems
│   ├── .env                 <- Environment variables
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx          <- Main chat interface
│   │   ├── App.css          <- Frontend styling
│   │   └── main.jsx         <- React entry point
│   │
│   ├── package.json
│   └── vite.config.js
│
├── screenshots/
│   ├── frontend-working.png <- Frontend demo screenshot
│   ├── swagger-docs.png     <- FastAPI Swagger docs
│   └── backend-logs.png     <- Observable backend execution logs
│
├── README.md
├── DESIGN_NOTES.md
├── PRODUCTION_DESIGN.md
├── .gitignore
```

---

## Sample Queries

### Password Reset

User:

```text
Reset my password
```

DeskMate:

```text
Password reset link sent successfully.
```

---

### Software Access Request

User:

```text
I need access to Adobe Creative Suite
```

DeskMate:

```text
You do not currently have access to Adobe Creative Suite.
A priority ticket has been created: INC-8315
```

---

### VPN Support

User:

```text
My VPN is not working
```

DeskMate:

```text
VPN appears active. Try reconnecting.
```

---

### Ticket Status

User:

```text
What is the status of INC-1001?
```

DeskMate:

```text
Ticket INC-1001 is currently Open.
```

---

### Out-of-Scope Request

User:

```text
Book me a flight
```

DeskMate:

```text
I can only help with IT helpdesk-related requests.
```

---

## Screenshots

### Frontend Chat Interface

```text
screenshots/frontend-working.png
```

### Swagger API Docs

```text
screenshots/swagger-docs.png
```

### Backend Execution Logs

```text
screenshots/backend-logs.png
```

---

## Error Handling

The system gracefully handles:

- Out-of-scope requests
- Missing or malformed inputs
- Internal system failures
- Invalid ticket IDs
- Unexpected LLM outputs

---

## Production Considerations

Production design details are documented in:

```text
PRODUCTION_DESIGN.md
```

This includes:
- Azure deployment architecture
- hallucination mitigation
- observability strategy
- security considerations
- reliability engineering decisions

---

## Author

Puneeth Kumar B C  
1MV22AI044