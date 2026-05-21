# Design Notes

## Why FastAPI?

FastAPI was chosen because it is lightweight, fast to develop with, and provides automatic API documentation.

## Why React?

React provides a clean and interactive frontend chat interface.

## Why Deterministic Tool Orchestration?

The system uses structured intent extraction followed by explicit tool execution instead of fully autonomous agents.

This improves:
- observability
- debugging
- reliability
- predictability

for operationally sensitive helpdesk workflows.

## Why Mock Internal Systems?

The assignment specifically scoped internal systems as mocks. The focus was therefore placed on workflow orchestration and AI integration rather than infrastructure complexity.

## Observability

The system logs:
- incoming user queries
- LLM outputs
- tool execution
- ticket creation
- errors

This enables easier debugging and tracing.

## Tradeoffs

The solution prioritizes:
- simplicity
- fast iteration
- clarity of architecture
- debuggability

over:
- production scalability
- advanced security hardening
- distributed infrastructure