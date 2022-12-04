FROM python:3.6.8

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m pip install -r requirements.txt

EXPOSE 8501

COPY . /app

RUN sh setup.sh

CMD streamlit run Apple_Foliar_Disease_Detection.py --server.port $PORT