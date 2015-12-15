# start with a base image
FROM ubuntu:14.04

# install dependencies
RUN apt-get update
RUN apt-get install -y autoconf automake libtool
RUN apt-get install -y libpng12-dev
RUN apt-get install -y libjpeg62-dev
RUN apt-get install -y g++
RUN apt-get install -y libtiff4-dev
RUN apt-get install -y libopencv-dev libtesseract-dev
RUN apt-get install -y git
RUN apt-get install -y cmake
RUN apt-get install -y build-essential
RUN apt-get install -y libleptonica-dev
RUN apt-get install -y liblog4cplus-dev
RUN apt-get install -y libcurl3-dev
RUN apt-get install -y python2.7-dev
RUN apt-get install -y tk8.5 tcl8.5 tk8.5-dev tcl8.5-dev
RUN apt-get build-dep -y python-imaging --fix-missing
RUN apt-get install -y imagemagick
RUN apt-get install -y wget
RUN apt-get install -y python python-pip

# build leptonica
RUN wget http://www.leptonica.org/source/leptonica-1.70.tar.gz
RUN tar -zxvf leptonica-1.70.tar.gz
WORKDIR leptonica-1.70/
RUN ./autobuild
RUN ./configure
RUN make
RUN make install
RUN ldconfig
WORKDIR /
RUN ls

RUN apt-get install -y tesseract-ocr

ADD requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /code/
EXPOSE 5000
