import pyaudio
import wave
import speech_recognition as RECo
import sqlite3 as sQ

#---------------------------------------------------------- GRABACION DEL MICROFONO--------------------------------------

# Configura las constantes
FORMATO = pyaudio.paInt16
CANALES = 1   #Se usa 1 para canal mono, 2 para canal stereo
RATE = 44100   #Esta es la frecuencia de muestreo
CHUNK = 1024   #Numero de cuadros de audio por buffer
SEGUNDOS_GRABACION = 5  #El numero de segundos que durara la grabacion de voz
NOMBRE_ARCHIVO_SALIDA = "grabacion.wav" #EL nombre que se le dara a la grabacion para guardarlo, 

# Inicia PyAudio
audio = pyaudio.PyAudio()

# Inicia la grabación
flujo = audio.open(format=FORMATO, channels=CANALES, #crea un objeto llamado flujo que sonectara al microfono, con los parametros ya inicializados
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("grabando voz...")
cuadros = []

for i in range(0, int(RATE / CHUNK * SEGUNDOS_GRABACION)):
    datos = flujo.read(CHUNK)
    cuadros.append(datos)          #ESta lista almacena por 5 segundos,varios cuadros de 1024 datos extraidos del microfono
print("grabación de voz terminada")

# Detiene la grabación
flujo.stop_stream() #Detiene la grabacion
flujo.close() #Cierra la grabacion
audio.terminate() #Cierra la conexion al sistema de audio (mic y altavoces)

#-------------------------------------------------------SE TRANSFORMA A WAV-----------------------------------------------
# Guarda la grabación en un archivo WAV
archivo_wave = wave.open(NOMBRE_ARCHIVO_SALIDA, 'wb') #Abre el archivo de tipo .wav en escritura binaria
archivo_wave.setnchannels(CANALES)                    #Este metodo le pone los canales en los que va a trabajar el audio
archivo_wave.setsampwidth(audio.get_sample_size(FORMATO))
archivo_wave.setframerate(RATE)
archivo_wave.writeframes(b''.join(cuadros))           #La grabacion relizada por el microfono y guardada en la lista cuadros, se guardara en un archivo de tipo .wav
archivo_wave.close()                                #Se cierra el archivo ya modificado


#-------------------------------------------------------SE ABRE EL ARCHIVO WAV YA GUARDADO Y LO LEE EL SPEECH, LO TRANSFORMA A TEXTO
# Crea una instancia de Recognizer
r = RECo.Recognizer()

# Abre el archivo de audio
with RECo.AudioFile(NOMBRE_ARCHIVO_SALIDA) as fuente:
    # Lee el archivo de audio
    audio = r.record(fuente)

    try:
        # Usa el reconocimiento de voz de Google para transformar el audio a texto
        texto = r.recognize_google(audio, language='es-ES') #Selecciona el idioma en paremtros, junto al audio ya capturado
        print("El audio dice: " + texto) #Imprime el texto ya transformado
    except RECo.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio")
    except RECo.RequestError as e:
        print("No se pudo solicitar resultados de Google Speech Recognition; {0}".format(e))

#-------------------------------------------------------- ABRE LA BBDD y GUARDA LOS DATOS si son nuevos---------------------------------------

Conexion = sQ.connect("BaseDatosAudio.db")
Cursor = Conexion.cursor()
Cursor.execute(f"SELECT * FROM Reconocimientos WHERE VozTexto == '{texto}'")
Existencia = Cursor.fetchall()
if Existencia:
    print("Ese texto ya habia sido almacenado")
else:
    archivo_wave = wave.open("grabacion.wav", 'rb')            #Se abre en lectura binaria
    audio = archivo_wave.readframes(archivo_wave.getnframes())
    Cursor.execute("INSERT INTO Reconocimientos(VozTexto, GrabacionWB) VALUES(?,?)", (texto, audio))
    Conexion.commit()
Conexion.close()



