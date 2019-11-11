# USAGE
# python opencv_tutorial_01.py

# import the necessary packages
import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("jerry.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
#apresentacao da imagem selecionada
cv2.imshow("Imagem", image)
cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
#corta a imagem nos parametro selecionados
roi = image[60:160, 200:310]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
#diminui a imagem para as dimensoes especificadas abaixo
resized = cv2.resize(image, (80, 100))
cv2.imshow("Redimensionamento Fixo", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Redimensionamento pela Proporcao", resized)
cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Redimensionar Imutils", resized)
cv2.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotacao OpenCV", rotated)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Rotacao Imutils", rotated)
cv2.waitKey(0)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
#embaça a imagem
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Desfocar", blurred)
cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
#apresenta um retangulo sobre a imagem
cv2.rectangle(output, (180, 360), (200, 160), (0, 0, 255), 2)
cv2.imshow("Retangulo", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
#apresenta um circulo sobre a imagem
output = image.copy()
cv2.circle(output, (150, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circulo", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
#apresenta uma linha sobre a imagem
output = image.copy()
cv2.line(output, (60, 20), (200, 200), (0, 0, 255), 5)
cv2.imshow("Linha", output)
cv2.waitKey(0)

# draw green text on the image
#apresenta um texto sobre a imagem
output = image.copy()
cv2.putText(output, "OpenCV + Jerry!!!", (10, 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
