FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app/

COPY requirements.txt /app/
COPY model.pkl /app/
RUN pip install -r ./requirements.txt

COPY main.py __init__.py predictive_model.py /app/