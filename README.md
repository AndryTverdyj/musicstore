# The Music store project.
==========================

Simple storage to help store, search and manage Music works.

1 Installation
---------------
First you need to clone this repository.
>git clone https://github.com/AndryTverdyj/musicstore.git

2 Usage
--------

Move on to directory musicstore

and run this project using docker

>docker-compose up --build

If you need to run the django commands ( for loading .csv files ),
you can do it this way

>docker-compose run backend python manage.py <command_name>

3 Uploading .csv files
-----------------------
This project runs localy. Open http://localhost in your browser.
As you can see here is the form for file uploading. Upload your .csv file (only .csv-format)
and run next command

>docker-compose run backend python manage.py load_music_works_csv <your_file_name>

then you can see data below.

You can search additional information by ISWC using search-form on SPA.

4 Backend API
--------------

Backend API includes endpoint for file uploading :
> http://localhost/api/upload/ -

and two endpoints for reading music works
first one :
> http://localhost/api/musicworks/

GET request - return MusicWork objects list
you can send additionalargument iswc as a get paramenter.
> http://localhost/api/musicworks/?iswc=<some_iswc>

it helps to find MusicWork object by iswc.

second one:
> http://localhost/api/musicworks/<id>/

GET request - return MusicWork object by ID !!! Not used in this case
