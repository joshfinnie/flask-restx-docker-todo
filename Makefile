run:
	@docker compose up

build:
	@docker compose build

format:
	@docker compose run app poetry run black todo