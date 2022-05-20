## Athenians Institute Reg
Course Registration, update and Review
## Built By [Andy, Elvis & Lillian](https://github.com/Andy3643/Student-Portal)
You can view the site at: [ ATHENIANS COURSE REG](https://pitches-posts.herokuapp.com/ytidcdytic)

## Description
Due to having a large number of students, institutions of higher learning often face the challenge of ineffective student results and course management as reported by increased cases of 'missing marks' and students not registering for exams.  due to these challenges, we want to create a system that will help students register for courses online to help in data management.
[Go Back to the top](#Athenians-Institute-Reg)
## Courses
The user would like to.... :
*  View the list of courses on the site
*  enroll on courses
*  View the most recent courses
*  An email alert when a new registration is made by joining a course.
* See random courses on the site
* enquire
* call and send feedback
The writer would like to... :
* see random courses on the site
* sign in to the course registration.
* create an enrollment from the application.
* delete course / unenroll.
* update or delete courses I have enrolled.
[Go Back to the top](#Athenians-Institute-Reg)
## Behaviour Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View List of courses | Click on register | Taken to the registration form | Click on `enroll` | Taken to where you can enroll | Signs In/ Signs Up |
| Click on `Click sign up` | If logged in, display form to add a course| Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
| Click on Sign Out | Redirects to the home page | Signs user out |
[Go Back to the top](#Athenians-Institute-Reg)
## Getting started
### Prerequisites
* python3.8
* virtual environment
* pip
* Markfile
[Go Back to the top](#Athenians-Institute-Reg)
### Cloning
* In your terminal:
        git clone https://github.com/Andy3643/Student-Portal
        cd Students Portal
[Go Back to the top](#Athenians-Institute-Reg)
## Running the Application
* Install virtual environment using `$ python3.8 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Creating the virtual environment
        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python
* Installing Flask and other Modules
        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-Bootstrap
        $ python3.8 -m pip install Flask-Script
* Install all the dependencies from the requirements.txt file by running `python3.8 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:
        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>
* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:
        chmod a+x start.sh
        ./start.sh
[Go Back to[Go Back to the top](#Athenians-Institute-Reg)
## Testing the Application
* To run the tests for the class file:
        python3.8 manage.py server
[Go Back to the top](#Athenians-Institute-Reg)
## Built With
* [Python3.8](https://docs.python.org/3/)
* Flask
* Boostrap
* HTML
* CSS
## Platforms
* slack
* github projects
* figma
* google meet
[Go Back to the top](#Athenians-Institute-Reg)
## License
[MIT LICENCE](https://github.com/DynastyElvis/Personal-Blog/blob/main/LICENSE)
Copyright (c) 2022 K. E. Rono
Copyright (c) 2022 L. MUITA
Copyright (c) 2022 J. MULONGA
[Go Back to the top](#Athenians-Institute-Reg)
## Known Bugs
No Known Bugs.
## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :kipkemoilvs@gmail.com
## Authors Info
LinkedIn - [KIPKEMOI ELVIS RONO](https://www.linkedin.com/in/elvis-rono-aa3548209/)
LinkedIn - [JOSHUA MULONGA](https://www.linkedin.com/in/elvis-rono-aa3548209/)
LinkedIn - [LILLIAN MUITA](https://www.linkedin.com/in/elvis-rono-aa3548209/)
[Go Back to the top](#Athenians-Institute-Reg)
