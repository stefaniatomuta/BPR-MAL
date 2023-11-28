FROM python:3.11

WORKDIR /BPR-MAL/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt

CMD ["python", "./main.py"]