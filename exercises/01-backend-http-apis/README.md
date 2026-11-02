# 🌐 Exercises: Stage 01 (Backend Fundamentals)

### `EX-01-1`: HTTP/HTTPS & cURL Deep Dive
* **Goal**: Understand the raw mechanics of HTTP requests and responses.
* **Tasks**:
  1. Use `curl -v` to query public endpoints (e.g. `https://httpbin.org/get`, `/post`, `/status/404`).
  2. Inspect the request line, TLS handshake, headers sent, and response status lines.
  3. Send custom headers (`Authorization: Bearer token`, `Content-Type: application/json`).
  4. Document your observations in `exercises/01-backend-http-apis/curl-notes.md`.

---

### `EX-01-2`: RESTful API & OpenAPI Specification
* **Goal**: Learn contract-first API design using OpenAPI 3.0 / Swagger.
* **Tasks**:
  1. Design a REST API specification for a Mentorship Platform in YAML (`openapi-spec.yaml`).
  2. Define endpoints:
     - `GET /api/v1/mentees` (pagination with query params `page`, `size`)
     - `POST /api/v1/mentees` (create mentee with validation)
     - `GET /api/v1/mentees/{id}/submissions`
     - `POST /api/v1/submissions/{id}/review`
  3. Include proper HTTP response status codes: `200`, `201`, `400`, `404`, `409`.
  4. Define standard error payload according to RFC 7807 (Problem Details).

---

### `EX-01-3`: Raw Java HTTP Socket Server
* **Goal**: Demystify web servers by writing a minimal HTTP server in pure Java without Spring or Tomcat.
* **Tasks**:
  1. Implement `SimpleHttpServer.java` listening on port `8080` using `java.net.ServerSocket`.
  2. Read incoming TCP byte stream, parse the HTTP request line (`GET /hello HTTP/1.1`).
  3. Construct a valid HTTP/1.1 response string with headers (`Content-Type: text/plain`, `Content-Length`) and body.
  4. Test it by opening `http://localhost:8080/hello` in your browser or with `curl`.
