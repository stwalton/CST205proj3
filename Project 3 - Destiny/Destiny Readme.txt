Fernando Madrigal
Juan Zuniga
Steven Walton
CST 205 Group 253
5-16-2017

GitHub: https://github.com/stwalton/CST205proj3
Trello: https://trello.com/b/QidpAtIU/cst-205-team-253-project-3

This project is written in Python 2

Wrappers: 
PyQt4
Pyaudio
ffmpeg
pydub
numpy
scipy
matplotlib
MySQLdb 
Also used Xampp to locally store the SQL database.

This application is also using Dejavu,code developed by Will Drevo, and is open soure. We are specifically using his program for his algorithms for fingerprinting and finding music off the database. The files needed to run this application is already provided, but reconmend checking his project out. The websites are:
http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/
https://github.com/worldveil/dejavu  

Once you have all the wrappers and database set up, you will need to go in the main file (Destiny.py) to set up the config file for the database. It should look something like this: 

config = {
        "database": {
                "host": "127.0.0.1:3306",
                "user": "STEVEN",
                "passwd": "1234",
                "db": "TESTDB",
                }
        }


Change the username, password, and database(db) to what your settings are, and you should be able to start fingerprinting. Once you fire up the program, you are presented with three different options, fingerprint, search by file, and search by microphone. If you haven't started to fingerprint, I woud highly reconmend do that first.This option will bring up a file explorer window which you can select the file to fingerprint. Once you have a database going, you can begin searching for songs. If you chose file, you are presented with a file explorer which you can select your file that you would like to search from. The last option, the microphone is fairly simple. Hit the button and the program immediaely starts recording and should listen for about 15 seconds.  