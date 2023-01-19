import speech_recognition as SRG

#To recoginize the sound and intialize the Recoginizer 
store = SRG.Recognizer()

#Use Microphone Audio Input as source
with SRG.Microphone() as src:
    print("Please Speak Something")

    #Record the audio adn specify the duration of audio
    audio_input = store.record(src, duration=7)
    print("Processing What You Said.")

    try:
        #recoginize the audio and output text
        text_output = store.recognize_google(audio_input)
        print("Here is what you said: ", text_output)
    except:
        print("Oops! Some error occured during audio processing")
