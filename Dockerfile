# set base image (host OS)
FROM python:3.9-alpine

# # set the working directory in the container
WORKDIR /bot

RUN pip install pipenv

# copy the dependencies file to the working directory
COPY Pipfile* ./

# install dependencies
RUN pipenv install

# copy the content of the local src directory to the working directory
COPY . .

RUN pipenv install --system --deploy --ignore-pipfile

# command to run on container start
CMD [ "python", "main.py" ] 