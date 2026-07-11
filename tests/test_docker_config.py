from __future__ import annotations

import subprocess


def test_docker_compose_config_renders():
    result = subprocess.run(
        ["bash", "-lc", "cd docker && docker compose --env-file .env.example config"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "services:" in result.stdout
    assert "backend:" in result.stdout
    assert "frontend:" in result.stdout
    assert "db:" in result.stdout
