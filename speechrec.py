import whisper
import pyttsx3
import os
import speech_recognition as sr

# Load Whisper model
model = whisper.load_model("base")

# TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech rate

# Speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            audio_data = audio.get_wav_data()
            result = model.transcribe(audio_data)
            command = result['text'].lower()
            print(f"You said: {command}")
            return command
        except Exception as e:
            print("Could not understand audio, please try again.")
            return ""

def process_command(command):
    if "بناؤ" in command or "کریئیٹ" in command:
        folder_name = command.split()[-1]
        create_folder(folder_name)
        speak(f"فولڈر {folder_name} ٺاهي ڇڏيو آهي")
    elif "ختم" in command or "ڈیلیٹ" in command:
        folder_name = command.split()[-1]
        delete_folder(folder_name)
        speak(f"فولڈر {folder_name} ختم ڪري ڇڏيو آهي")
    else:
        speak("مان توهان جي ڳالھ نٿو سمجھي سگھان. ٻيهر ڪوشش ڪريو.")

def create_folder(name):
    path = os.path.expanduser(f"~/Desktop/{name}")
    os.makedirs(path, exist_ok=True)

def delete_folder(name):
    path = os.path.expanduser(f"~/Desktop/{name}")
    if os.path.exists(path):
        os.rmdir(path)
    else:
        speak(f"فولڊر {name} نه مليو")

if __name__ == "__main__":
    speak("سلام! مان توهان جو مددگار آهيان. توهان کي ڇا ڪرڻو آهي؟")
    while True:
        command = listen()
        if command:
            process_command(command)
        if "خدا حافظ" in command or "بند" in command:
            speak("الوداع!")
            break
