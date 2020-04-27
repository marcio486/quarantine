FROM ubuntu
USER root
RUN apt-get update -yq && apt-get install -yqq \git \python3 \python3-pip
RUN pip3 install flask
RUN pip3 install pandas
RUN pip3 install sqlalchemy
RUN pip3 install psycopg2-binary
COPY . /opt/source-code
ENTRYPOINT python3 /opt/source-code/webapp2.py
