#! /usr/bin/env bash
set -euo pipefail

RUFF_MODE=''
RUFF_FLAGS=''

usage() {
  cat << EOF >&2
Usage: $0 [OPTIONS]
Options:

--ci                  Run in CI mode: run all tests, lints, and formatting.
                      Fail if changes are required
-f, --format          Format the code
-F, --format-check    Run the formatter and fail if changes would be made
-l, --lint            Lint the code
-L, --lint-check      Run the linter and fail if changes would be made
-h, --help      Show this message and exit
EOF
}

process_args() {
    while test $# -gt 0
    do
      case "$1" in
          --ci) IS_CI='true'
              ;;
          --format | -f) RUFF_MODE='format'
              ;;
          --format-check | -F) RUFF_MODE='format'
              RUFF_FLAGS='--check'
              ;;
          --lint | -l) RUFF_MODE='check'
              RUFF_FLAGS='--fix'
              ;;
          --lint-check | -L) RUFF_MODE='check'
              ;;
          --help | -h) usage;
              exit 0
              ;;
          *) usage;
              exit 1;
              ;;
      esac
      shift
  done
}

process_args "$@"

if [ -z ${IS_CI+x} ]; then
  eval "ruff ${RUFF_MODE} /home/app/web ${RUFF_FLAGS} --ignore=E501"
else
  ruff format /home/app/web --check --ignore=E501
  ruff check /home/app/web --ignore=E501
fi
