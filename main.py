#!/bin/env python

import time
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('/home/aasumitro/Documents/Projects/cici/python/firebase.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<project-name>.firebaseio.com/'
})

def watch_event():
    dbRef = db.reference("testpin")
    status = dbRef.child("raspi_server_1").child("status")
    if status.get() :
        print(status.get()) # print out latest status replace with (turn on light)
        time.sleep(10) # delay for 10s
        status.set(False) # set status value
        print(status.get()) # print out latest status after update replace with (turn off light)

    # current status (just for test)
    print(status.get())
    status.set(True)

while True:
    watch_event()
