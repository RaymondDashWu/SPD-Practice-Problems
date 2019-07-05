def convert(number):
    rain_sound = ""
    if number % 3 == 0:
        rain_sound += "Pling"
    if number % 5 == 0:
        rain_sound += "Plang"
    if number % 7 == 0:
        rain_sound += "Plong"
    return str(number) if rain_sound == "" else rain_sound
