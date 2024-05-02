import random
weather_options = ['sunny','rainy','cloudy']

current_weather = weather_options[random.randint(0,len(weather_options)-1)]

match current_weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside")