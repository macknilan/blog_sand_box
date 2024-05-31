build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up

ps:
	docker compose -f local.yml ps

upd:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs

show-logs-django:
	docker compose -f local.yml logs --tail=100 -f django

show-logs-postgres:
	docker compose -f local.yml logs --tail=100 -f postgres

makemigrations:
	docker compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm django python manage.py migrate

superuser:
	docker compose -f local.yml run --rm django python manage.py createsuperuser

collectstatic:
	docker compose -f local.yml run --rm django python manage.py collectstatic --no-input --clear

down-v:
	# REMOVE NAMED VOLUMES DECLARED IN THE VOLUMES SECTION OF THE COMPOSE FILE AND ANONYMOUS VOLUMES ATTACHED TO CONTAINERS.
	docker compose -f local.yml down -v

volume:
	docker volume inspect local_postgres_data

authors-db:
	docker compose -f local.yml exec postgres psql --username=blog_sand_box_usr --dbname=blog_sand_box_db

ruff-check:
	docker compose -f local.yml exec django ruff check .

black-check:
	docker compose -f local.yml exec django black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec django black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec django black --exclude=migrations .


