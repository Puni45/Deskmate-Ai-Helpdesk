# DeskMate AI Helpdesk

DeskMate is an AI-powered IT helpdesk assistant that handles employee IT support requests using natural language.

---

# Features

- Password reset assistance
- Software access requests
- VPN troubleshooting
- Ticket status lookup
- Out-of-scope request handling
- AI-powered intent extraction
- Mock internal IT systems
- Real-time chat interface

---

# Tech Stack

## Frontend
- React
- Vite
- Axios

## Backend
- FastAPI
- Python

## LLM
- Groq API
- Llama 3.3 70B Versatile

---

# Architecture

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

---

# Setup Instructions

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn openai python-dotenv fastapi[all]
python -m uvicorn main:app --reload