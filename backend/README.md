# Backend Instructions

*[Local Install](#-Local-Install)
*[Online*TBD*](#-Online*TBD*)
*[Issues](#-Issues)

## Local Install
To run the backend locally you will first need to clone the git repo onto your machine.
i.e (git clone https://github.com/thegolriz/WebSite-project-ballc.git)
Once this is done ensure all needed files came over:
- Docker
- Poetry
Once you have that you will need to run a couple things to ensure everything is properly loaded.

**env**
Note all the information comes from a .env file,
this should be put in the root directory, to run it you will need to make one,
looking at the dockercompose will help set up all that is required for the database.
There is also a .env_example, update the information inside to match what is required then make it yours via:
mv .env_example .env

**Docker Install**
Note that the docker compose file is in the root directory, make sure you are in there NOT the backend directory.
Once there run docker compose up -d, it is not recommended to compose the .dev version. If you wish to please run it via:
docker compose -f docker-compose.dev.yml up -d (Note as of 09/23/25 the .dev compose is not finished). Once you run Docker compose
it will also run poetry and install all the dependencies needed. At this point you should have a docker container running, check with
docker ps, if you don't see one, ensure you have the docker daemon installed and run docker ps -a to check if the container was made but not
ran. If you still have issues please go down to the issues page to see how to submit an issue.

#### Start server
To start the server and send api requests, ensure you are in the backend folder, top level then:
**Poetry run flask run**...You should now see your local host, to make sure its working open a browser and go to localhost/api/hello.
http://127.0.0.1:5000/api/hello 
you should recieve a page that shows **{"message":"Hello from the API"}** 
### Running via postman
To run via postman, ensure you have postman agent installed and running then, go to [postman](https://www.postman.com/)

| API Endpoint | Type       | How to run |
|--------------|------------|------------|
| /hello       | GET        | Hit send   |
| /users       | GET        | Hit send   |
| /logout      | POST/DELETE| Hit send   |
| /signup      | POST       | Body -> Raw<br> email(unique)<br> first name <br> last name<br> password( len > 7) <br> [Example Signup](#-Example-Signup)|






#### Example Signup
{
    "email":"test@test.test",
    "firstName":"tester",
    "lastName":"test",
    "password":"12345678"
}
Passwords are hashed then put into database for data protection.

