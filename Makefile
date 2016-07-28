migrate:
	- python airmap/manage.py makemigrations users travels
	- python airmap/manage.py migrate
