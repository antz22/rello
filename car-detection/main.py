import cv2
import numpy as np
import time


net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

classes = []

with open('coco.names', 'r') as f:
    classes = f.read().splitlines()


cap = cv2.VideoCapture(0)
#img = cv2.imread('image3.jpeg')


font = cv2.FONT_HERSHEY_DUPLEX
starting_time = time.time()
frame_id = 0


while True:

    _, img = cap.read()
    height, width, _ = img.shape
    frame_id += 1

    blob = cv2.dnn.blobFromImage(
        img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layersOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                class_ids.append(class_id)
                confidences.append((float(confidence)))

    print(len(boxes))
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 8)
            cv2.putText(img, label + " " + confidence,
                        (x, y+20), font, 1, (255, 255, 255), 2)

    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(img, "FPS: " + str(fps), (10, 30), font, 1, (0, 0, 0), 1)
    # cv2.resize(img,(600, 400))
    cv2.imshow('Output', cv2.resize(img, (700, 500)))
    key = cv2.waitKey(1)  # 0

    # if the 'c' key is pressed, stop the loop
    if key == ord('c'):
        break


cap.release()
cv2.destroyAllWindows()
