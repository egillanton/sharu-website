<h1 align="center">
Website - Student Hackathon Association at Reykjavik University
</h1>

<img src="https://user-images.githubusercontent.com/9976294/73139773-6cd71480-4069-11ea-8f1e-ae266dafd720.png" alt="Screenshot" align="center"/>

<h2 align="center">
<a href="https://sharu-2020.herokuapp.com/">www.nhvhr.ru.is</a>
</h2>


## Setup

Make sure to have Python 3.6 or newer, and pip installed.

### Get virtualenv

```bash
$ pip install virtualenv
```

### Create a virtual enviroment

Make sure to create a Python3 instead of Python2 enviroment by refrencing its binaries.
```bash
$ which python3
/usr/bin/python3
```

You can use any name you want, we will use "venv".
```bash
$ virtualenv -p /usr/bin/python3  venv
```

### Activate enviroment

```bash
$ . venv/bin/activate
```

Now you have activated your virual enviroment and your teminal should display its name as so:
```bash
$(venv)
```

### Install requried packages
```bash
$(venv) pip3 install -r requirements.txt  
```

### Run The Application

```bash
$(venv) flask run
```

You’ll see output similar to this:

```bash
Serving Flask app "app"
Environment: development
Debug mode: on
Running on http://127.0.0.1:5000/
Restarting with stat
Debugger is active!
Debugger PIN: 298-204-950
```

Open the link in your browser.

### Push to Heroku
Make sure you have installed Heroku CLI, and have authentication to the Heroku project.

Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
**Login into Heroku**
```bash
$ heroku login
```

**Clone the repository**
Use Git to clone heroku-app's source code to your local machine.


```bash
$ heroku git:clone -a <heroku-app>
$ cd <heroku-app>
```

**Deploy your changes**
Make some changes to the code you just cloned and deploy them to Heroku using Git.

```bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

## License
This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.

<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>