FROM python
RUN pip install scikit-learn==1.0.2 spacy && \
    python -m spacy download en_core_web_sm && \
    mkdir /worky

WORKDIR /worky

COPY . .
COPY ../model.py .
COPY ../trained_model.pkl .
COPY ../trained_vect.pkl .

CMD python worker.py
