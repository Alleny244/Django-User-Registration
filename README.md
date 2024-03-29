# Django-User-Registration
 User login and register system implementation in django  
![](https://img.shields.io/github/repo-size/Alleny244/Django-User-Registration.svg?label=Repo%20size&style=flat-square)&nbsp;![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)&nbsp;


Django is an open-source python web framework used for rapid development, pragmatic, maintainable, clean design, and secures websites. A web application framework is a toolkit of all components need for application development. The main goal of the Django framework is to allow developers to focus on components of the application that are new instead of spending time on already developed components. Django is fully featured than many other frameworks on the market. It takes care of a lot of hassle involved in the web development; enables users to focus on developing components needed for their application.

Django by default provides an authentication system configuration. User objects are the core of the authentication system.today we will implement Django’s authentication system.

django based login,logout and register system [django docs on auth system](https://docs.djangoproject.com/en/2.2/topics/auth/default/)

---

learn how to make on geeksforgeeks : https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/


![beginner-friendly](https://img.shields.io/badge/beginner%20friendly-django%20project%20-green)
---


## Virtualenv & Dependencies

create a virtualenv and run requirements.txt<br/>
<b>virtualenv</b>

<pre>pip install virtualenv</pre>

<b> what is virtual environment ? </b><br/>
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.
<br/>
<a href="https://www.geeksforgeeks.org/python-virtual-environment/" >read more... </a>

to run requirements.txt

<pre>$ pip install -r requirements.txt</pre>

here <b>env/</b> folder contains all dependencies

## Running locally

<ol>
  <li>
      clone repository 
      <pre>$ git clone https://github.com/itsvinayak/user_login_and_register.git</pre>
  </li>
  <li>
     make database settings and connect it to your local database 
    <pre>$ cd ./user_login_and_register/project </pre>
    open <b>settings.py</b> file
    <pre>
                DATABASES = {
            "default": {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'Auth',
              'USER': 'postgres',
              'PASSWORD': '1234',
              'HOST': 'localhost'
            }
        }
   </pre>
   set this part according to needs.
  </li>
  <li>
    run migrations 
    <pre>$ python manage.py migrate</pre>
  </li>
  <li>
    now, runserver 
    <pre>$ python manage.py runserver</pre>
  </li>
 </ol>

![alt text](https://github.com/itsvinayak/user_login_and_register/blob/master/Screenshot%20from%202019-07-23%2007-26-47.png)


---

