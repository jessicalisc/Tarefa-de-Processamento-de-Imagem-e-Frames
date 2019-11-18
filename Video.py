import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('Tom e Jerry.avi')

i = 1
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame em Cinza',gray) # Este filtro muda a coloraçao do frame selecionado para cinza.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 100):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    cortar = frame[90:350, 50:310] #corta o video em pixes especificos

    cv2.imshow('Frame recortada',cortar)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 200):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    redimensionar = cv2.resize(frame, (160, 300))

    cv2.imshow('Video redimensionado',redimensionar)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 300):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() 
    (h, w, d) = frame.shape
    r = 300.0 / w
    dim = (300, int(h * r))
    proporcao = cv2.resize(frame, dim)
    cv2.imshow('Redimensionar por proporcao',proporcao) #
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    if (i == 400):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()
    redimutils = imutils.resize(frame, width=300) # este filtro redimensiona a frame conforme o tamanho especificado

    cv2.imshow('Redimensionar pelo Imutils',redimutils)# apresenta em tela os resultados do filtro aplicado.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 500):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -180, 1.0)
    rotacao = cv2.warpAffine(frame, M, (w, h)) #este filtro esta fazendo a rotaçao da frame apartir das dimensoes especificadas.

    cv2.imshow('Rotacao OpenCV',rotacao) # apresenta em tela o resultado do filtro de rotaçao
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 600):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    rotacaoim = imutils.rotate(frame, -45) # rotacao da imagem pela biblioteca imutils em 45 graus

    cv2.imshow('Rotacao Imutils',rotacaoim) #apresenta em tela o resultado do filtro.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 700):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    rota = imutils.rotate_bound(frame, 90) #filtro responsavel por mudar a posiçao da frame em 90 graus

    cv2.imshow('Rotacao Modificada',rota) # apresenta em video o resultado do filtro
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 800):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    desfoque = cv2.GaussianBlur(frame, (11, 11), 0) #filtro responsavel por desfocar a imagem toda das frames.

    cv2.imshow('Desfocar o Video ',desfoque) #apresenta no video os resultados do filtro
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 900):
        break
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    output = frame.copy()
    cv2.rectangle(output, (380, 360), (250, 100), (0, 0, 255), 5)# filtro responsavel por modelar um retandulo coma as seguintes especificações sobre as frames.

    cv2.imshow('Retangulo sobre o Video',output) # responsavel apresentar em tela um retangulo sobre o video.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1000):
        break
    i +=1

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

while(cap.isOpened()):
    ret, frame = cap.read()

    saida = frame.copy()
    cv2.putText(saida, "OpenCV + Tom e Jerry!!!", (20, 20),# filtro responsavel por colocar uma simples frase em determinados frames e posiçoes na matriz
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('Frase aplicada sobre o Video',saida)# apresentação em tela do trabalho realizado pelo filtro, no caso a frase"Opencv + Tom e Jerry"
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1300):
        break
    i +=1

cap.release()
cv2.destroyAllWindows()
