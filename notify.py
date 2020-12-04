#!/bin/env python

import time
import firebase_admin
from firebase_admin import credentials, messaging, db


cred = credentials.Certificate('/home/aasumitro/Documents/Projects/cici/python/firebase.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<project-name>.firebaseio.com/'
})


def push_notify(name, url) :
    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.
    registration_tokens = []

    # This will load available registration token stored on
    # Realtime Database and will append on empty array
    dbRef = db.reference("users")
    dataSnapshot = dbRef.get()
    for key, val in dataSnapshot.items():
        registration_tokens.append(val['token'])

    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        # notification = messaging.Notification(
        #     title = "Bajaga",
        #     body = "Terdeteksi orang tak dikenal",
        #     image = url
        # ),
        android = messaging.AndroidConfig(
            notification = messaging.AndroidNotification(
                title = "Just Test",
                body = "Hello from firebase notification",
                image = url,
                # click_action = "DetailScreenActivity",
            ),
            priority = "high",
            data = {'url': url, 'name': name},
        ),
        data = {'url': url, 'name': name},
        tokens = registration_tokens,
    )

    # Send a message to the device corresponding
    # to the provided registration token.
    response = messaging.send_multicast(message, app=default_app)
    if response.failure_count > 0 :
        responses = response.responses
        failed_tokens = []
        for idx, resp in enumerate(responses):
            if not resp.success:
                failed_tokens.append(registration_tokens[idx])

    # Failed response token
    # print("list of failures token: {0}".format(failed_tokens))
    # Response is a message ID string.
    print('Successfully sent message:', response)


while True:
    push_notify("Gambar Test", "https://cdn.searchenginejournal.com/wp-content/uploads/2019/12/how-to-execute-a-link-conversion-strategy-5df792498b991-760x400.webp")
    time.sleep(10)





