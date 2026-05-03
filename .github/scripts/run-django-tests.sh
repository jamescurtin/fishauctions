#!/usr/bin/env bash
# Run the Django test suite under coverage and emit XML + HTML reports.
# Designed to run inside the `test` compose service (see docker-compose.yaml).
# coverage `data_file = "/tmp/.coverage"` is set in pyproject.toml so per-worker
# files survive the container's `app` user (uid 1000) bind-mount permissions.

set -u

coverage run manage.py test --parallel auto
rc=$?

# Combine per-worker data files; tolerate the no-op case (single-worker / rerun).
coverage combine 2>/dev/null || true
coverage xml -o coverage-out/coverage.xml
coverage html -d coverage-out/htmlcov

exit "$rc"
