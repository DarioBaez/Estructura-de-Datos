import pyaudio

# Configuración
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Obtener información del dispositivo de audio
device_info = p.get_default_input_device_info()

# Obtener el número máximo de canales de entrada
CHANNELS = int(device_info['maxInputChannels'])

# Abrir stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

# Bucle principal
try:
    while True:
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)
except KeyboardInterrupt:
    print("* done recording")

# Cerrar stream
stream.stop_stream()
stream.close()
p.terminate()
