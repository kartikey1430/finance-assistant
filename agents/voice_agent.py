import speech_recognition as sr
import pyttsx3

from agents.retriever_agent import load_sample_docs, build_vector_index, get_relevant_info

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source, timeout=5)
        try:
            query = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service failed."

def main():
    print("🔄 Initializing agents...")
    docs = load_sample_docs()
    vector_db = build_vector_index(docs)

    query = listen()
    if "sorry" in query.lower():
        speak("Sorry, I couldn't understand you. Please try again.")
        return

    response = get_relevant_info(query, vector_db)
    print(f"🤖 Agent Response: {response}")
    speak(response if response else "Sorry, I could not retrieve any relevant information.")

if __name__ == "__main__":
    main()
