FROM python:3

ADD start_service.py /
ADD init_db.py /

RUN pip3 install pyzmq
RUN apt-get update && apt-get install -y cython3
RUN python3 init_db.py

EXPOSE 5555

ENTRYPOINT [ "python3", "start_service.py" ]
