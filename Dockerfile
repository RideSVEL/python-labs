FROM python:3
WORKDIR /usr/src/app/
RUN pip install beautifulsoup4
RUN pip install lxml
RUN pip install numpy
RUN pip install matplotlib
RUN pip install pandas
RUN pip install plotly
RUN pip install requests
COPY lab16 /usr/src/app/
RUN cd /usr/src/app/
CMD ["python" ,"script.py" ,"java"]