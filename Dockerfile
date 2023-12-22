FROM python:3.10

RUN mkdir /calculator_bot

WORKDIR /calculator_bot

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY bot ./bot

CMD ["python", "-m", "bot"]