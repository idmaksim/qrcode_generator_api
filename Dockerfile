FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN rm -r .venv

CMD ["uvicorn", "src.main:app", "--port", "8080"]
