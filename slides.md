# meltano demo day

GRPC , Protobuf, Mysql, all the random things I learned. 

### links

[project repo](https://gitlab.com/pandemicsyn/llamalake/)

[slides (raw form)](https://gitlab.com/pandemicsyn/llamalake/-/blob/main/slides.md)


```
 _________________________
 < Llamalake > Datalake  >
 -------------------------
             O
              O
               o
                \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \____(      )___) )___
  \______(_______;;; __;;;
```

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
-import-path ~/projects/llamalake/meltapi/v1 \
-plaintext dev:50051 \
meltapi.v1.RunService/Submit
```
---


## In action

And of course multiple blocks work fine too:

```bash
grpcurl -d '{"blocks": "tap-gitlab target-jsonl tap-gitlab target-jsonl"}' \
-proto run.proto \
-import-path ~/projects/llamalake/meltapi/v1 \
-plaintext dev:50051 \
meltapi.v1.RunService/Submit
```

---

## In action

And errors get bubbled up too, like plugins that's aren't installed:

```bash
grpcurl -d '{"blocks": "what-even-is-this"}' \
     -proto run.proto \
     -import-path ~/projects/llamalake/meltapi/v1 \
     -plaintext dev:50051 \
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
grpcurl -d '{"blocks": "target-jsonl tap-gitlab"}' \
     -proto run.proto \
     -import-path ~/projects/llamalake/meltapi/v1 \
     -plaintext dev:50051 \
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

You start with `run.proto`...

```protobuf
syntax = "proto3";
package meltapi.v1;

// RunService provides a way to execute a `meltano run` like command via GRPC.
service RunService{
 rpc Submit(SubmitRequest) returns (SubmitResponse) {}
}

message SubmitRequest{
 // The blocks to execute e.g. "tap-gitlab some-mapping target-jsonl"
 string blocks = 1;
 // Whether to perform a full refresh
 bool full_refresh = 2;
 // Whether to force a run even if a job with the same ID is already running
 bool force = 3;
}

message SubmitResponse{
 repeated Job jobs = 1;
}

message Job{
 int64 id = 1;
 string job_id = 2;
 string state = 3;
}
```


---

## How's this work.

- GRPC Stubs and protobuf
- A *ver smoll, much wow* python server
- Seriously, thats it


...and after a `buf generate*` end up with


```tree

gr
├── __init__.py
├── main.py    <---- our server that we wrote to satisfy the stubs
└── meltapi
    └── v1
        ├── run_pb2.py      <-- "python" for our protobuf schema
        ├── run_pb2.pyi     <-- type hints 
        └── run_pb2_grpc.py <-- python grpc stubs for clients and services
gen
└── proto
    └── go
        └── meltapi
            └── v1
                ├── run.pb.go      <-- Go types for our protobuf schema
                └── run_grpc.pb.go <-- Go grpc stubs for clients and services
```

Big take away: we can generate clients and lang specific types for python, Go, JS, etc etc

Next step is to satisfy the service stubs...

*more on `buf` coming up

---

## How's this work.

- GRPC Stubs and protobuf
- A *ver smoll, much wow* python server
- Seriously, thats it

#### Ver smoll - server

~130 lines , including white space and log lines. By no means production ready but pretty dang small!

---

## How's this work.

- GRPC Stubs and protobuf
- A *ver smoll, much wow* python server
- Seriously, thats it

#### Ver smoll - server

~130 lines , including white space and log lines. By no means production ready but pretty dang small!


## learnings

- easiest part of the day! not having complex logic in `meltano.cli.run` paid off
- [open-tracing](https://github.com/opentracing-contrib/python-grpc) support looks like its g2g
- python grpc has some quirks
  - interceptor's status is confusing. Random posts indicating its not implemented as it was spec'd
  - repeated values  (can't assign directly, extend/append) 
  - asyncio version technically still beta but "stable" api sig
- Some meltano.core improvements:
  - Have some "ClickExceptions" too far back (mostly in parser) that should not be ClickExceptions
  - couple of log lines reference the cli but are actually agnostic
  - really need the ability to turn off the ETL log for jobs
- fork() complaints ? not sure whats up
- GIL still a problem because python gonna python

---

## My criteria for success

✔ From my local console fire a GRPC message at a remote service (running in docker, or a remote vm)

✔ Have the remote service return a message confirming submission, or an error if the parsing fails (i.e. you ask it to do a remote meltano run tap tap target)

✔ Have the remote service perform the meltano run call using `meltano.core` NOT simply invoking the meltano cli.

✔ Have the remote service finish the meltano run and log the result to the remote console or a remote log file.


## Bonus content

~~Use GRPC streaming to stream the logs back to the client in real time.~~

x Planetscale for a meltano.db

✔ Evaluate [buf](https://buf.build) and publish the schema to the public registry

---

### Bonus content - mysql/planetscale

#### ☠️  Meltano + Planetscale ☠️

Dead on arrival, initial create table's fail.

- Probably just need to define some max string lengths in our migrations (sometimes we do, sometimes we don't)
  - In sqlalchemy `String()` -> `Varchar`  for MySQL, and in MySQL land varchar's need a max length. 
- Maybe other stuff, gave up pretty quickly

---

### Bonus content - buf

##### buf - https://buf.build 

>The Buf CLI is a one stop shop for your local Protocol Buffers needs

- makes proto dependency mgmt a lot better
- takes care of build, opinionated linting, breaking change detection, and generation! 🤩🤩🤩
- buf schema registry interesting - [meltapi](https://buf.build/pandemicsyn/meltapi)
- A++ would use again

Seriously, super awesome project and cli just hit v1 (raised $93 million to fix protobuf 🤯). Makes protobuf a way better dev experience than in past.

---

# Questions ?


