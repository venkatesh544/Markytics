"# Markytics" 
steps:
The first thing to do is to clone the repository:

$ git clone https://github.com/master-app-v2.git
$ cd master-app-v2

$ virtualenv --no-site-packages env
$ source env/bin/activate

If your project is already in an existing python virtualenv first install django by running

$ pip install django

Then install the dependencies:

$(env)$ pip install -r requirements.txt

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

if you want run your project on terminal you should give some commend like this

$(env)$ cd project
$(env)$ python manage.py runserver

after run your project successful then it had proveded one url like this

And navigate to http://127.0.0.1:8000/.

if you want to go corrcet page just click url or just copy the url link and open a browser past url that it.


Then simply apply the migrations:

$ python manage.py migrate
You can now run the development server:

$ python manage.py runserver
