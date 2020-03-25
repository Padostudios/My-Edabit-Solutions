def hacker_speak(txt):
    return txt.replace("a","4").replace("e","3").replace("o","0").replace("i","1").replace("s","5") #my way

def hacker_speak(txt):
    return txt.translate(str.maketrans('aeios', '43105')) # way of a bustard

print(hacker_speak("javascript is cool"))