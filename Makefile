#Makefile


PORT ?= 8000
start:
	uv run python manage.py runserver

