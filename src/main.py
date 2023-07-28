from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def changeBrightness(imgPath):
    brightnesFactor = float(input("Nhập giá trị tăng độ sáng: "))
    img = Image.open(imgPath)
    imgMatrix = np.array(img)
    imgMatrix = np.clip(imgMatrix,0,255)
    newImgMatrix = imgMatrix.astype('int32') + brightnesFactor
    newImgMatrix = np.clip(newImgMatrix,0,255)
    newImg = Image.fromarray(newImgMatrix.astype('uint8'))

    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_changeBrightness"+"."+fileExtension
    newImg.save(path)

def changeContrast(imgPath):
    img = Image.open(imgPath)
    contrastFactor = float(input("Nhập giá trị tăng độ tương phản: "))
    img = Image.open(imgPath)
    imgMatrix = np.array(img)
    newImgMatrix = contrastFactor*imgMatrix
    newImgMatrix = np.clip(newImgMatrix,0,255)
    newImg = Image.fromarray(newImgMatrix.astype('uint8'))
    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_changeContrast"+"."+fileExtension
    newImg.save(path)



def convertIntoGray(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    grayImg = Image.new('L', (width, height))
    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            avg = int(round((r+b+g)/3))
            grayImg.putpixel((i, j), avg)
    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_gray"+"."+fileExtension
    grayImg.save(path)

def convertIntoSepia(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    sepiaImg = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            newR = int(0.393 * r + 0.769 * g + 0.189 * b)
            newG = int(0.349 * r + 0.686 * g + 0.168 * b)
            newB = int(0.272 * r + 0.534 * g + 0.131 * b)
            newR = min(255,newR)
            newG = min(255,newG)
            newB = min(255,newB)
            sepiaImg.putpixel((i, j), (newR,newG,newB))
    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_sepia"+"."+fileExtension
    sepiaImg.save(path)

def vericalFlipImage(imgPath):
    img = Image.open(imgPath)
    imgMatrix = np.array(img)
    verImgMatrix = np.fliplr(imgMatrix)
    verImg = Image.fromarray(verImgMatrix)
    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_verticalFlip"+"."+fileExtension
    verImg.save(path)

def horizonalFlipImage(imgPath):
    img = Image.open(imgPath)
    imgMatrix = np.array(img)
    horImgMatrix = np.flipud(imgMatrix)
    horImg = Image.fromarray(horImgMatrix)
    
    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_horizonal"+"."+fileExtension
    horImg.save(path)

def blurImage(imgPath):
    img = Image.open(imgPath)
    imgMatrix = np.array(img)
    width, height = img.size
    kernel = np.ones((3, 3)) / 9 
    kernel = np.flipud(np.fliplr(kernel)).astype('float')  # Convert kernel to float
    blurImg = Image.new('RGB', (width, height))  # Create a new RGB image
    x = kernel.shape[0] // 2
    y = kernel.shape[1] // 2
    for i in range(x, width - x):
        for j in range(y, height - y):
            region = imgMatrix[i - x:i + x + 1, j - y:j + y + 1]
            newPixel = np.sum(region * kernel)
            newPixel = int(np.clip(newPixel, 0, 255))
            blurImg.putpixel((i, j), (newPixel, newPixel, newPixel))  # Set pixel value as RGB tuple

    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_blur"+"."+fileExtension
    blurImg.save(path)


def cutBySize(imgPath):
    size = int(input("Nhập độ lớn cần cắt (%): "))
    
    img = Image.open(imgPath)
    width, height = img.size
    size = int((height * size) //100)
    cuttedImg = Image.new('RGB', (size, size))  # Define size of the cutted image
    xPadding = (width- size) // 2
    yPadding = (height - size) // 2
    for i in range(xPadding, xPadding + size):
        for j in range(yPadding, yPadding + size):
            pixel = img.getpixel((i, j))  # Get pixel value from the original image
            cuttedImg.putpixel((i - xPadding, j - yPadding), pixel)  # Set pixel value in the cutted image


    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_cutted"+"."+fileExtension
    cuttedImg.save(path)


def roundCut(imgPath):
    img = Image.open(imgPath)
    imgMatrix = np.array(img)
    width, height = img.size

    size = min(width, height)
    roundImg = Image.new('RGB', (size, size))
    xPadding = (width - size) // 2
    yPadding = (height - size) // 2
    x = width//2
    y = height // 2
    radius = size // 2
    for i in range(xPadding,xPadding+size):
        for j in range(yPadding,yPadding+size):
            distance = np.sqrt((i - x)**2 + (j - y)**2)
            if distance <= radius:
                pixel = img.getpixel((i + (width - size) // 2, j + (height - size) // 2))
                roundImg.putpixel((i - xPadding, j - yPadding), pixel)
            else:
                roundImg.putpixel((i - xPadding, j - yPadding),  (0, 0, 0) )
    fileName, fileExtension = imgPath.split(".")
    path = fileName + "_round"+"."+fileExtension
    roundImg.save(path)

    

def main():
    imgPath = input("Nhập tên tập tin ảnh: ")
    choice = int(input("Lựa chọn chức năng xử lý ảnh (từ 1 đến 7, 0 để thực hiện tất cả): "))

    if choice == 1:
        changeBrightness(imgPath)
    elif choice == 2:
        changeContrast(imgPath)
    elif choice == 3:
        dimension = int(input("(ngang = 0 , dọc = 1)"))
        if(dimension): 
            vericalFlipImage(imgPath)
        else:
            horizonalFlipImage(imgPath)
    elif choice == 4:
        type = int(input("(gray = 0 , sepia = 1)"))
        if(type): 
            convertIntoSepia(imgPath)
        else:
            convertIntoGray(imgPath)
    elif choice == 5:
        blurImage(imgPath);
    elif choice == 6:
        cutBySize(imgPath)
    elif choice == 7:
        roundCut(imgPath)
    elif choice == 0:
        changeBrightness(imgPath)
        changeContrast(imgPath)
        horizonalFlipImage(imgPath)
        vericalFlipImage(imgPath)
        convertIntoGray(imgPath)
        convertIntoSepia(imgPath)
        cutBySize(imgPath)
        roundCut(imgPath)

    


if __name__  == "__main__":
    main()