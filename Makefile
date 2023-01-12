-include .env
export $(shell sed 's/=.*//' .env)

export APP_NAME = app
export PYTHONPATH=$(CURDIR)

format:
	@black app
	@isort app

lint:
	@flake8 app
	@black --check app --diff
	@isort --check-only app

####################################
# Dependencies Commands
####################################
packages:
	@printf "Installing libraries... "
	@venv/bin/pip3.9 install -q --no-cache-dir -r requirements.txt
	@echo "OK"

env-create: env-destroy
	@printf "Creating virtual environment... "
	@virtualenv -q venv -p python3.9
	@echo "OK"

env-destroy:
	@printf "Destroing virtual environment... "
	@rm -rfd venv
	@echo "OK"

install: env-create packages

infra-up:
	@docker-compose up -d


####################################
# App (Run, Debug and Test) Commands
####################################
test:
	@py.test -vv -rxs --capture=tee-sys

coverage:
	@py.test -xs --cov app --cov-report xml --cov-report term-missing --cov-config .coveragerc

debug-api:
	@uvicorn app.interface.api.main:app --port ${PORT} --workers 3 --reload

run-api:
	@gunicorn app.interface.api.main:app -w 3 -k uvicorn.workers.UvicornWorker

alembic-upgrade:
	@alembic upgrade head