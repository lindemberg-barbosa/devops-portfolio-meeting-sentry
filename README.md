# Sentry - Flask example

Requirements:
  - python3
  - docker
  - docker compose

Flask App:
1. Enter in flask-app folder
1. Create a virtualenv: `python3 -m venv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install packages: `pip3 install -r requirements.txt`
1. Run app: `flask run --debug`
1. App will run in http://localhost:5000

Sentry:
1. Enter in Sentry folder
1. Run `SENTRY_IMAGE=getsentry/sentry:21.5.0 ./install.sh`
1. When the script finishes you can run Sentry with `docker compose up -d`
1. App will run in http://localhost:9000
