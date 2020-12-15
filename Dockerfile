FROM python:3.7.6-buster
MAINTAINER python_student

RUN mkdir /master_mind_project/
COPY ./requirements.txt /master_mind_project/
COPY ./master_mind.py /master_mind_project/
COPY ./test_master_mind.py /master_mind_project/

RUN pip install --upgrade pip
RUN pip install -e
RUN pip3 INSTALL -r /master_mind_project/requirements.txt

WORKDIR /master_mind_project/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
