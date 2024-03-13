from imutils import paths
from PIL import Image

def stitch():
    imageFolder = r' ' #replace with folder path [in inverted commas (' ')] that will contain results from model (ie ./runs/results)
    imagePath = list(paths.list_images(imageFolder))
    images = [Image.open(x) for x in imagePath]
    if len(images) <= 7:
        columns = len(images)
    if len(images) > 7:
        columns = 7
    stitched_image = createGrid(images, (len(images)//7)+1, columns) #can vary dimensions of grid
    #replace with path [in inverted commas (' ')] that will contain stitched image grid (ie ./runs/stitched/StitchedOutput.png)
    stitched_image.save(' ', format='png')


def createGrid(images, rows, columns):
    len(images) == rows*columns
    width, height = images[0].size
    grid = Image.new('RGB', size=(columns*width, rows*height))
    for i, image in enumerate(images):
        grid.paste(image, box=(i % columns*width, i//columns*height))
    return grid
