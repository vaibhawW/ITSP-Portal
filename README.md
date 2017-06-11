# STAB-ITSP Portal #
### What is this repository for? ###
This is the portal for IITB|STAB ITSP 2017
* Version	:	1.0
### How do I get set up? ###
* Summary 
    1.	Copy project
	2.	Update settings
	3.	Migrate
	4.	Create Passwords
* Setps followed:
	1. 	Creating project (optional)
		  1.1.	in terminal type **django-admin startproject WEBSITENAME**
		  1.2	change to the directory of WEBSITENAME **cd WEBSITENAME**
		*I will be refering to this WEBSITENAME directory as root directory from now on*
	2. 	Copy paste the ITSP folder from downloaded folder to root directory.
	3.	In root directory, open settings.py
		Here are the configurations you need to do.
		  3.1.	in INSTALLED_APP add ITSP
		  3.2.	change DATABASE settings as we are going to be using database to manage data.
		  3.3.	add following line of codes in settings.py at the bottom*.
		
			MEDIA_ROOT = BASE_DIR + '/ITSP/static/media/'
			MEDIA_URL = '/static/media/'
			APPEND_SLASH = True
	4.	Update your urls.py in *root directory/root directory* to include urls.py of ITSP app.
	5.	in terminal type
			
			pip install multiselectfield
		or

			sudo pip install multiselectfield
	6.	makemigrations and migrate...

			python manage.py makemigrations
			python manage.py migrate
	7.	run django shell and create user-passwords.

			python manage.py shell
			imoprt passmanager
			passsmanager.generate(NUMBEROFUSERS)
	8.	you are all set and ready to go...

* Dependencies

    1.	python 2.7
    2.	pip
    3.	multiselectfield(django-python)

* Database configuration

    1.	I did tests on mysql

* Deployment instructions

    1.	(to be updated)

### Contribution guidelines ###

* Writing tests
    I have tried to keep it as simple as possible. I have no idea how to write tests, so I have no comments on it. I know that you can write tests. If intrested, please write some. :) 
    And I promise I am going to learn it soon and update this.

* Code review
    You are more than invited to drop a review. I am learning, and would be greateful if someone has advices for me to improve my skills.

### Who do I talk to? ###

* We are the student-tech community of IITB. You can go to http://tech-iitb.org for more contact details regarding this project. 
* Also, if you want to contact me, you can leave a message for me here mail to me at vaibhawofficial@gmail.com
