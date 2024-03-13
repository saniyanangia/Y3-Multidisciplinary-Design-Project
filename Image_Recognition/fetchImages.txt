import cv2
import callYolo
import os


def getImage(dirpath, validFiles = ('jpg', 'jpeg', 'png')):
    dirpath = r' ' #replace with folder path [in inverted commas (' ')] that will contain image from rpi
    selectedFile = [os.path.join(dirpath, filename)
                   for filename in os.listdir(dirpath)]
    selectedFile = [f for f in selectedFile if '.' in f and
                   f.rsplit('.', 1)[-1] in validFiles and os.path.isfile(f)]
    if not selectedFile:
        raise ValueError(
            "Error: Check if images were correctly saved in %s" % dirpath)
    return max(selectedFile, key=os.path.getmtime)


def main():
    image = getImage(
        #replace with folder path [in inverted commas (' ')] that will contain image from rpi
        dirpath=r' ', validFiles = ('jpg', 'jpeg', 'png'))
    print("Image Path: ", image)
    imageName = os.path.basename(image)
    print("Image File: ", imageName)
    picture = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    return callYolo.callImageRecogintion(picture)


if __name__ == "__main__":
    main()
