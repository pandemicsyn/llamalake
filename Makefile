
pygen:
	python -m grpc_tools.protoc --proto_path=proto run.proto --python_out=gr --grpc_python_out=gr

test:
	poetry run pytest

lint:
	poetry run black gr tests
