FROM python
RUN pip install flask flask-restx mongoengine && \
    mkdir /worky

WORKDIR /worky

COPY . .

CMD python app.py
