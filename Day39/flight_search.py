import requests
#-----------API INFO----------

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY= "TEQUILA_API_KEY"

class FlightSearch:
  
  def get_destination_code(self,city_name):
    
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apikey": TEQUILA_API_KEY}
    query = {
      "term": city_name,
      "location_type": "city"
    }
    
    response = requests.get(url= location_endpoint, headers = headers, params = query)
    
    result = response.json()["location"]
    code = results[0]['code']
    
    return code
