import speech_recognition as sr
from gtts import gTTS
import subprocess
from pathlib import Path
import sys
import time
import webbrowser




speakers = {
    'name':["alina","kolya","vlad","dima","andrey","pyetr"],
    "commands":{
        "greetings":["привет","приветик","ку","хай"],
        "launch_google_chrome":["запусти google chrome","включи google chrome"],
        "launch_youtube":["запуск youtube", "запусти youtube","youtube","включи youtube"],
        "google_query":["найди информацию", "хочу найти информацию", "google"],
        "write_to_notes":['запиши заметку', 'сделай заметку','хочу запомнить фразу','напиши заметку'],
        "set_timer":["установи таймер","засеки время", "засечь время"],
    }

           }

print(speakers["name"])
input_speaker = input("введите спикера:").lower()



# Основные функции для захвата звука и пере обработки речи в текст
def command_pronunciations():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Говорите команды/что надо записать...")
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source, phrase_time_limit=1.5)
            print("Распознаю...")
            text = recognizer.recognize_google(audio, language="ru-RU").lower()
            print(text)
            return text
    except sr.UnknownValueError:
        print("Скажите предложения по громче")

def file_not_found():
    speaker = Path(f"speakers/{input_speaker}/{input_speaker}_file_not_found.ogg")
    if speaker.exists():
        subprocess.run(["start", "", speaker.absolute()], shell=True)
        print("этот файл не найден")
    else:
        print("этот файл не найден")



def speaker_check(name_speaker):

    if input_speaker in speakers['name']:
        speaker = Path(f"speakers/{input_speaker}/{input_speaker}_hello.ogg")
        if speaker.exists():
            print(f"Ваш спикер {input_speaker} найден")
            subprocess.run(["start", "", speaker.absolute()], shell=True)
            time.sleep(4)

    else:
        print("Файл не найден")
        exit()




def launch_google_chrome():
    a = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    speaker = Path(f"speakers/{input_speaker}/{input_speaker}_launch_google_chrome.ogg")
    if speaker.exists():
        subprocess.run(["start", "", speaker.absolute()], shell=True)
        time.sleep(3)
        subprocess.Popen([a])
    else:
        file_not_found()


def write_to_notes():
    qwery = command_pronunciations()
    speaker = Path(f"speakers/{input_speaker}/{input_speaker}_launch_google_chrome.ogg")
    if speaker.exists():
        with open(r"notes/write_to_notes","a",encoding="utf-8") as file:
            file.write(f"🔳{qwery}\n")
            print(f"Ваша заметка записана")
            time.sleep(3)
    else:
        file_not_found()



def set_timer():
    qwery = command_pronunciations()

    hour = "час"
    minutes = "минут"
    second = "секунд"
    for i in minutes:
        if qwery.find(i):
            print("fsdf")





def launch_youtube():
    webbrowser.register('Google-chrome',None,webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
    speaker = Path(f"speakers/{input_speaker}/{input_speaker}_launch_google_chrome.ogg")
    if speaker.exists():
        webbrowser.get("Google-chrome").open("youtube.com/")
        time.sleep(3)

    else:
        file_not_found()

def google_query():
    qwery = command_pronunciations()
    webbrowser.register('Google-chrome', None,
                        webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
    speaker = Path(f"speakers/{input_speaker}/{input_speaker}_launch_google_chrome.ogg")
    if speaker.exists():
        webbrowser.get("Google-chrome").open(f"https://www.google.com/search?q=%D1%8F{qwery}")
        time.sleep(3)
    else:
        file_not_found()

def greetings():
    speaker = Path(f"speakers/{input_speaker}/{input_speaker}_greetings.ogg")

    if speaker.exists():
        subprocess.run(["start", "", speaker.absolute()], shell=True)
    else:
        file_not_found()



def main():
    qwery = command_pronunciations()
    for k,v in speakers["commands"].items():
        if qwery in v:
            globals()[k]()
        print("Ничего нету")

if __name__ == '__main__':
    speaker_check(input_speaker)
    main()



