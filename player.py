import cv2
import vlc

cam = cv2.VideoCapture(0) #mobile - ip
m = vlc.MediaPlayer(r'2 Many Girls - Fazilpuria.mp4')
fd = cv2.CascadeClassifier(r'C:\Program Files\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
flag = 1

while True:
    r, i = cam.read()
    j = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    face = fd.detectMultiScale(j,1.3,7)
    print(face)
    l = len(face)
    print( l)
    total = 0 #to store the width of the face in the camera
    for(x,y,w,h) in face:
        stroke = 4
        #cv2.rectangle(i,(x,y),(x+w, y+h),(0,0,255),stroke) #if we give the stroke negative then: 'fill'
        total = w*h
    if(l>0):
        print('Song played')
        flag =0
        m.play()
        if(total>100000):
            print("low volume,  total = ",total)
            print('Value: ',100 - int(total/10000))
            m.audio_set_volume(100 - int(total/10000))
        elif(total>50000):
            print("High volume")
            m.audio_set_volume(100)
    elif(flag==0):
        print("Song paused")
        m.pause()
        flag =1
    
    #cv2.imshow('image', j)
    cv2.imshow('image2',i)
    k=cv2.waitKey(5)

    if(k==ord('b')):
        r,back = cam.read()
        cv2.imshow('my image',back)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
