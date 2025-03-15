import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)
wikipedia.set_lang("pt")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo")
        command = r.recognize_google(audio, language='pt-br')
        print("Usuário falou: " + command + "\n")
    except Exception as e:
        print(e)
        speak("Não entendi")
        return ""
    return command


if __name__ == "__main__":
    speak("Assistente Digita foi ativada")
    speak("Como eu posso te ajudar?")

    while True:
        command = getCommand().lower()

        # Comando para procurar na Wikipedia
        if 'wikipédia' in command:
            command = command.replace("wikipédia", "")
            command = command.replace("procure na", "")
            command = command.replace("pesquise na", "")

            results = wikipedia.summary(command, sentences=2)
            speak("De Acordo com a Wikipédia")
            speak(results)

        # Comando para abrir o Youtube
        elif 'youtube' in command:
            speak("Abrindo o Youtube")
            webbrowser.open("youtube.com")
            exit(0)

        # Comando para abrir o Google
        elif 'google' in command:
            speak("Abrindo o Google")
            webbrowser.open("google.com")
            exit(0)

        # Comando para abrir o site do Vasco
        elif 'site do vasco' in command:
            speak("Abrindo o site oficial do Vasco")
            webbrowser.open("https://www.crvasco.com.br/")

        # Comando para pesquisar as melhores músicas de 2025 no YouTube
        elif 'melhores músicas no youtube 2025' in command:
            speak("Pesquisando as melhores músicas de 2025 no YouTube")
            webbrowser.open("https://www.youtube.com/results?search_query=melhores+músicas+2025")

        # Comando para pesquisar as melhores músicas de rock no YouTube
        elif 'melhores músicas de rock' in command:
            speak("Pesquisando as melhores músicas de rock no YouTube")
            webbrowser.open("https://www.youtube.com/results?search_query=melhores+músicas+de+rock")

        # Comando para abrir o C:\
        elif 'c2 pontos' in command:
            speak("Abrindo o C:")
            webbrowser.open("C://")

        # Comando para abrir a calculadora
        elif 'calculadora' in command:
            speak("Abrindo a Calculadora")
            loc = "C:\\Windows\\System32\\calc.exe"
            os.startfile(loc)

        # Comando de despedida
        elif 'tchau' in command:
            speak("Tchau Tchau")
            exit(0)
