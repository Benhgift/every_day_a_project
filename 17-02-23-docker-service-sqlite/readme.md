#Silly Python Dockerized Service

## Quickstart
To run a service that holds records of movie names and years run this:

    sudo docker build -t silly-service .
    sudo docker run --net=host --rm -P silly-service

Now that the service is running, run this from another terminal: 

    python3 test_service.py

That will open a prompt. Type `get` to read the database and type `put movie_name_here year_here` to insert into the database.



