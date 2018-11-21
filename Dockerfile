FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app/

ENV ENVIRONMENT production

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt
COPY model.pkl /app/

COPY main.py __init__.py predictive_model.py documentation.py /app/