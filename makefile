package_dir := src
code_dir := $(package_dir)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: docker_build
docker_build: ## Build Docker image
	docker compose build

.PHONY: docker_rebuild
docker_rebuild: ## Rebuild Docker image
	docker compose down
	docker compose build --no-cache

.PHONY: docker_up
docker_up: ## Run Docker container
	docker compose up -d

.PHONY: docker_down
docker_down: ## Stop Docker container
	docker compose down

.PHONY: alembic_upgrade
alembic_upgrade: ## Run Alembic migrations
	alembic upgrade head

.PHONY: alembic_downgrade
alembic_downgrade: ## Rollback Alembic migrations
	alembic downgrade -1

.PHONY: generate
generate:
	alembic revision --autogenerate -m "$(NAME)"

.PHONY: mypy
mypy:
	mypy . --explicit-package-bases

.PHONY: run
run: ## Run backend
	gunicorn -k uvicorn.workers.UvicornWorker \
	--workers=$(G_WORKERS) --bind "$(G_HOST):$(G_PORT)" \
	--log-level debug src.app.main:create_app
