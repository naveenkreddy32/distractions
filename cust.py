from pydub import AudioSegment
import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say(".")

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

#voices = engine.getProperty('voices')
#male_voice = voices[0].id
#female_voice = voices[1].id


# List of distraction phrases
phrases = [
    "Hey, you! That’s the wrong answer, but I love the confidence!",
    "You’re so close, in the wrong direction!",
    "You’re on fire! Unfortunately, it’s a dumpster fire.",
    "Wow, that was almost right… if we were playing a different game.",
    "Your brain just did a backflip… and landed on its face.",
    "You’re thinking outside the box. The problem is, the answer is inside the box.",
    "Mathematically, your answer makes no sense… but I respect the hustle.",
    "Good try! You just invented a new word!",
    "I appreciate the effort, even though it’s completely useless.",
    "I’m not saying your answer is bad, but even autocorrect is confused.",
    "You got it! …Oh wait, never mind.",
    "Trust your instincts! Unless your instincts are that.",
    "I have faith in you… very, very little, but it’s there!",
    "If you had 5 more minutes… you’d still be wrong.",
    "You were right… in an alternate universe.",
    "I admire your commitment to being incorrect.",
    "I think you just unlocked a new level of confusion.",
    "Think faster! Or at least, think better!",
    "If that was an SAT question, you'd get partial credit… maybe.",
    "Your brain and the right answer are in two different time zones.",
    "Hey, red-shirt guy! You look confident. Too bad you’re confidently wrong.",
    "Oh wow! That was… definitely an answer.",
    "Whoever just whispered an answer—blame them if it’s wrong!",
    "Someone on your team knows the answer… too bad it’s not you!",
    "You’re not overthinking this, you’re just thinking incorrectly.",
    "That was a bold move. Boldly wrong.",
    "If this were a history test, that answer might be right. But it’s not.",
    "Fun fact: The answer is NOT what you just said.",
    "Let’s all take a moment to appreciate how wrong that was."
]

# Silence (10 seconds)
silence_duration = 5000  # 10 sec in milliseconds
silence_audio = AudioSegment.silent(duration=silence_duration)
final_audio = AudioSegment.empty()

background_music = AudioSegment.from_file("/Users/naveenkreddynagireddy/Downloads/funny-comedy-cartoon-background-music-294730.mp3") - 15 # Your background music file

# Set the background music volume (optional)
# background_music = background_music - 15  # Lower the volume (optional)

for i, phrase in enumerate(phrases):
    temp_filename = f"temp_{i}.wav"

    # if i % 2 == 0:
    #     engine.setProperty('voice', male_voice)  # Male voice for even phrases
    # else:
    #     engine.setProperty('voice', female_voice)  # Female voice for odd phrases


    engine.save_to_file(phrase, temp_filename)
    engine.runAndWait()

    # Read MP3 file explicitly specifying the format
    phrase_audio = AudioSegment.from_file(temp_filename)

    phrase_audio = phrase_audio + silence_audio

    final_audio += phrase_audio

    os.remove(temp_filename)  # Clean up temp file

# Overlay the background music (adjust the volume if necessary)
music_duration = len(final_audio)  # Length of the generated speech
background_music = background_music[:music_duration]  # Trim music to match speech length
final_audio = final_audio.overlay(background_music)

# Export final MP3
final_audio.export("funny_distraction.mp3", format="mp3")
print("MP3 file 'funny_distraction.mp3' created successfully!")
