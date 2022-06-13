FROM python:3.9

ENV VIRTUAL_ENV=/opt/fastvenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv $VIRTUAL_ENV
RUN pip3 install -r requirements.txt
RUN mkdir src

COPY main.py .
COPY src ./src

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000" ]

EXPOSE 5000/tcp