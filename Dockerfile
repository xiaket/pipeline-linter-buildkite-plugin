FROM python:alpine

COPY hooks/requirements.txt hooks/linter.py /

RUN pip3 install -q --disable-pip-version-check -r /requirements.txt

ENTRYPOINT ["python3", "/linter.py"]
