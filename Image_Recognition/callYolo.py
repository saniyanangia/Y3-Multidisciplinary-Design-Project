import cv2
import detect
import os

global count
count = 0


def callImageRecogintion(picture):
    global count
    count = count + 1 #to save all images taken by rpi camera
    name = 'output' + str(count) + '.png'
    outputDir = os.path.join('runs', 'output', name)
    cv2.imwrite(outputDir, picture)
    print("Running model")
    resultsDir = os.path.join('runs', 'results')
    return detect.detect(weights='best.pt',
                         source=outputDir,
                         imgsz=640, 
                         conf_thres=0.65, #can lower conf_thres if accuracy is lower
                         iou_thres=0.25,
                         device='',
                         view_img=False,
                         save_txt=False,
                         save_conf=False,
                         nosave=False,
                         classes=None,
                         agnostic_nms=False,
                         augment=False,
                         update=False,
                         project=resultsDir,
                         exist_ok=False,
                         half=False,
                         )
