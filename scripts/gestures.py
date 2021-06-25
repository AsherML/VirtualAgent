import math

def is_speaking(facemesh, threshold):
    top_lip=facemesh.landmark[13]
    bottom_lip=facemesh.landmark[14]
    distance=((top_lip.x-bottom_lip.x)**2 + (top_lip.y-bottom_lip.y)**2)
    return distance>threshold

def hand_gestures(left_hand, right_hand):

    def angle(origin, point1, point2):
        def distance(point1, point2):
            return math.sqrt(((point2.x-point1.x)**2 + (point2.y-point1.y)**2 + (point2.z-point1.z)**2))
        vector1=[point1.x-origin.x, point1.y-origin.y, point1.z-origin.z]
        vector2=[point2.x-origin.x, point2.y-origin.y, point2.z-origin.z]
        combined_vector=(vector1[0]*vector2[0])+(vector1[1]*vector2[1])+(vector1[2]*vector2[2])
        return math.acos(combined_vector/(distance(point1, origin)*distance(point2, origin)))

    if left_hand is None and right_hand is None:
        return False
    if left_hand is None:
        wrist=right_hand.landmark[0]
        thumb=right_hand.landmark[4]
        pointer=right_hand.landmark[8]
        dip=right_hand.landmark[6]
    else:
        wrist=left_hand.landmark[0]
        thumb=left_hand.landmark[4]
        pointer=left_hand.landmark[8]
        dip=left_hand.landmark[6]
    
    if angle(wrist, thumb, pointer)<angle(wrist, thumb, dip) and thumb.y<pointer.y:
        return "Thumb"
    else:
        return "Raise"
    
def make_limbs(left_hand, right_hand, face_center, width, height):
    
    def border_distance(hand_origin, face_center, width, height):
        face_radius=abs(int(20+4000*face_center.z))
        hand_radius=abs(int(20+1000*hand_origin.z))
        def distance(p1, p2):
            return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
        return distance(face_center, hand_origin)>(face_radius+hand_radius+30)

    left_circles=[(int(face_center.x*width-200), int(face_center.y*height), abs(int(20+1000*face_center.z))), (int(face_center.x*width-150), int(face_center.y*height+150), abs(int(20+1000*face_center.z))), (int(face_center.x*width-150), int(face_center.y*height-150), abs(int(20+1000*face_center.z)))]
    right_circles=[(int(face_center.x*width+200), int(face_center.y*height), abs(int(20+1000*face_center.z))), (int(face_center.x*width+150), int(face_center.y*height+150), abs(int(20+1000*face_center.z))), (int(face_center.x*width + 150), int(face_center.y*height-150), abs(int(20+1000*face_center.z)))]
    if left_hand is None and right_hand is None:
        return left_circles, right_circles
    if right_hand is not None:
        right_hand_origin=right_hand.landmark[0]
        
        right_circles=[(int(right_hand_origin.x*width), int(right_hand_origin.y*height), abs(int(20+1000*right_hand_origin.z))), (int(right_hand_origin.x*width+150), int(right_hand_origin.y*height+150), abs(int(20+1000*right_hand_origin.z))), (int(right_hand_origin.x*width+150), (int(right_hand_origin.y*height-150)), abs(int(20+1000*right_hand_origin.z)))]
    if left_hand is not None:
        print('left')
        left_hand_origin=left_hand.landmark[0]
        print(left_hand_origin)
        # if border_distance(left_hand_origin, face_center, width, height):
        left_circles=[(int(left_hand_origin.x*width), int(left_hand_origin.y*height), abs(int(20+1000*left_hand_origin.z))),(int(left_hand_origin.x*width-150), int(left_hand_origin.y*height+200), abs(int(20+1000*left_hand_origin.z))), (int(left_hand_origin.x*width-150), int(left_hand_origin.y*height-200), abs(int(20+1000*left_hand_origin.z)))]
    return left_circles, right_circles


        
   
        
        
    

