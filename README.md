# catfacts-fastapi

# What
Cat facts! From FastAPI!

# Why
It amuses me.

# How
## Standalone
### Installing
`pip install .`
### Initialize database
`init-catfacts`
### Dev
`uvicorn catfacts_fastapi.main:app --reload`
### Prod
`gunicorn -w 4 -k uvicorn.workers.UvicornWorker catfacts_fastapi.main:app -b 0.0.0.0:8000 --access-logfile -`
## Docker
`docker compose up`, then try `curl http://localhost:8000`.
## Kubernetes

# Endpoints

* `/`: Retrieves a random fact.
* `/v2/`: Retrieves a random fact.
* `/v2/all`: Retrieves all facts.
* `/v2/random`: Retrieves a random fact.
* `/v2/fact/{id}`: Retrieves a fact by ID.

# There was a v1?

Yep! No, I don't know where the source code is.

# License

MIT.