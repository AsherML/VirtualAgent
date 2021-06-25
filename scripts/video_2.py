import cv2
import mediapipe as mp
import gestures
import math

mp_holistic=mp.solutions.holistic
width=1220
height=880


default_frames, speaking_frames, agree_frames, raise_hand_frames=([],[],[],[])

default=cv2.VideoCapture("resources/default_wifiicon.mp4")
speaking=cv2.VideoCapture("resources/speaking_wifiicon.mp4")
agree=cv2.VideoCapture("resources/trimmed_nod.mp4")
raise_hand=cv2.VideoCapture("resources/want_to_speak_wifiicon.mp4")

def safe_show(frame_container, count):
    if count>=len(frame_container):
        cv2.imshow("Vero Animations", frame_container[0])
        return 0
    else:
        cv2.imshow("Vero Animations", frame_container[count])
        if frame_container==agree_frames:
            return count+1
        else:
            return count+7

def store_frames(frame_container, video_obj):
    while video_obj.isOpened():
        success, image=video_obj.read()
        if not success:
            video_obj.release()
            break
        image=cv2.resize(image, (width, height))
        frame_container.append(image)

store_frames(default_frames, default)
store_frames(speaking_frames, speaking)
store_frames(agree_frames, agree)
store_frames(raise_hand_frames, raise_hand)

cap=cv2.VideoCapture(0)

speaking_delay=20
thumb_delay=20
frame_count=0

with mp_holistic.Holistic(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as holistic:

    while cap.isOpened():
        success, image=cap.read()
        if not success:
            print("Ignoring empty camera")
            continue

        image=cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=holistic.process(image)
        
        if results is None or results.face_landmarks is None:
            frame_count=safe_show(default_frames, frame_count)
            
        else:
            speaking_indicator=gestures.is_speaking(results.face_landmarks, 0.00005)
            if speaking_indicator or speaking_delay<10:
                if speaking_indicator:
                    speaking_delay=0
                frame_count=safe_show(speaking_frames, frame_count)
                
            else:
                hand_gesture=gestures.hand_gestures(results.left_hand_landmarks, results.right_hand_landmarks)
                if hand_gesture or thumb_delay<10:
                    if hand_gesture=="Thumb" or thumb_delay<10:
                        if hand_gesture=="Thumb":
                            thumb_delay=0 
                        frame_count=safe_show(agree_frames, frame_count)
                    else:
                        frame_count=safe_show(raise_hand_frames, frame_count)    
                else:
                    frame_count=safe_show(default_frames, frame_count)
        
        speaking_delay+=1
        thumb_delay+=1
                    
        if cv2.waitKey(5) & 0xFF == 27:
                break
cap.release()

            
        

            
        
        
        


