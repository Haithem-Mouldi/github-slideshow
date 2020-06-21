def PreProcess(img):
    '''
    Giving a path to an image with text,
    this function do the PreProcess part
    to get better results using Tesseract
    '''
    kernel = np.ones((1, 1), np.uint8)
    #transforming the colors of the image to gray graduations:
    img=cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    #Removing Noise
    img =cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    #Binarizing the image
    img = cv2.threshold(cv2.GaussianBlur(img,(3,3),0), 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)[1] 
    return img
