# meltano demo day

GRPC , Protobuf, Mysql, all the random things I learned. 

### project repo

https://gitlab.com/pandemicsyn/llamalake/

### these slides (raw form)

https://gitlab.com/pandemicsyn/llamalake/-/blob/main/slides.md

---

## My criteria for success

✔ From my local console fire a GRPC message at a remote service (running in docker, or a remote vm)

✔ Have the remote service return a message confirming submission, or an error if the parsing fails (i.e. you ask it to do a remote meltano run tap tap target)

✔ Have the remote service perform the meltano run call using `meltano.core` NOT simply invoking the meltano cli.

✔ Have the remote service finish the meltano run and log the result to the remote console or a remote log file.


## Bonus content

✔ Remote service returns job info

~~Use GRPC streaming to stream the logs back to the client in real time.~~

x Planetscale for a meltano.db

✔ Evaluate [buf](https://buf.build) and publish the schema to the public registry


---

## First things first - wtf did I build. 

I wrapped meltano (the lib, not the cli) in a GRPC service that allows you to invoke `meltano run` style commands remotely. Like an API server, but better! Ok, maybe not better, but definite more fun. 

Lets see it in action. Server is over there -------------------->

---


## In action

We can execute a run as usual:

```bash
grpcurl -d '{"blocks": "tap-gitlab hide-gitlab-secrets target-jsonl", "force": false, "full_refresh": true}' \
-proto run.proto \
-import-path /home/syn/projects/llamalake/meltapi/v1 \
-plaintext localhost:50051 \
meltapi.v1.RunService/Submit
```
---


## In action

And of course multiple blocks work fine too

```bash
grpcurl -d '{"blocks": "tap-gitlab hide-gitlab-secrets target-jsonl tap-gitlab hide-gitlab-secrets target-jsonl"}' \
-proto run.proto \
-import-path /home/syn/projects/llamalake/meltapi/v1 \
-plaintext localhost:50051 \
meltapi.v1.RunService/Submit
```

---

## In action

And errors get bubbled up too, like plugins that's aren't installed:

```bash
➜ grpcurl -d '{"blocks": "what-even-is-this"}' \
     -proto run.proto \
     -import-path /home/syn/projects/llamalake/meltapi/v1 \
     -plaintext localhost:50051 \
     meltapi.v1.RunService/Submit
```
```
ERROR:
  Code: InvalidArgument
  Message: Block what-even-is-this not found
```
---

## In action

And bad invocation orders:

```bash
➜ grpcurl -d '{"blocks": "target-jsonl tap-gitlab"}' \
     -proto run.proto \
     -import-path /home/syn/projects/llamalake/meltapi/v1 \
     -plaintext localhost:50051 \
     meltapi.v1.RunService/Submit
```
```
ERROR:
  Code: InvalidArgument
  Message: block violates set requirements: Unknown command type or bad block sequence at index 1, starting block 'target-jsonl'
```

---

## How's this work.

- GRPC Stubs and protobuf
- A *ver smoll, much wow* python server
- Seriously, thats it

---

## How's this work.

- GRPC Stubs and protobuf
- A *ver smoll, much wow* python server
- Seriously, thats it

## learnings

- easiest part of the day! not having complex logic in `meltano.cli.run` paid off.
- theres mypy protobuf plugin \o/
- [open-tracing](https://github.com/opentracing-contrib/python-grpc) support looks like its g2g.
- python grpc has some quirks
  - interceptor's status is confusing. Random posts indicating its not implemented as it was spec'd. Some helper lib's exist: https://grpc-interceptor.readthedocs.io/en/latest/ , but mostly fine
  - repeated values  (can't assign directly, extend/append) 
  - asyncio version technically still beta but "stable" api sig
- Have some "ClickExceptions" too far back (mostly in parser) that should not be ClickExceptions.
- couple of log lines reference "cli" but are actually agnostic
- really need the ability to turn off the ETL log for jobs and a more generic way to hook in custom IO.
- fork() complaints ? not sure whats up. GIL still a problem because python gonna python

---

### What did I learn - mysql/planetscale

## Meltano + Planetscale: :((((

Probably just need to define some max string lengths in our migrations (some do, some don't). String() -> Varchar , and in MySQL land varchar's need a max length. 

Very small decisions can enable a larger eco system's. Fine to be opinionated and primarily focused on $ONE_TECH, but if we should exclude a tech/stack let's do so intentionally. 

---

### What did I learn - bonus content

## buf - https://buf.build 

>The Buf CLI is a one stop shop for your local Protocol Buffers needs

- makes proto dependency mgmt a lot better
- takes care of build, opinionated linting, breaking change detection, and generation! 🤩🤩🤩
- buf schema registry interesting - [meltapi](https://buf.build/pandemicsyn/meltapi)
- A++ would use again

Seriously, super awesome project and cli just hit v1 (raised $93 million to fix protobuf 🤯) 

