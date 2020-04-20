import numpy as np
import cv2
import imutils
import os

def take(new_student):
    base_dir=os.path.dirname(os.path.abspath('__file__'))
    image_dir=os.path.join(base_dir,'images')
    std_dir=os.path.join(image_dir,new_student)
    os.mkdir(std_dir)
    capture=cv2.VideoCapture(0)
    count=0
    net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
    while(True):
        _,frame=capture.read()
        frame = imutils.resize(frame, width=720) 
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detected_faces = net.forward()
        
        if detected_faces is not None:
            count+=1
            for i in range(0, detected_faces.shape[2]):
                    
                confidence = detected_faces[0, 0, i, 2]

                if confidence < 0.6:
                    continue
                
                file_name=str(count)+'.jpg'
                file_name_path=os.path.join(std_dir,file_name)
                cv2.imwrite(file_name_path,frame)
                
                cv2.putText(frame,str(confidence),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)  
                cv2.imshow('Face Cropper',frame)
        
        else:
            print("Face not Found")
            pass
        
        if cv2.waitKey(1)==13 or count==100:
            break
            
    capture.release()
    cv2.destroyAllWindows()
    
    
