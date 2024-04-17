test-all:
	coverage run -m unittest tests/*.py
	coverage html

test-all-report:
	coverage run -m unittest tests/*.py
	coverage report

test-utils:
	coverage run -m unittest tests/test_utils.py
	coverage report

test-restaurant:
	coverage run -m unittest tests/test_restaurant.py
	coverage report

test-tableprinter:
	coverage run -m unittest tests/test_table_printer.py
	coverage report

fix-codestyle:
	isort .
	autopep8 --recursive --in-place .

lint:
	pylint --rcfile .pylintrc --exit-zero .

run:
	python main.py