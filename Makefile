project = llamalake
sha = $(shell git rev-parse --short HEAD)

.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

test: ##
	poetry run pytest

lint: ## run python and proto linters
	poetry run black gr/*.py tests
	poetry run isort gr/*.py
	buf lint

generate: ## generate the protobuf/grpc files
	rm -rf gr/proto
	buf generate

pygen-legacy:  ## TODO: remove this
	python -m grpc_tools.protoc --proto_path=proto run.proto --python_out=gr --grpc_python_out=gr

run-gr: ## run grpc server
	python gr/main.py

mac-deps: ## install mac dependencies - requires brew/pip
	brew install protobuf buf
	pip install mypy-protobuf