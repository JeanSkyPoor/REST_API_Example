FROM python

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "test_api.py"]