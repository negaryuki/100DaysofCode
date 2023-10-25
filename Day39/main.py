from pprint import pprint
import requests 


#-----------END POINTS----------

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/62bf219154ff52ae3cb0172f15a57ff7/flightDeals/prices"


class DataManager:
  
  def __init__(self):
    self.destination_data = {}
    
  def get_destination_data(self):
    
    response = requests.get(url=SHEETY_PRICE_ENDPOINT)
    data = response.json()
    self.destination_data = data["prices"]
    
    
    return self.destination_data
    
    # creating a put request to update. IATA code data in Google sheets
    
    def update_destination_codes(self):
      
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            
            print(response.text)
