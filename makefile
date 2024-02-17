package_dir := src
code_dir := $(package_dir)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run_local
run_local: ## Run the application locally (python package)
	python3 -B -m $(package_dir)

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

.PHONY: lint
ruff:  ## Ruff check
	poetry run ruff .

.PHONY: mypy
mypy: ## mypy checl
	poetry run mypy . --explicit-package-bases

.PHONY: uvicorn
uvicorn: ## run your FastAPI app
	uvicorn --factory src.app.main:create_app
