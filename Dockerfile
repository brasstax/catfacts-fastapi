FROM python:3.9-slim
COPY . /
RUN pip install .
RUN init-catfacts
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "catfacts_fastapi.main:app", "-b", "0.0.0.0:8000", "--access-logfile", "-"]