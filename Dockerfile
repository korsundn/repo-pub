FROM python:3.8
RUN pip install -U aiogram
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
CMD ["python", "echo_bot.py"]
