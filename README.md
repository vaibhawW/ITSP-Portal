# STAB-ITSP Portal #


Prerequesites:
	
	settings.py should be configured to use some database.

Setps followed:

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
		
		**MEDIA_ROOT = BASE_DIR + '/ITSP/static/media/'**
		**MEDIA_URL = '/static/media/'**
		**APPEND_SLASH = True**

4.	Update your urls.py in *root directory/root directory* to include urls.py of ITSP app.

5.	in terminal type
		**pip install multiselectfield**
		or
		**sudo pip install multiselectfield**

6.	makemigrations and migrate...
		**python manage.py makemigrations**
		**python manage.py migrate**

7.	run django shell and create user-passwords. 
		**python manage.py shell**
		**imoprt passmanager**
		**passsmanager.generate(NUMBEROFUSERS)**

8.	you are all set and ready to go...


### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)


Customization Steps:
Add clubs on line 3 in models.py

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
