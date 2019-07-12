
clean: clean-build clean-others clean-pyc clean-test

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-others:
	@find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

test:
	@py.test -s tests

coverage:
	@py.test -s tests --cov

coverage.html:
	@py.test -s tests --cov --cov-report=html

pep8:
	@pep8 --filename="*.py" --ignore=W --first --show-source --statistics --count

deps:
	pip3 install -r requirements.txt

free:
	pip3 freeze > requirements.txt

run:
	python3 manage.py runserver

setup:
	python3 manage.py makemigrations
	python3 manage.py migrate

merge:
	python3 manage.py makemigrations --merge

user:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell

app:
	python3 manage.py startapp $(n)

migra:
	python3 manage.py makemigrations $(n)
	python3 manage.py migrate $(n)

static:
	python3 manage.py collectstatic
