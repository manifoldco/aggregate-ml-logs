FROM python:3.6.4

WORKDIR /opt/src/
COPY . ./
ENV PYTHONPATH /opt/src
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]