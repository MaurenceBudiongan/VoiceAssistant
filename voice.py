import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import time
import pygame
import threading


engine = pyttsx3.init()
engine.setProperty("rate", 160) 
engine.setProperty("volume", 1.0) 


pygame.mixer.init()


multo_lyrics = [
    (23, "Humingang malalim, pumikit na muna"),
    (32, "At baka-sakaling namamalikmata lang"),
    (42, "Ba't nababahala? 'Di ba't ako'y mag-isa?"),
    (50, "'Kala ko'y payapa, boses mo'y tumatawag pa"),
    (61, "Binaon naman na ang lahat"),
    (65, "Tinakpan naman na 'king sugat"),
    (69, "Ngunit ba't ba andito pa rin?"),
    (74, "Hirap na 'kong intindihin"),
    (78, "Tanging panalangin, lubayan na sana"),
    (87 , "Dahil sa bawat tingin, mukha mo'y nakikita"),
    (97 , "Kahit sa'n man mapunta ay anino mo'y kumakapit sa 'king kamay"),
    (106 , "Ako ay dahan-dahang nililibing nang buhay pa"),
    (115 , "Hindi na makalaya"),
    (120 , "Dinadalaw mo 'ko bawat gabi"),
    (124, "Wala mang nakikita"),
    (129, "Haplos mo'y ramdam pa rin sa dilim"),
    (133 , "Hindi na nananaginip"),
    (138, "Hindi na ma-makagising"),
    (143 , "Pasindi na ng ilaw"),
    (147, "Minumulto na 'ko ng damdamin ko"),
    (151, "Ng damdamin ko"),
    (165, "Hindi mo ba ako lilisanin?"),
    (133, "Hindi pa ba sapat pagpapahirap sa 'kin?"),
    (138, "Hindi na ba ma-mamamayapa?"),
    (143, "Hindi na ba ma-mamamayapa?"),
    (148, "Hindi na makalaya"),
    (153, "Dinadalaw mo 'ko bawat gabi"),
    (158, "Wala mang nakikita"),
    (163, "Haplos mo'y ramdam pa rin sa dilim"),
    (168, "Hindi na nananaginip"),
    (173, "Hindi na ma-makagising"),
    (178, "Pasindi na ng ilaw"),
    (183, "Minumulto na 'ko ng damdamin ko"),
    (188, "Ng damdamin ko"),
    (193, "Hindi mo ba ako lilisanin?"),
    (198, "Hindi pa ba sapat pagpapahirap sa 'kin?"),
    (203, "Hindi na ba ma-mamamayapa?"),
    (208, "Hindi na ba ma-mamamayapa?"),
]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    

    try:
        with sr.Microphone() as source:
            print("Aray koo...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    except AttributeError:
        print("Microphone not available. Please type your command:")
        return input().lower()
    except Exception as e:
        print(f"Error accessing microphone: {e}")
        print("Please type your command:")
        return input().lower()

    try:
        command = r.recognize_google(audio, language="en-US")
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def display_lyrics(music_path):
    """Display lyrics synchronized with the music"""
    try:

        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        
        start_time = time.time()
        current_lyric_index = 0
        

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n🎵 You can now relapse: Multo by Cup of Joe")
        print("=" * 60)
        print("\n♪ Instrumental intro ♪\n")
        print("Lyrics will start in 23 seconds...")
        

        time.sleep(23)
        

        while pygame.mixer.music.get_busy() or current_lyric_index < len(multo_lyrics):
            elapsed_time = time.time() - start_time
            

            if (current_lyric_index < len(multo_lyrics) and 
                elapsed_time >= multo_lyrics[current_lyric_index][0]):
      
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n🎵 Now playing: Multo by Cup of Joe")
                print("=" * 60)
                print(f"\n{multo_lyrics[current_lyric_index][1]}\n")
                current_lyric_index += 1
            
            time.sleep(0.1) 
            
    except Exception as e:
        print(f"Error playing music: {e}")
        speak("Sorry, I couldn't play the music.")

def play_music():
    """Play music with synchronized lyrics display"""
    music_path = "C:/Users/II/Desktop/voice/Cup_of_Joe_-_Multo_(mp3.pm).mp3"
    
    if os.path.exists(music_path):
     
        lyrics_thread = threading.Thread(target=display_lyrics, args=(music_path,))
        lyrics_thread.daemon = True
        lyrics_thread.start()
        
        speak("Playing Multo by Cup of Joe. Lyrics will start in 23 seconds.")
    else:
        speak("Music file not found. Please check the file path.")
        print(f"File not found: {music_path}")

def main():
    speak("Hello! How can I help you?")
     

    try:
        sr.Microphone()
        print("Microphone is ready!")
    except AttributeError:
        print("Microphone not available. You'll need to type commands.")
        speak("Microphone not detected. You'll need to type your commands.")
    
    while True:
        command = listen()

        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "play music" in command or "multo" in command:
            play_music()

        elif "stop music" in command:
            pygame.mixer.music.stop()
            speak("Music stopped")

        elif "stop" in command or "exit" in command:
            pygame.mixer.music.stop()
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()