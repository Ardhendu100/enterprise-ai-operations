                        Users
                          │
                          ▼
                 React + JavaScript
                          │
                          ▼
                    FastAPI Backend
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    Authentication   AI Orchestrator   REST APIs
                          │
                          ▼
                   Planner Agent
                          │
      ┌───────────┬───────────┬────────────┐
      ▼           ▼           ▼            ▼
 Research      SQL Agent   Report     Reviewer
  Agent                     Agent      Agent
      │           │           │
      ▼           ▼           ▼
 External      PostgreSQL    PDF/Excel
 APIs                        Generator
                          │
                          ▼
                    Final Response

────────────────────────────────────────────

## Supporting Services

• PostgreSQL
• Redis
• Qdrant
• Celery
• Docker
• Nginx
• Prometheus
• Grafana
• Loki

## Architecture Principles

Modular Monolith (v1)
API First
Clean Architecture
Repository Pattern
Service Layer
Async First
Stateless APIs
Dependency Injection
Event-Driven Background Jobs
Secure by Default

## Core Modules
Frontend
----------
Authentication
Dashboard
Chat
Reports
Knowledge Base
Settings
Admin

Backend
---------
API
Auth
Users
Chat
Agents
Reports
Knowledge
Notifications

AI Layer
----------
Planner Agent
Research Agent
SQL Agent
Report Agent
Reviewer Agent

Future:
-------
Memory Agent
Notification Agent
Security Agent
Data Layer
PostgreSQL
Redis
Qdrant


Data Layer
-----------
PostgreSQL
Redis
Qdrant


Infrastructure
----------
Docker
GitHub Actions
Monitoring
Logging
