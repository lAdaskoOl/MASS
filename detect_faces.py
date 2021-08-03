import datetime
from network import Network
import cv2
import os
from face_rec import classify_face
from email.message import EmailMessage
import imghdr
import smtplib

def sendEmail():
    # Create the container email message.
    msg = EmailMessage()
    msg['Subject'] = 'Our family reunion'
    # me == the sender's email address
    # family = the list of all recipients' email addresses
    msg['From'] = 'some email'
    msg['To'] = 'your email'
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    files = os.listdir('images/')
    with open(files[0], 'rb') as fp:
        img_data = fp.read()

    msg.add_attachment(img_data, maintype='image',
                       subtype=imghdr.what(None, img_data))

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)
    print("Email sent...")

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

n = Network()

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

    if not len(faces) == 0:
        name = classify_face(img)
        if "Unknown" in name:
            date = datetime.datetime.now()
            file = "images/" + str(date).replace(' ', '_').replace(':', '_')[0: 19] + ".jpg"
            cv2.imwrite(file, img)
            #TODO: notify the user about the detected faces
            data = "write Face detected on " + str(date).replace(' ', '_').replace(':', '_')[0: 19]
            info = n.send(data)
            if info["number"] == 1: # if user is not connected to the server
                sendEmail()

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    # Comment this line so the window does not show up
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()