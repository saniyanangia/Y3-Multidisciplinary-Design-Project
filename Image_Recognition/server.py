import cv2
import imagezmq
import socket
import fetchImages
import sys

imageHub = imagezmq.ImageHub(open_port='tcp://*:50000')
print("Start image server")

while True:
    print("Waiting for image")
    rpiName, image = imageHub.recv_image()
    cv2.waitKey(1)
    print("rpi name: ", rpiName)
    if rpiName == "done":
        message = "Done"
        message = message.encode('utf-8')
        imageHub.send_reply(message)
        img = cv2.imread('runs/stitched/stitchedOutput.png')
        resizeImage = cv2.resize(img, (720*2, 720))
        cv2.imshow('Stitched Image', resizeImage)
        stopCondition = 0xEFFFFF
        while (cv2.waitKey(0) & stopCondition) != 27:
            continue
        imageHub.close()
        print("Exiting")
        sys.exit(0)

    print("Received")
    outputDir = r' ' #replace with folder path [in inverted commas (' ')] that will contain image from rpi 
    print("Saved")
    cv2.imwrite(outputDir, image)
    print("Sending to image processing")
    message = fetchImages.main()
    if message is None:
        message = "NO"
    message = message.encode('utf-8')
    cv2.waitKey(1)
    imageHub.send_reply(message)
