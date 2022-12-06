FROM python:latest
COPY  . .
RUN pip install -r requirements.txt 
CMD [ "python", "./pasar_a_json.py" ]
CMD [ "cat" , "leaks.json" ]