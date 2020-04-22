FROM ubuntu
USER root
RUN apt-get update -yq && apt-get install -yqq \git \python3 \python3-pip
RUN pip3 install flask
COPY . /opt/source-code
ENTRYPOINT FLASK_APP=/opt/source-code/webapp.py flask run
