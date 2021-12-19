.PHONY: run clean

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
DB0 = data/nba_players.csv
DB1 = data/nba_player_data.csv

.PHONY: all
all: 
	make clean
	make test
	git restore $(DB0)
	git restore $(DB1)

cli:
	$(PYTHON) my-sqlite/my_sqlite_cli.py

reset_db:
	git restore $(DB0)
	git restore $(DB1)

test: env
	$(PYTHON) test/qwasar_tests.py

env: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)	