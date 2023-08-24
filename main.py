import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils import send_email_detection,get_coordinate_ip,send_emails_detection




cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://dgprojectfacedetection-default-rtdb.firebaseio.com/",
    'storageBucket':"dgprojectfacedetection.appspot.com"
})

 

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, targetIds = encodeListKnownWithIds
# print(targetIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []
targetInfo = None

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    # imgS = cv2.resize(img, (int(img.shape[1] * 0.25), int(img.shape[0] * 0.25)))
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)
            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

            if matches[matchIndex]:
                print("Known Face Detected")
                id = targetIds[matchIndex]
                targetInfo = db.reference(f'Targets/{id}').get()
                if targetInfo is not None:
                    name = targetInfo['name'].upper()
                    infos = targetInfo['infos']
                    status = targetInfo['status']
                    option = targetInfo['option']

                    recipient_email='woosiascharles1@gmail.com'
                    recipient_emails=['woosiascharles1@gmail.com','pyp0859@gmail.com']


                # print(targetIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                # print("bbox", bbox)
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                cv2.putText(imgBackground, name, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                
                if status == 'bandit'.capitalize():
                    subject = "Face detection"
                    message = "This is an alert: we have detected a face \nlocation{}\n\n  \nname: {}\nstatus: {}\noption: {}\ninfo: {}\n".format(get_coordinate_ip(),name, status, option, infos)
                    # message = "This an alert we have detected a face in your house \n name:$`{}`\n status:$`{}`\n option:$`{}`\n info:$`{}`\n".format(s=name,s=status,s=option,s=info)
                    send_emails_detection(recipient_emails, message,subject)
                    # send_email_detection(recipient_email, message,subject)
                else:
                    print("No alert")


            else:
                print("Unknown Face")
                name = "Unknown Face"
                name = "Unknown"
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = (55 + x1, 162 + y1, x2 - x1, y2 - y1)

                # Dessiner un rectangle rouge
                cv2.rectangle(imgBackground, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 0, 255), 2)

                cv2.putText(imgBackground, name, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

                #other way to do it
                # y1, x2, y2, x1 = faceLoc
                # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                # bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                # imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                # cv2.putText(imgBackground, name, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                    
                # print("I dont know this face\n no information available!!!")
    else:
        modeType = 0
        counter = 0
    cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
   




















