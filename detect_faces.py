import datetime
from network import Network
import cv2
from face_rec import classify_face

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
            n.send(data)

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