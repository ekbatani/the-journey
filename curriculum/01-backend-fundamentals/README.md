# 🌐 Stage 01: Backend Fundamentals

> **Roadmap**: [roadmap.sh/backend](https://roadmap.sh/backend)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Understand how the Internet, DNS, and TCP/IP operate beneath the surface.
- Master the HTTP/1.1 and HTTP/2 protocols (methods, headers, status codes, request/response cycles).
- Grasp REST architectural principles and design clear, predictable JSON APIs.
- Understand how web servers process incoming network connections.

---

## 📚 Core Topics & Knowledge Map

### 1. How the Web Works
- **DNS (Domain Name System)**: Translating domain names to IP addresses (A, AAAA, CNAME records).
- **TCP/IP & Handshakes**: Three-way handshake (`SYN` -> `SYN-ACK` -> `ACK`), connection reliability.
- **TLS/HTTPS**: Asymmetric encryption for key exchange, symmetric encryption for data transfer.

### 2. HTTP Deep Dive
- **Methods**: `GET` (safe/idempotent), `POST` (non-idempotent), `PUT` (idempotent replacement), `PATCH` (partial modification), `DELETE` (idempotent removal).
- **Status Codes**:
  - `2xx`: Success (`200 OK`, `201 Created`, `204 No Content`)
  - `3xx`: Redirection (`301 Moved Permanently`, `304 Not Modified`)
  - `4xx`: Client Errors (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`)
  - `5xx`: Server Errors (`500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`)
- **Headers**: Content-Type, Authorization, Accept, Cache-Control, User-Agent, CORS headers (`Access-Control-Allow-Origin`).

### 3. REST Architectural Principles
- Stateless communication.
- Client-server separation.
- Resource-oriented URIs (`/api/v1/orders/123/items`).
- Proper use of HTTP verbs and representation formats (JSON).

---

## 🧪 Assigned Exercises
Navigate to [`exercises/01-backend-http-apis/`](../../exercises/01-backend-http-apis/):
* **`EX-01-1`**: HTTP/HTTPS & cURL Deep Dive
* **`EX-01-2`**: RESTful API & OpenAPI Specification
* **`EX-01-3`**: Raw Java HTTP Socket Server
