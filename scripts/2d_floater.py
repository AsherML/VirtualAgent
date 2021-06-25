import cv2
import mediapipe as mp
import numpy as np
import gestures
import math
import random

width=1220
height=880
speaking_delay=20

mp_holistic=mp.solutions.holistic
cap=cv2.VideoCapture(0)

default_floater_loc=None
floater_dimensions=None
perma_count=5
increasing=True

with mp_holistic.Holistic(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8) as holistic:

    while cap.isOpened():
        color=(255, 0,0)
        success, image=cap.read()
        if not success:
            print("something went wrong with your camera")
            continue
        image=cv2.flip(image, 1)
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=holistic.process(image)

        new_image=np.zeros((height, width, 3), np.uint8)
        

        if results and results.face_landmarks is not None:
            face_center=results.face_landmarks.landmark[4]
            default_floater_loc=(int(face_center.x*width)+200, int(face_center.y*height)+200, abs(int(20+2000*face_center.z)))
            is_talking=gestures.is_speaking(results.face_landmarks, 0.00005)
            if is_talking or speaking_delay<6:
                if is_talking:
                    speaking_delay=0
                count=perma_count
                while count>0:
                    cv2.circle(new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=(count*10)+abs(int(+4000*face_center.z)), color=(255-(count*20),0,0), thickness=20)
                    count-=1
                if perma_count<=0:
                    increasing=True
                if perma_count>=20:
                    increasing=False
                if increasing:
                    perma_count+=random.randint(1, 7)
                else:
                    perma_count-=random.randint(1,7)
                

                
            if results.left_hand_landmarks is not None or results.right_hand_landmarks is not None:
                if results.right_hand_landmarks is not None:
                    hand=results.right_hand_landmarks.landmark[0]
                    floater_dimensions=(int(hand.x*width), int(hand.y*height-200), abs(int(20+2000*face_center.z)))
                else:
                    hand=results.left_hand_landmarks.landmark[0]
                    floater_dimensions=(int(hand.x*width), int(hand.y*height-200), abs(int(20+2000*face_center.z)))
    
            
            else:
                floater_dimensions=default_floater_loc
            
            cv2.circle(new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(20+4000*face_center.z)), color=color, thickness=-1)
            cv2.circle(new_image, center=floater_dimensions[:2], radius=floater_dimensions[2], color=(255,0,0), thickness=-1)
        else:
            cv2.circle(new_image, center=(int(face_center.x*width), int(face_center.y*height)), radius=abs(int(20+4000*face_center.z)), color=color, thickness=-1)
            cv2.circle(new_image, center=floater_dimensions[:2], radius=floater_dimensions[2], color=(255,0,0), thickness=-1)
        speaking_delay+=1
        cv2.imshow("With Circle", new_image)
        if cv2.waitKey(5) & 0xFF==27:
            break
cap.release()


            



            
            
        
            
            