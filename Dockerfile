From python:3.8
WORKDIR /APP
COPY . . 
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]