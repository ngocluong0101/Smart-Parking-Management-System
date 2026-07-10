# Deployment Diagram

```mermaid
flowchart LR
    User[Browser] --> Nginx[Nginx Reverse Proxy]
    Nginx --> FE[React Frontend]
    Nginx --> BE[FastAPI Backend]
    BE --> AI[AI Inference Service]
    BE --> DB[(MySQL)]
    AI --> WEIGHTS[YOLO Weights]
    BE --> LOGS[Logs / Audit]
```
