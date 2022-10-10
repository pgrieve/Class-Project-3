## Intro- printed
hello = input("Welcome to my Weather Program! -- Press Enter to Continue")

import json, requests


#App id as signed up from openweathermap.org
APPID = '780ebeaf90ee70836c71fc164346ad42'


#format of url when zipcode is given
def get_forecasturl_zipcode(zipcode):
    url = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&appid=%s' % (zipcode, APPID) 
    return  url


#format of url when city is given
def get_forecasturl_city(city):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (city, APPID)
    return url 


def main():

    


        #Ask the user for zip code or city
        user_input = input('Enter zip code or city: ')


        #Get the correct url based on input
        if user_input.isdecimal():
            url = get_forecasturl_zipcode(user_input)
        else :
            url = get_forecasturl_city(user_input)
        
        response = requests.get(url)


        #Check whether the connection was established
        try:
            response.raise_for_status()
            print('Connection was successful')
        except:
            print('Connection was not succesful')
           


        weathers = json.loads(response.text)['list']
         
        #Display the weather information to the user
        print('Weather today is ' + weathers[0]['weather'][0]['main'])
        print('Weather tomorrow is ' + weathers[1]['weather'][0]['main'])

        option = str(input('Would you like to enter another weather forecast, Yes or No? ')).lower().strip()
      #while loop for a yes selection or to exit the program (and to catch input errors)
        while not (option == 'yes' or option == 'no'): 
          option = str(input('You did not enter a valid selection.\n'
    'Please enter Yes for another forecast or No to exit: ')).lower().strip()
        if option == 'yes':
          print('')
          main() # this calls your program to execute again if input is "yes"
        if option == 'no':
          print('Thank you for using the weather forecast. Goodbye')



if __name__ == "__main__":
    main()