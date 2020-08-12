FROM python:3.7.6

ADD requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip3 install https://download.pytorch.org/whl/cpu/torch-1.6.0%2Bcpu-cp37-cp37m-linux_x86_64.whl

ADD . /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
