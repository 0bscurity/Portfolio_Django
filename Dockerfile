FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y --no-install-recommends tzdata
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

RUN apt-get install g++ unixodbc-dev -y
RUN apt-get install -y python3-pip


WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY / /code

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

#ENTRYPOINT ["tail", "-f", "/dev/null"]
