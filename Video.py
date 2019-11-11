import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('Tom e Jerry.avi')

i = 1
while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame em Cinza',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 100): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    cortar = frame[90:350, 50:310] #corta o video em pixes especificos

    cv2.imshow('Frame recortada',cortar)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 200):
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    redimensionar = cv2.resize(frame, (160, 300))

    cv2.imshow('Video redimensionado',redimensionar)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 300):
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while
    (h, w, d) = frame.shape
    r = 300.0 / w
    dim = (300, int(h * r))
    proporcao = cv2.resize(frame, dim)
    cv2.imshow('Redimensionar por proporcao',proporcao)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    if (i == 400): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()
    redimutils = imutils.resize(frame, width=300)

    cv2.imshow('Redimensionar pelo Imutils',redimutils)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 500): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -45, 1.0)
    rotacao = cv2.warpAffine(frame, M, (w, h))

    cv2.imshow('Rotacao',rotacao)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 600): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    rotacaoim = imutils.rotate(frame, -45) # rotacao da imagem pela biblioteca imutils

    cv2.imshow('Rotacao Imutils',rotacaoim)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 700): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    rota = imutils.rotate_bound(frame, 45)

    cv2.imshow('Rotacao Modificada',rota)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 800): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    rota = imutils.rotate_bound(frame, 45)

    cv2.imshow('Rotacao Modificada',rota)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 800): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    desfoque = cv2.GaussianBlur(frame, (11, 11), 0)

    cv2.imshow('Desfocar o Video ',desfoque)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 900): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    output = frame.copy()
    #apresenta um retangulo sobre a imagem
    cv2.rectangle(output, (380, 360), (250, 100), (0, 0, 255), 5)

    cv2.imshow('Retangulo sobre o Video',output)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1000): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read()

    saida = frame.copy()
    cv2.circle(saida, (150, 50), 40, (255, 10, 0), -1)

    cv2.imshow('Circulo sobre o Video',saida)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1100): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    saida = frame.copy()
    cv2.line(saida, (60, 20), (200, 200), (0, 0, 255), 5)

    cv2.imshow('Linha sobre o Video',saida)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1100): #1822 frames
        break
    #print (i)
    i +=1

while(cap.isOpened()):
    ret, frame = cap.read() #fazer tramento do ultimo while

    saida = frame.copy()
    cv2.putText(saida, "OpenCV + Jerry!!!", (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('Frase aplicada sobre o Video',saida)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if (i == 1200): #1822 frames
        break
    #print (i)
    i +=1

cap.release()
cv2.destroyAllWindows()
