<<<<<<< Updated upstream
# We will use Ubuntu for our image
FROM ubuntu
# Updating Ubuntu packages
RUN apt-get update && yes|apt-get upgrade
# Adding wget and bzip2
RUN apt-get install -y wget bzip2
# Anaconda installing
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN bash Anaconda3-5.0.1-Linux-x86_64.sh -b
RUN rm Anaconda3-5.0.1-Linux-x86_64.sh
# Set path to conda
ENV PATH /root/anaconda3/bin:$PATH
# Updating Anaconda packages

#RUN apt-get -y  install gnupg2
RUN conda install pip
RUN pip freeze > require.txt
RUN pip install -r require.txt

# install psycopg2 dependencies


RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

