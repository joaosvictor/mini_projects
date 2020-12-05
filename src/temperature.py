from time import sleep 
def convert_from_to():
    
    # driver code  
    print('Choose some temperature below to convert')
    print('-'*20)
    option = 0
    while option != 7:
        print('''        1. Convert Celsius to Fahrenheit.
        2. Convert Celsius to Kelvin.
        3. Convert Fahrenheit to Celsius.
        4. Convert Fahrenheit to Kelvin.
        5. Convert Kelvin to Fahrenheit.
        6. Convert Kelvin to Celsius.
        7. Finish the program.
        ''')
        option = int(input('Which of the above do you want to perform ? ' ))
        print('')
        sleep(0.5)

        if option == 1:
            number=float(input('Tell me the temperature: ' ))
            a= number * 9/5 + 32
            mins = f"{a:.2f}"
            print('This is the temperature performed: {}°F'.format(mins))
            break
        elif option == 2:
            number=float(input('Tell me the temperature: ' ))
            a= number + 273.15
            mins = f"{a:.2f}"
            print('This is the temperature performed: {}K'.format(mins))
            break
        elif option == 3:
            number=float(input('Tell me the temperature: ' ))
            a=(number - 32) * 5/9
            mins = f"{a:.2f}"
            print('This is the temperature performed: {}°C'.format(mins))
            break
        elif option == 4:
            number=float(input('Tell me the temperature: ' ))
            a=(number - 32) * 5/9 + 273.15
            mins = f"{a:.2f}"
            print('This is the temperature performed: {}K'.format(mins))
            break
        elif option ==5:
            number=float(input('Tell me the temperature: ' ))
            a=(number - 273.15)* 9/5 + 32
            mins = f"{a:.2f}"
            print('This is the temperature performed: {}°F'.format(mins))
            break
        elif option ==6:
            number=float(input('Tell me the temperature: ' ))
            a=number - 273.15
            mins = f"{a:.2f}"
            print('This is the temperature performed: {}°C'.format(mins))
            break
        elif option ==7:
            number=float(input('Tell me the temperature: ' ))
            print('Finishing...')
        else:
            print('Ops... this option is not valid! Try again.')
            continue 
        print(' ')
        sleep(0.5)
        break

convert_from_to()
