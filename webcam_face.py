import cv2
import mediapipe as mp

def get_face_curve_points():
    mp_face_mesh = mp.solutions.face_mesh
    cap = cv2.VideoCapture(0)

    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1) as face_mesh:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb)

            if results.multi_face_landmarks:
                face_landmarks = results.multi_face_landmarks[0]
                # 광대~턱선 라인 좌표 일부 추출 (5개 지점 예시)
                indices = [234, 93, 132, 58, 172]
                coords = []
                h, w, _ = frame.shape
                for idx in indices:
                    lm = face_landmarks.landmark[idx]
                    coords.append((lm.x * w, lm.y * h))
                
                cap.release()
                cv2.destroyAllWindows()
                return coords  # [(x1, y1), (x2, y2), ...]

            cv2.imshow('Webcam - Press Q to cancel', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    return []
