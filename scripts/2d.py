import cv2
import mediapipe as mp
import numpy as np
import gestures
import math

width  = 1220
height = 880

mp_holistic=mp.solutions.holistic
cap=cv2.VideoCapture(0)


max_size=300
min_size=100
current_size=150
increasing=True
speaking_delay=20
# p0=None
# nod_threshold=0.8
# y_movement=0
# count=0


with mp_holistic.Holistic(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        success, image=cap.read()
        if not success:
            print("Something went wrong with your camera")
            continue

        image=cv2.flip(image,1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = holistic.process(image)

        new_image=np.zeros((height, width,3), np.uint8)

        if results and results.face_landmarks is not None:
            face_center=results.face_landmarks.landmark[4]
            hand_gesture=gestures.hand_gestures(results.left_hand_landmarks, results.right_hand_landmarks)
            is_talking=gestures.is_speaking(results.face_landmarks, 0.00005)
            if is_talking or speaking_delay<6:
                if is_talking:
                    speaking_delay=0
                cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(20+4000*face_center.z)), color=(211, 214, 15), thickness=-1)
                cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(40+4000*face_center.z)), color=(255,0,0), thickness=-1)
                cv2.imshow("VERO 2D", new_image)

            

            elif hand_gesture:
                if hand_gesture=="Thumb":
                    cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(20+4000*face_center.z)), color=(0,255,0), thickness=-1)
                    cv2.imshow("VERO 2D", new_image)
                else:
                    cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=current_size, color=(255,0,0), thickness=-1)
                    if current_size>=max_size:
                        increasing=False
                    if current_size<=min_size:
                        increasing=True
                    if increasing:
                        current_size+=15
                    else:
                        current_size-=15


            else:
            
                if hand_gesture:
                    cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=current_size, color=(255,0,0), thickness=-1)
                    if current_size>=max_size:
                        increasing=False
                    if current_size<=min_size:
                        increasing=True
                    if increasing:
                        current_size+=15
                    else:
                        current_size-=15

                    current_size=150
                    increasing=True
                    cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(20+4000*face_center.z)), color=(255,0,0), thickness=-1)
                else:
                    cv2.circle(img=new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(20+4000*face_center.z)), color=(255,0,0), thickness=-1)
        speaking_delay+=1
        cv2.imshow("VERO 2D", new_image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
