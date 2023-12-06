import cv2
import numpy

cascade_path = './Models/haarcascade_frontalface_default.xml'
smile_path = './Models/haarcascade_smile.xml'

clf = cv2.CascadeClassifier(cascade_path)
camera = cv2.VideoCapture(0)

def face_capture():
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=25,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, width, height) in faces:
            rectangle = cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)


        cv2.imshow('Faces', frame)
        print(faces)
        if type(faces) == numpy.ndarray:
            print("Обнаружено лицо")
            yep = 15
            main(yep)
            quit()

        # if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == ord('й'):
        #     quit()
    camera.release()
    cv2.destroyAllWindows()



def main(yep):
    if yep == 15:
        quit()
    else:
        face_capture()


if __name__ == '__main__':
    yep =  1
    main(yep)
