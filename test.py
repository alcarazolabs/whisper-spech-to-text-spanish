# pip install git+https://github.com/openai/whisper.git

import whisper
# Modelos probados: tiny, base, small y medium.
# tiny 27sg
# small 25sg aprox (Dio mejores resultados)
# medium 1.10 min

# https://github.com/openai/whisper
model = whisper.load_model("small")
result = model.transcribe("ia2.wav")

print(result["text"])

# Tiempo promedio aws: 24sg Se compara y es parecido a whisper small.