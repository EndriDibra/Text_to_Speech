# Using the required libraries
from gtts import gTTS
from playsound import playsound

# Initializing the type of audio and language
audio = 'speech.mp3'
language = "en"

# Taking input:(text) from the user
print("Please enter your text")
text = input()

# Initializing input, language
sp = gTTS(text=text, lang=language, slow=False)

# The input from the user will be saved and played by the computer using machine-voice
sp.save(audio)
playsound(audio)
