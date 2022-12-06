# msSQL-Flask
In this project, my groupmates and I, created a relational database schema for a complex application. we also created a web UI to show some of the capabilities of the App.


The App has three types of users: Educational Institutions, Developers, and Companies. Developers could enroll in classes offered by educational institutions and they might apply for job oppurtunities offered by companies. Companies can hold competitions and developers can compete in them. Lots of functionalities like: registering at classes, submitting tasks, applying for jobs, creating competitions and posting job offers are implemented.

# How to run the app
Database server will run in a docker container and there is no need to install it on your machine. So you need to install docker in your machine.

Create SQL server, required tables and inserting some data:
```
cd db
./configure
```

Running the Flask webserver
```
cd ..
python3 -m flask run
```

Here is the data diagram of the App:
<img src="https://github.com/itsAliSali/msSQL-Flask/blob/main/DB_datadiagram.png" height="670">

A demo web App to show some of the functionalities: 
<img src="https://github.com/itsAliSali/msSQL-Flask/blob/main/web-app.png" height="500">


Note: 
* This code is prone to sql injection and many other security leaks. Password are kept as plane text. And many other bad practices! This project was done for educational purposes only.



