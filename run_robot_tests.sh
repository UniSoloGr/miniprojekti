
#!/usr/bin/env bash
set -e

export DATABASE_URL="sqlite:///test.db"
export SECRET_KEY="test-secret-key"

uv run python src/db_helper.py

uv run python src/index.py &
SERVER_PID=$!

trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

for i in {1..30}; do
    if curl -fsS http://127.0.0.1:5001/ >/dev/null; then
        break
    fi
    sleep 1
done

uv run robot src/tests/app.robot
