import cv2
import numpy as np
import time


# tiny
net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')
# normal
# net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

classes = []

with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture('avoidingLeftCrash.mp4')


font = cv2.FONT_HERSHEY_DUPLEX
starting_time = time.time()
frame_id = 0
obj_id = 0
danger_objects = []


while True:

    _, img = cap.read()
    height, width, _ = img.shape
    frame_id += 1

    # calculation of danger zone
    dangerw = (int) (width * .5)
    epsilonw = (int) (width * 0.1)
    dangerh = (int) (height * .33)
    epsilonh = (int) (height * 0.15)

    colors = np.random.uniform(0, 255, size=(1, 3))
    cv2.rectangle(img, (dangerw-epsilonw, dangerh-epsilonh), (dangerw+epsilonw, dangerh+epsilonh), (0,0,255), 2)
    cv2.putText(img, "DANGER!",
                (dangerw-epsilonw, dangerh-epsilonh-7), font, 1, (0, 0, 255), 2)


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

                if center_x in range(dangerw-epsilonw, dangerw+epsilonw) and center_y in range(dangerh-epsilonh, dangerh+epsilonh):
                    danger = True
                    if len(danger_objects) == 0:
                        danger_objects.append({obj_id: [center_x, center_y, 1]})
                        last_timestamp = time.time()
                        obj_id += 1
                    else:
                        added = False
                        for i in range(len(danger_objects)):
                            value = list(danger_objects[i].values())[0]
                            # print(value)
                            # print(value[0] in range(center_x-10, center_x+10))
                            # print(value[1] in range(center_y-10, center_y+10))
                            # print(time.time() - last_timestamp)
                            if value[0] in range(center_x-15, center_x+15) and value[1] in range(center_y-15, center_y+15) and time.time() - last_timestamp < 2 and value[1] > center_y:
                                value[2]+=1
                                # print('DANGER +1')
                                if value[2] >= 4:
                                    print('WHOOP WHOOP RED DANGER ALERT!!!!')
                                    break
                                added = True
                                last_timestamp = time.time()
                                break
                        if added == False:
                            danger_objects.append({obj_id: [center_x, center_y, 1]})
                            last_timestamp = time.time()
                            obj_id += 1
                    # print(danger_objects)
                    # print(len(danger_objects))
                    # print('DANGER!')

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
    cv2.imshow('Output', cv2.resize(img, (700, 500)))
    key = cv2.waitKey(1)  # 0

    # if the 'c' key is pressed, stop the loop
    if key == ord('c'):
        break


cap.release()
cv2.destroyAllWindows()
