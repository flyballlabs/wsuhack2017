FROM alpine
RUN apk add --update git python3 
RUN git clone http://git.dopensource.com/tmoore/wsu-hackathon
CMD cd wsu-hackathon/server-api/am
RUN pip3 install -r wsu-hackathon/server-api/am/requirements.txt
CMD ["python3", "wsu-hackathon/server-api/am/rest_am_server.py"]
