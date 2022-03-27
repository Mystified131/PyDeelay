import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

stuttertrax = []

trnam = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PyStutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav"):
            stuttertrax.append(filepath)
            trnam.append(str(file[:-4]))

trlen = len(stuttertrax)

for y in range(trlen):

    atrack = stuttertrax[y]

    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    print("")

    print("Please wait. Working on: " + atrack)

    print("")
           
    newAudio = AudioSegment.from_wav(atrack)

    audlen = len(newAudio)

    delln = random_number2(100, 800)

    delAudio = AudioSegment.silent(duration = delln)

    delitr = random_number2(4, 6)

    defad = 1 / delitr * 18

    defad2 = .4 * defad

    altAudio = newAudio - defad2

    altAudiodelt = newAudio[0:0]

    for ctr in range(delitr):

        altAudionew = delAudio + altAudio

        altAudionew = altAudionew - defad

        altAudio = altAudio + delAudio

        altAudiodelt = altAudionew.overlay(altAudio)

        altAudio = altAudiodelt - defad2

     
    oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Delayout_" + trnam[y] + "_" + str(tim) + ".wav"    
    altAudio.export(oufil, format="wav")


print("")

print("Your delay file(s) can be found in the same folder as this code.")

print("")

##THE GHOST OF THE SHADOW##







