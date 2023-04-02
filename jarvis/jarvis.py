import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.GetProperty('voices')
print(voices[0].id)
engine.SetProperty('voice', voices[0].id)

def speak(audio):
    pass
