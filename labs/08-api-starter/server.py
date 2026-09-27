import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


TASKS = [
    {"id": 1, "title": "Inspect pump"},
]


class Handler(BaseHTTPRequestHandler):
    def _json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/tasks":
            return self._json(200, {"tasks": TASKS})

        if path.startswith("/tasks/"):
            raw_id = path.rsplit("/", 1)[-1]
            if not raw_id.isdigit():
                return self._json(400, {"error": "task id must be an integer"})

            task_id = int(raw_id)
            for task in TASKS:
                if task["id"] == task_id:
                    return self._json(200, task)

            return self._json(404, {"error": "task not found"})

        return self._json(404, {"error": "route not found"})

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/tasks":
            return self._json(404, {"error": "route not found"})

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)

        try:
            payload = json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return self._json(400, {"error": "invalid JSON"})

        title = payload.get("title")
        if not isinstance(title, str) or not title.strip():
            return self._json(400, {"error": "title is required"})

        task = {"id": len(TASKS) + 1, "title": title.strip()}
        TASKS.append(task)
        return self._json(201, task)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8766), Handler)
    print("Lab API listening on http://127.0.0.1:8766")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
