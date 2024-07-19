import cv2
import time
import numpy as np

# Camera resolution
Wcam, hcam = 648, 480
cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, hcam)

pTime = 0  # Initialize previous time

while True:
    success, img = cap.read()
    if not success:
        break

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (60, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("img", img)
    key = cv2.waitKey(1)

    # Break the loop when 'q' is pressed
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

