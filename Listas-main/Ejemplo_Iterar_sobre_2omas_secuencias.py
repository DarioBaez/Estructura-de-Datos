#Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con la función integrada zip(). 
preguntas = ['nombre', 'objetivo', 'sistema operativo'] 
respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux'] 
for pregunta, respuesta in zip(preguntas, respuestas): 
    print(f'¿Cual es tu {pregunta}?, la respuesta es: {respuesta}.')