import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray,1.3)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),5)
        cv2.imshow('result',img)
        if cv2.waitKey(1)== 27:
            break
    else:
        print("Camera Not Working")

capture.release()
cv2.destroyAllWindows()

