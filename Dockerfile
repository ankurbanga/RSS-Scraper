FROM python:3
WORKDIR /scrape
ADD . /scrape
RUN pip install beautifulsoup4
RUN pip install lxml
RUN pip install requests
CMD ["python3","./webscraperss.py"]


