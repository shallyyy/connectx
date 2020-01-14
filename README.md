# connect-five
Connect Five

## Description

This repo holds the files a connect-five game based in Java. It allows a user to register an account, login, view their stats and scoreboard, and most importantly play connect-5 against another user of their choosing. 

It also contains the Flask web server written in Python that implements a basic RestAPI.

Finally, it holds a PostgreSQL file that creates the appropriate tables and keys in which the RestAPI communicates with. 

### Assumptions
+ User's data such as past games and current games will be held in the database. 
+ Many pairs of users can play independently 


### Java
The game is mostly within a connectx object, of which main creates an instance and runs the game upon launch. The connectx communicates data to the PostRequestHandler and GetRequestHandler, which then make Rest calls to the Flask Webserver that is being hosted locally. The Java holds very little logic and only displays and returns what the Rest API delivers. 

### Flask Webservice and RestAPI
The flask webservice runs locally on port 5000. The RestAPI was designed to handle all the logic of the game, and allow for any Architecture to communicate with it, allowing cross-platform support. For example, if a PHP application of connect five was created it could communicate with a Java or NodeJS version easily. 

I choose Flask due to my experience in creating a RestAPI for a project in my System Analysis and Design project. 

### PostgresSQL
The database is hosted on port 5432. I choose Postgres for its extensibility and past experiences with it. The schema has three tables:
Users
Games
Moves

The game board, 6x9, is made up of moves from the table Moves.  Games hold the game state, current turn and finally players. 

### Tests
Junit tests can be found in this directory:
ConnectX\java\src\com\ConnectX\Tests

## Deploying
Unfortunately, the problem with creating a more scalable and extensible game is the cost of deploying the games server and database. 
NOTE: I have provided images of gameplay. If it becomes too difficult or tedious to deploy I can either record the gameplay, server and database in action or even screen call my monitor with the game in action via Skype! Apologies for this. Also, feel free to contact me for help on deployment!

If you do want to deploy the code these are the steps:

### Step 1 - Host the Postgres Database
Luckily PostgreSQL has great documentation for installing and getting Postgres up and running. Follow the steps in the link below:
https://www.postgresqltutorial.com/install-postgresql/

Once the database is set up and running you can now run the Database.sql in the Tables Schema that comes preloaded in the Postgres database. If all goes well, you should have a schema and database similar to this:

![alt text](https://github.com/shallyyy/connectx/blob/master/Images/database.png "Database.png")

### Step 2 - Setting up the server
Firstly the server runs on Python 3.7, although earlier versions would likely suffice. Simply go into your command line in the root RestAPi folder and run the following command

Python RestAPI.py

You should receive a message stating it is listening on port 5000 and debugging mode is enabled. 

### Step 3 - Java
Finally is running the Java Program. The IDE I used was IntelliJ. It is likely the simplest way to run the code, and to do so is by opening the connectx directory as a Java Project and clicking run on Main. I used Java 11 and Java 8 will not work. 

If IntelliJ is not possible,  head over to ConnectX\java\out\production\java\com\company and run:
Java Main

This will likely have the same outcome, although perhaps with some debugging. 

## Images
Here are some of the images of the game working:


### Example game
![alt text](https://github.com/shallyyy/connectx/blob/master/Images/Example%20Game.png "Game.png")

### Open games list
![alt text](https://github.com/shallyyy/connectx/blob/master/Images/Logging%20in%20and%20Open%20Games%20menu.png "OpenGames.png")


### Scoreboard
![alt text](https://github.com/shallyyy/connectx/blob/master/Images/Scoreboard%20Menu.png "Scoreboard.png")


### Stats
![alt text](https://github.com/shallyyy/connectx/blob/master/Images/Statistics%20Menu.png "Stats.png")



