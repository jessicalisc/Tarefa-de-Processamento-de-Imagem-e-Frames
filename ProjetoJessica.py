# USAGE
# python opencv_tutorial_01.py

# importando as bibliotecas necessárias
import imutils
import cv2

# carregando imagem
image = cv2.imread("jerry.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# Para apresentar a imagem modificada precisamos apertar uma tecla para passar para a proxima imagem
cv2.imshow("Imagem", image)
cv2.waitKey(0)

# Salvando imagem em BGR por causa do OpenCV que não salva em RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))


#corta a imagem nos parametro selecionados
roi = image[60:160, 200:310]
cv2.imshow("Cortando Imagem", roi)
cv2.waitKey(0)

# no nosso caso as dimenções são 80x100px
#diminui a imagem para as dimensoes especificadas abaixo
resized = cv2.resize(image, (80, 100))
cv2.imshow("Redimensionamento Fixo", resized)
cv2.waitKey(0)

# calculo manual para ver a proporção da imagem e apresenta-la
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Redimensionamento pela Proporcao", resized)
cv2.waitKey(0)

# usar a biblioteca Imutils para calcular a proporção
resized = imutils.resize(image, width=300)
cv2.imshow("Redimensionar Imutils", resized)
cv2.waitKey(0)

# a imagem sera girada em 45 graus no sentido horario pelo Opencv
# E depois aplicar a distorção
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotacao OpenCV", rotated)
cv2.waitKey(0)

# aqui é possivel ver uma rotação por meio do Imutils que tem o cuidado de nao cortar a imagem
rotated = imutils.rotate(image, -180)
cv2.imshow("Rotacao Imutils", rotated)
cv2.waitKey(0)

# O OpenCV possivelmente cortará a imagem na rotação, mas aqui usaremos como auxilio o imutils
# pois ele não deixa a imagem ser cortada.
rotated = imutils.rotate_bound(image, 90)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# aplica o filtro gaussiano em 11x11 para suavizar a imagem
# reduz ruídos de alta frequência
#embaça a imagem
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Desfocar", blurred)
cv2.waitKey(0)

# desenha um retângulo vermelho sobre a imagem
output = image.copy()
#apresenta um retangulo sobre a imagem
cv2.rectangle(output, (180, 360), (200, 160), (0, 0, 255), 2)
cv2.imshow("Retangulo Vermelho", output)
cv2.waitKey(0)

# desenhe um circulo azul 20px (de preenchimento) nas seguintes posições
# x=150,y=150
#apresenta um circulo sobre a imagem
output = image.copy()
cv2.circle(output, (150, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circulo Azul", output)
cv2.waitKey(0)

# desenhe uma linha vermelha com as proporções x=60,y=20 por x=200,y=200
#apresenta uma linha sobre a imagem
output = image.copy()
cv2.line(output, (60, 20), (200, 200), (0, 0, 255), 5)
cv2.imshow("Linha Vermelha", output)
cv2.waitKey(0)


#apresenta um texto sobre a imagem
output = image.copy()
cv2.putText(output, "OpenCV + Jerry!!!", (10, 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
