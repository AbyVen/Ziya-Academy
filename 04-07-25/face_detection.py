import cv2
from pync import Notifier

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

face_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    
    for (x, y, w, h) in faces:
        if not face_detected:
            Notifier.notify("Face detected!", title="Face Detection")
            face_detected = True
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if len(faces) == 0:
        face_detected = False

    
    cv2.imshow('Face Detection', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
