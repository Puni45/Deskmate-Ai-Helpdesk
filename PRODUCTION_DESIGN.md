# Production Design Note

## Azure Architecture

A production version of DeskMate would use:

- Azure OpenAI
- Azure App Service or AKS
- Azure API Management
- Azure Key Vault
- CosmosDB or PostgreSQL
- Azure Monitor + Application Insights

---

## Biggest Risks

### Hallucinated Tool Execution

LLMs may trigger incorrect workflows or actions.

Mitigations:
- structured JSON outputs
- validation layers
- deterministic orchestration
- explicit tool boundaries

---

### Prompt Injection

Users may attempt to manipulate prompts.

Mitigations:
- system prompts
- strict tool permissions
- allowlisted actions
- input validation

---

### Reliability

External LLM APIs may fail or timeout.

Mitigations:
- retries
- fallback responses
- circuit breakers
- timeout handling

---

### Observability

Operational systems require traceability.

Mitigations:
- structured logging
- correlation IDs
- OpenTelemetry tracing
- centralized monitoring

---

### Security

Employee IT systems may contain sensitive information.

Mitigations:
- RBAC
- Azure Key Vault
- private networking
- audit logging

---

## Future Improvements

- Real ticketing integrations
- Slack/MS Teams support
- Knowledge base search
- Multi-user support
- Authentication and authorization