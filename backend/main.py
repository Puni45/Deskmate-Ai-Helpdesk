from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

from llm import extract_intent
from tools import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    user: str
    message: str

@app.post("/chat")
def chat(query: Query):

    try:

        print("\n[INFO] User Query:", query.message)

        intent_data = extract_intent(query.message)

        print("[INFO] LLM Output:", intent_data)

        cleaned = intent_data.replace("```json", "").replace("```", "").strip()

        print("[INFO] Cleaned LLM Output:", cleaned)

        parsed = json.loads(cleaned)

        intent = parsed.get("intent")

        # SOFTWARE ACCESS
        if intent == "software_access":

            software = parsed.get("software")
            priority = parsed.get("priority", "medium")

            has_access = check_software_access(
                query.user,
                software
            )

            if has_access:

                return {
                    "response":
                    f"You already have access to {software}."
                }

            ticket_id = create_ticket(
                query.user,
                f"Access request for {software}",
                priority
            )

            return {
                "response":
                f"You do not currently have access to {software}. "
                f"A {priority} priority ticket has been created: {ticket_id}"
            }

        # PASSWORD RESET
        elif intent == "password_reset":

            result = reset_password(query.user)

            return {
                "response": result
            }

        # TICKET STATUS
        elif intent == "ticket_status":

            ticket_id = parsed.get("ticket_id")

            status = check_ticket_status(ticket_id)

            if status:

                return {
                    "response":
                    f"Ticket {ticket_id} is currently {status['status']}."
                }

            return {
                "response": "Ticket not found."
            }

        # VPN ISSUE
        elif intent == "vpn_issue":

            vpn_status = check_vpn(query.user)

            if vpn_status:

                return {
                    "response":
                    "VPN appears active. Try reconnecting."
                }

            ticket_id = create_ticket(
                query.user,
                "VPN issue",
                "high"
            )

            return {
                "response":
                f"VPN issue detected. Ticket created: {ticket_id}"
            }

        else:

            return {
                "response":
                "I can only help with IT helpdesk-related requests."
            }

    except Exception as e:

        print("[ERROR]", str(e))

        return {
            "response":
            "An internal error occurred."
        }