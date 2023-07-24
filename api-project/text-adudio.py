from gtts import gTTS
from playsound import playsound

audio = 'interview.mp3'
language = 'en'

try:
    sp = gTTS(text='Enter the text wich y want to convert into audio file.',
          lang=language,
          slow=False)

except FileNotFoundError as fnf_error:
    print(fnf_error)

sp.save(audio)
playsound(audio)
