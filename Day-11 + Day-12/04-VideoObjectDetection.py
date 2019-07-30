import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture('video_1.mp4')

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    ret, img = capture.read()
    if ret:
        img = cv2.resize(img, None, fx=0.5, fy=0.5)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray,1.3)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),5)
            cv2.putText(img,'Person',(x,y), font,1, (0,255,0),2)
        cv2.imshow('result',img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        print("Camera Not Working")

capture.release()
cv2.destroyAllWindows()

