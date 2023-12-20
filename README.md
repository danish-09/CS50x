# GETAWAY IN KASHMIR
#### Video Demo: [Youtube video link](https://www.youtube.com/watch?v=GMELlgr3rbI)
#### Description:
GETAWAY IN KASHMIR web application using python, Flask, SQL.

**GETAWAY IN KASHMIR is my final project of [CS50x](https://www.edx.org/learn/computer-science/harvard-university-cs50-s-introduction-to-computer-science), Harvard University's introduction to the intellectual enterprises of computer science and the art of programming**.

I believe connections matter and this is the exactly what this webapp tries to do, it tries to connect people no matter where they come from cross cutting cultural, regional differences.
This web application aims to connect travelers in Kashmir.
First time users have to register using their username and password using the register link on the navbar, after the username and the password are properly validated against stored information in the database then the user can login using using his username and password.
After the user has logged in he can see the homepage of the web application the homepage has information and some beautiful pictures of Kashmir giving the user a glimpse of this place called Heaven on Earth .
The user can also click on the places link on top of the navbar which will show the user the most popular places in Kashmir from a tourist's standpoint.
The about link on the navbar provides a small glimpse into what the developer aims to achieve
with this web application.
The user can then click on the visit link on the navbar which will render a form , which the user will fill out ,this form contains the name, place of visit, date of visit and the social contact fields. Once the form is submitted the form data is inserted into the database and a table containing the information related to other travelers who are going to visit the same places on the same dates is rendered.This table lists their user id's along with the social media sites so that these people can then be contacted by other fellow travelers leading to a connection.


**PROJECT FILES**

* static
  - images
  - styles.css
* templates
  - about
  - apology
  - home
  - layout
  - login
  - places
  - register
  - visit
  - visitors
* app.py
* helpers.py
* visitors.db
* README.md


**WORKING**

1. register
   - takes in username
   - takes in password
   - performs required validation
   - inserts data into users1 table

2. login
   - takes in username
   - takes in password
   - performs required validation

3. layout
   - Provides the layout of webpage extended to all other web pages
   - contains the navbar

4. home
   - serves as the homepage

5. about
   - gives brief information about web application

6. apology
   - contains an animated meme

7. places
   - list some famous places in kashmir

8. visit
   - provides a form using which user submits information about the places he/she wants to visit and the date of his visit

9. visitors
   - provides a table which contains information about people who are visiting the same place on the same data as the logged in user

10. app.py
    - configures routing
    - handles the backend logic of web application

11. helpers.py
    - provides some helpful functions

12. visitors.db
    - database containing the different tables

**Languages used**

* HTML
* CSS
* Python

**Stack**

* SQL
* Flask
* Jinja


