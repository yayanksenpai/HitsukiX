# set base image (host OS)
FROM python:3.9-slim-buster

# set the working directory in the container
WORKDIR /hitsuki/

RUN apt-get -qq update && apt-get -qq upgrade -y
RUN apt-get -qq install -y --no-install-recommends \
    wget \
    curl \
    git \
    gnupg2 

# Copy directory and install dependencies
COPY . /hitsuki
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# command to run on container start
CMD ["bash","start.sh"]
