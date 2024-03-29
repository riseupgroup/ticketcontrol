FROM python:3.9.10-alpine3.15
LABEL maintainer="https://github.com/riseupgroup"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt  /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

# use venv to seperate dependencies of python of those of alpine
# use non root user for security
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache --virtual .tmp-deps \
        linux-headers build-base musl-dev && \
    apk add --update --no-cache docker && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    mkdir -p /app/uploads && \
    mkdir -p /app/settings && \
    #chown -R app:app /vol && \
    #chmod -R 755 /vol/ && \
    #chown -R app:app /app/uploads && \
    #chmod -R 755 /app/uploads && \
    #chown -R app:app /app/settings && \
    #chmod -R 755 /app/settings && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]
