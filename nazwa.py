# Tutaj pisz swój kod, młody padawanie ;-)
from microbit import *
import speech
from microbit import sleep

poem = [
    "there was a young man from koczala"
    "where he was born",
    "He returned to his hometown dark",
    "he went to the lake",
    "and I have been there forever",
    "EXTERMINATE",
]

# Loop over each line in the poem and use the speech module to recite it.
for line in poem:
    speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)