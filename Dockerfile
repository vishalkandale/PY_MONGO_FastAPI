FROM python:3.7

RUN pip install fastapi uvicorn pymongo

EXPOSE 8000

COPY ./PY_MONGO /app

CMD ["uvicorn", "app.index:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
