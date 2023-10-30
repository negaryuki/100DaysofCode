#—————— CONSTANTS —————
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Set the origin city IATA code to London
ORIGIN_CITY_IATA = "LON"

# Initialize data management, flight search, and notification manager objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get destination data from a data source (possibly a Google Sheet)
sheet_data = data_manager.get_destination_data()

# If the first row in the data doesn't have an IATA code, fetch codes for cities and update the data
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# Create a dictionary of destinations with IATA codes as keys
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

# Define the date range for flight searches (from tomorrow to six months from today)
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# Loop through each destination to check for flight prices
for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    # Print the flight price (for debugging purposes)
    print(flight.price)
    
    # If no flight is found, continue to the next destination
    if flight is None:
        continue

    # If the found flight price is lower than the recorded price, notify customers
    if flight.price < destinations[destination_code]["price"]:
        # Get customer emails and names
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        # Compose a notification message with flight details
        message = f"Low price found! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        # Add stopover information if there are stopovers in the flight
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stopover, via {flight.via_city}."

        # Send email notifications to customers
        notification_manager.send_emails(emails, message)
