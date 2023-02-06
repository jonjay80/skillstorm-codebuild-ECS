FROM public.ecr.aws/sam/build-python3.8:latest
# set a directory for the app
WORKDIR /usr/src/app
# copy all the files to the container
COPY . .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# tell the port number the container should expose
EXPOSE 5000
# run the command
CMD ["python", "./app.py"]
