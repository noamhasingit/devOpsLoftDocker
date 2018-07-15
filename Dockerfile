FROM python:3
ADD application.py /
ADD requirements.txt /
ADD static /static
ADD templates /templates
ADD bootstrap.sh / 
ADD config.py /
ADD data /data
ADD mod_auth /mod_auth
ADD config.py /
RUN pip install --upgrade setuptools
RUN pip install -r /requirements.txt
CMD [ "python3", "./application.py" ]


