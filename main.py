import cv2
import mediapipe as mp
import pyautogui

def facialTracking():
    video_path = 'clipchampv2.mp4'
    cam = cv2.VideoCapture(video_path)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
    screen_w, screen_h = pyautogui.size()

    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0)) # cv2.circle() takes the frame as the first argument, the center of the circle as the second, radius third, and color as the final argument
                if id == 1:
                    screen_x = int(landmark.x * screen_w)
                    screen_y = int(landmark.y * screen_h)
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < .004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    # if 'q' is pressed, it will end the program.

def eyeTracking():
    video_path = 'clipchampv2.mp4'
    cam = cv2.VideoCapture(video_path)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
    screen_w, screen_h = pyautogui.size()

    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0)) # cv2.circle() takes the frame as the first argument, the center of the circle as the second, radius third, and color as the final argument
                if id == 1:
                    screen_x = int(landmark.x * screen_w)
                    screen_y = int(landmark.y * screen_h)
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < .004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    # if 'q' is pressed, it will end the program.

while True:
    output = input('Facial Tracking or Eye Tracking? ').strip().lower()

    if 'facial' in output:
        facialTracking()
        break
    elif 'eye' in output:
        eyeTracking()
        break
    else:
        print('Please provide a valid tracking method.')