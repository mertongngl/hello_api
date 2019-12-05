FROM python:3.5

ADD . /home/test

WORKDIR /home/test

RUN useradd -rm -d /home/test -s /bin/bash -u 1000 test

RUN chown -R test /home/test

RUN pip install -r requirements.txt

RUN export FLASK_APP=app.py

ENTRYPOINT [ "python", "app.py" ]
