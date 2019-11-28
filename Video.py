# importando bibliotecas necessárias
import numpy as np
import cv2
import imutils

# carregando vídeo
cap = cv2.VideoCapture('Tom e Jerry.avi')

i = 1 #capturando primeira frame

#Este primeiro filtro tem a capacidade de alterar a coloração
# do frame para cinza
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame em Cinza',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 100):
        break
    i +=1

# Este filtro cora o frame em pixes especificos no caso
# frames x=90:350 e y=50:310
while(cap.isOpened()):
    ret, frame = cap.read()

    cortar = frame[90:350, 50:310]

    cv2.imshow('Frame recortada',cortar)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 200):
        break
    i +=1

# Redimensionar nada mais é que diminuir a frame nos valores descrito aqui
# no caso x= 160 e y=300
while(cap.isOpened()):
    ret, frame = cap.read()

    redimensionar = cv2.resize(frame, (160, 300))

    cv2.imshow('Video redimensionado',redimensionar)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 300):
        break
    i +=1


# O redimensionamento por proporção nada mais é do que
# diminuir a frame nas proporções indicadas, porem fazer ajustes
# necessários para que a imagem do frame ao final nao saia distorcida como anteriormente
while(cap.isOpened()):
    ret, frame = cap.read()
    (h, w, d) = frame.shape
    r = 300.0 / w
    dim = (300, int(h * r))
    proporcao = cv2.resize(frame, dim)
    cv2.imshow('Redimensionar por proporcao',proporcao)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    if (i == 400):
        break
    i +=1

# Este filtro vai fazer o mesmo trabalho do anterio com a cautela de não cortar a frame
# por causa da biblioteca Imutils
while(cap.isOpened()):
    ret, frame = cap.read()
    redimutils = imutils.resize(frame, width=300)

    cv2.imshow('Redimensionar pelo Imutils',redimutils)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 500):
        break
    i +=1

# A rotação pelo OpenCV faz a modificação da frame em suas proporções normais
#
while(cap.isOpened()):
    ret, frame = cap.read()
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -180, 1.0)
    rotacao = cv2.warpAffine(frame, M, (w, h))

    cv2.imshow('Rotacao OpenCV',rotacao)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 600):
        break
    i +=1

# Este filtro busca fazer as transformadas na frame com o cuidado de não corta as imagens
while(cap.isOpened()):
    ret, frame = cap.read()

    rotacaoim = imutils.rotate(frame, -15)

    cv2.imshow('Rotacao Imutils',rotacaoim)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 700):
        break
    i +=1

# Filtro de Rotação neste caso responsavel por fazer uma rotação de 90 graus na frame
while(cap.isOpened()):
    ret, frame = cap.read()

    rota = imutils.rotate_bound(frame, 90)

    cv2.imshow('Rotacao Modificada',rota) # apresenta em video o resultado do filtro
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 800): #para na frame 800
        break
    i +=1

# Neste filtro é aplicado o filtro de gaussiano com proporções de 11x11 desfocando a frame por inteira
while(cap.isOpened()):
    ret, frame = cap.read()

    desfoque = cv2.GaussianBlur(frame, (11, 11), 0) #filtro responsavel por desfocar a imagem toda das frames.

    cv2.imshow('Desfocar o Video ',desfoque) #apresenta no video os resultados do filtro
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 900):
        break
    i +=1


# Filtro responsavel por apresentar um retângulo vermelho na tela da frames
#nas proporções especificadas abaixo:
while(cap.isOpened()):
    ret, frame = cap.read()

    output = frame.copy()
    cv2.rectangle(output, (380, 360), (250, 100), (0, 0, 255), 5)

    cv2.imshow('Retangulo sobre o Video',output) # responsavel apresentar em tela um retangulo sobre o video.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1000):
        break
    i +=1

# o Circulo sobre o vídeo nada mais é do que um filtro que aplica em determinada posição da frame
# um circulo no nosso caso azul
while(cap.isOpened()):
    ret, frame = cap.read()

    saida = frame.copy()
    cv2.circle(saida, (150, 50), 40, (255, 10, 0), -9) # filtro que medela um circulo a partir das dimensões aplicadas aqui.

    cv2.imshow('Circulo sobre o Video',saida) #responsavel por apresentar na tela um circulo sobre o video.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1100):
        break
    i +=1


# Neste filtro é desenhado uma linha vermelha sobre as frames nas posições especificadas abaixo
while(cap.isOpened()):
    ret, frame = cap.read()

    saida = frame.copy()
    cv2.line(saida, (160, 20), (250, 200), (0, 0, 255), 5) #filtro que modela uma linha em determinados frames e posições na matriz do video.

    cv2.imshow('Linha sobre o Video',saida)# apresenta sobre o video o objeto aplicado no filtro no caso uma linha na diagonal vermelha.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1200):
        break
    i +=1


#filtro responsavel por aplicar um frase de sua escolha sobre as frames aqui apresentadas
while(cap.isOpened()):
    ret, frame = cap.read()

    saida = frame.copy()
    cv2.putText(saida, "OpenCV + Tom e Jerry = Sucesso!!!", (20, 20),# filtro responsavel por colocar uma simples frase em determinados frames e posiçoes na matriz
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('Frase aplicada sobre o Video',saida)# apresentação em tela do trabalho realizado pelo filtro, no caso a frase"Opencv + Tom e Jerry"
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1300):
        break
    i +=1

cap.release()
cv2.destroyAllWindows()
