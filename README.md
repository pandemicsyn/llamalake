# Project llamalake

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

# gr/

A simple GRPC server that allows invoking `meltano run` style commands remotely. 

### run the service

```
(grpc) ➜ llamalake (main) ✗ python gr/main.py
```

### generate python proto files

```
(grpc) ➜ llamalake (main) ✗ make pygen
```