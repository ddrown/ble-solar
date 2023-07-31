test: venv
	venv/bin/python -m pytest -s tests

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

.PHONY: test
