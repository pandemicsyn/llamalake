# Project LlamaLake

Catch all repo for all my meltano related explorations and hacks

![](docs/llama.jpeg)

# setup

1. clone and setup your python environment

```
git clone git@gitlab.com:pandemicsyn/llamalake.git
cd llamalake
pyenv virtualenv 3.8.12 grpc
pyenv local grpc
```

2. install the dependencies (including meltano)
```
pip install poetry
poetry install
```

3. setup meltano
```
meltano install
```

4. Profit!

Tip: run `make` or `make help` to see the available make commands

```bash
$ make
generate                       generate the protobuf/grpc files
lint                           run python and proto linters
mac-deps                       install mac dependencies - requires brew/pip
pygen-legacy                   TODO: remove this
run-gr                         run grpc server
```

## gr/

A simple GRPC server that allows invoking `meltano run` style commands remotely. 

### run the service

```
(grpc) ➜ llamalake (main) ✗ python gr/main.py
```

### working with proto buf files

This repo uses [buf](https://docs.buf.build/introduction/getting-started/) to build, lint, and generate proto files. The buf schema registry for this poc can be found at [https://buf.build/pandemicsyn/meltapi](https://buf.build/pandemicsyn/meltapi). It may or may not be up to date (theres no CI/CD setup yet to auto update it). Consulting the proto files directly is your best bet.

Currently, only python packages (include mypy hints) are built.

Install deps:

```
$ brew install protobuf buf
$ pip install mypy-protobuf
```

or if you're on MacOS:

```
make mac-deps
```


### generate proto files

```
buf generate
```

or

```
make generate
```

### lint proto files

```
buf lint
```

or 

```
make lint
```
