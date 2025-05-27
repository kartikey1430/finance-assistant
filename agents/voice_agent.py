import speech_recognition as sr
import pyttsx3
from data_ingestion.api_agent import get_asia_tech_data

def analyze_sentiment(change):
    if change > 1:
        return "positive"
    elif change < -1:
        return "negative"
    return "neutral"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio)
        print("📝 Transcription:", transcript)
        return transcript
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except sr.RequestError:
        print("❌ Speech Recognition API unavailable")
        return None

def handle_voice_command():
    query = transcribe_speech()
    if query:
        speak(f"You said: {query}. Fetching stock data now.")
        data = get_asia_tech_data()
        if not data:
            speak("Sorry, I couldn't fetch any stock data.")
            return

        for stock in data:
            sentiment = analyze_sentiment(stock['change_percent'])
            summary = f"{stock['ticker']} is showing a {sentiment} change of {stock['change_percent']} percent."
            print(summary)
            speak(summary)

if __name__ == "__main__":
    handle_voice_command()
