FROM python:3.8-slim-buster AS builder
ENV PYTHONBUFFERED 1
WORKDIR /opt/webapp/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# copy requirements.txt
COPY ./requiremnets.txt /opt/webapp/requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

# runner stage
FROM python:3.8-slim-buster AS runner

ARG SECRET_KEY
ARG DEBUG

WORKDIR /opt/webapp
RUN groupadd -r django \
  && useradd -d /opt/webapp -r -g django django \
  && chown django:django -R /opt/webapp
USER django

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --chown=django:django . /opt/webapp/
RUN python manage.py migrate

# run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]