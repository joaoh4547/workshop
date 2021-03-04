FROM python:3.8
WORKDIR app/
COPY ./requirements.txt /app
COPY ./ml /app/ml
COPY ./data /app/data
COPY ./utils /app/utils
COPY ./main.py /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader -d $HOME/nltk_data stopwords

