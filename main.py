""" https://towardsdatascience.com/simple-face-detection-in-python-1fcda0ea648e
Surse: Towards Data Science, Youtube
"""


import cv2

face_cascade = cv2.CascadeClassifier('face_detector.xml')
# Citeste imaginea de la tastatura
img = cv2.imread(input('Specifica imaginea:'))
#Transforma imaginea in gri
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detecteaza fetele
faces = face_cascade.detectMultiScale(img, 1.1, 4)
ROI_number = 1
# Pentru fiecare coordonata a dreptunghiului fetei
for (x, y, w, h) in faces:
    #printeaza coordonatele
    print(x, y, w, h)
    #o converteste in gri
    roi_gray = gray[y:y + h, x:x + w]
    #scrie imaginea
    cv2.imwrite('fata{}.png'.format(ROI_number), roi_gray)
    #pune dreptunghiul in jurul fetelor
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #se incrementeaza numele
    ROI_number += 1
#scrie imaginea in fisier
cv2.imwrite("fete_detectate.png", img)
print('Salvat cu succes')
