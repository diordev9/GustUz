mig:
	./manage.py makemigrations
	./manage.py migrate
admin:
	python3 manage.py createsuperuser  --username admin --email  admin@mail.com

freeze:
	pip3 freeze > requirements.txt

install-lib:
	pip3 install -r requirements.txt
