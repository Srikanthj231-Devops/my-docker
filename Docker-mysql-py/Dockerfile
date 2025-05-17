FROM python

WORKDIR /my-app

COPY ./my-sql.py .

RUN pip install psycopg2

CMD ["python3","my-sql.py"]