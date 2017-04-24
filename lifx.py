import requests

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
headers = { "Authorization": "Bearer %s" % token,}

def menu():
    print()
    print('0. exit')
    print('1. Turn On Light')
    print('2. Turn Off Light')
    print('3. Toggle Power')
    print('4. Breath Effect')
    print('5. Pulse Effect')
    print('6. Set Brightness')
    print('7. Set Color')
    choice = (input('enter choice: '))
    return choice

def myMenu():
    choice = menu()
    while choice != "0":
        if choice == "1":
            turn_on(headers)
            choice = menu()
        elif choice == "2":
            turn_off(headers)
            choice = menu()
        elif choice == "3":
            toggle_power(headers)
            choice = menu()
        elif choice == "4":
            breath_effect(headers)
            choice = menu()
        elif choice == "5":
            pulse_effect
            choice = menu()
        elif choice == "6":
            set_brightness(headers)
            choice = menu()
        elif choice == "7":
            set_color(headers)
            choice = menu()
        elif type(choice) == int:
            print('choice must be an int')
        else:
            print('Invalid option')
            choice = menu()
    print()


def turn_on(headers):
    payload = {"power": "on",}
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

def turn_off(headers):
    payload = {"power": "off",}
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

def toggle_power(headers):
    response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)

def breath_effect(headers):
    data = {"period": 6, "cycles": 6,"color": "blue",}
    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=data, headers=headers)

def pulse_effect(headers):
    data = {"period": 2, "cycles": 5, "color": "green",}
    response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', data=data, headers=headers)

def set_brightness(headers):
    amount = float(input("Enter brightness betwwen 0 and 10: "))
    divisor = amount/10
    payload = {"power": "on", "brightness": divisor}
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

def set_color(headers):
    color = str(input("Enter a color: "))
    payload = {"power": "on", "color": color}
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

myMenu()
