import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

deelaytrax = []

trnam = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PyDeelay'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav"):
            deelaytrax.append(filepath)
            trnam.append(str(file[:-4]))

trlen = len(deelaytrax)

for y in range(trlen):

    atrack = deelaytrax[y]

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

    delln = random_number2(700, 1400)

    delAudio = AudioSegment.silent(duration = delln)

    delAudio2 = AudioSegment.silent(duration = delln)

    delitr = random_number2(2, 4)

    #defad = 1 / delitr

    defad2 = int(18 / delitr)

    altAudio = newAudio - defad2

    altAudionew = delAudio2 + altAudio

    #altAudiodelt = newAudio[0:0]

    for ctr in range(6):

        delAudio2 += delAudio

        altAudio = newAudio - defad2

        altAudionew = delAudio2 + altAudio

        newAudio = altAudionew.overlay(newAudio)

        #altAudiodelt = altAudiodelt.overlay(altAudionew)

        #altAudio = altAudiodelt - defad2

     
    oufil = "C:\\Users\\mysti\\Coding\\PyDeelay\\Delayout_" + trnam[y] + "_" + str(tim) + ".wav"    
    newAudio.export(oufil, format="wav")


print("")

print("Your delay file(s) can be found in the same folder as this code.")

print("")

##THE GHOST OF THE SHADOW##







