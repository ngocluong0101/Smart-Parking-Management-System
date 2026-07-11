from __future__ import annotations

from pathlib import Path
import subprocess


def test_frontend_build_artifacts_exist():
    frontend_dist = Path("frontend/dist")
    assert frontend_dist.exists(), "frontend dist folder should exist after build"
    assert (frontend_dist / "index.html").exists(), "frontend index.html should exist in dist"


def test_frontend_build_command_returns_zero():
    result = subprocess.run(
        ["bash", "-lc", "cd frontend && npm run build"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
