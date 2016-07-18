migrate:
	- python airmap/manage.py makemigrations users
	- python airmap/manage.py migrate
