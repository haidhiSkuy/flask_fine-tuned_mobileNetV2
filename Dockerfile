FROM python:3 

WORKDIR /usr/src/app 
COPY . ./
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
EXPOSE 5000
CMD ["python", "./app.py"]