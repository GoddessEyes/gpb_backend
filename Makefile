lint:
	isort -y
	flake8 --config=.flake8
	pylint src
