import cv2
import time
import csv
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)
prev_time=time.time()
max_face=0
previous_count=-1
csv_file=open("face_log.csv","w",newline="")
writer=csv.writer(csv_file)
writer.writerow(["Time","Faces"])
while True:

    ret, frame = cap.read()
   
    

    if not ret:
        print("Failed to access camera")
        break
    current_time=time.time()
    fps=1/(current_time-prev_time)
    prev_time=current_time

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )
        face_count=len(faces)
        max_face=max(max_face,face_count)
        if face_count!=previous_count:
            current_time_text=time.strftime("%H:%M:%S")
            print(f"{current_time_text}->Faces detected:{face_count}")
            writer.writerow([current_time_text,face_count])
            previous_count=face_count
        cv2.putText(
        frame,
        f"Faces detected: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        1
    )
        cv2.putText(
            frame,f"Faces detected:{face_count}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1
        )
        cv2.putText(

            frame,f"FPS:{fps:.2f}",(20,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1
        )
        cv2.putText(frame,f"Max face:{max_face}",(20,120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)


    cv2.imshow("Face Detection", frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break
    if key==ord("s"):
        filename=f"screenshot/screenshot_{int(time.time())}.jpg"
        cv2.imwrite(filename,frame)
        print(f"screenshot saved as {filename}")

   

cap.release()
cv2.destroyAllWindows()
csv_file.close()
print("Program ended")
print(f"MAXIMUM FACE DETECTED:{max_face}")