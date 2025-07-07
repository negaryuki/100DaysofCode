import requests
import json
from datetime import datetime
import time
from random import randint

# Product configuration
product_name = "RTX 3080 FE"

# API URL for checking availability (includes location & product SKU)
URL = "https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&locations=938%7C202%7C617%7C203%7C57%7C926%7C977%7C233%7C930%7C927%7C62%7C622%7C931%7C245%7C207%7C954%7C795%7C916%7C910%7C544%7C932%7C237%7C200%7C965%7C990%7C956%7C943%7C937%7C942%7C223%7C985%7C925&postalCode=M8W&skus=15463567"

# HTTP request headers (simulate a browser request)
headers = {
    'authority': 'www.bestbuy.ca',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4159.2 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/15463567',
    'accept-language': 'en-US,en;q=0.9'
}


def main():
    quantity = 0
    attempt = 1  # Track number of attempts

    while quantity < 1:
        try:
            # Send request to Best Buy API
            response = requests.get(URL, headers=headers)
            response.raise_for_status()

            # Decode JSON response
            response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))

            # Check remaining quantity from the first location
            quantity = response_formatted['availabilities'][0]['shipping']['quantityRemaining']

            if quantity < 1:
                print(f"Time: {datetime.now()} | Attempt: {attempt} | No stock")
                attempt += 1
                time.sleep(randint(1, 5))  # Sleep to avoid being blocked (optional but recommended)
            else:
                print(f"🚨 {product_name} available to ship!\nQuantity: {quantity}")
                alert(f"🚨 {product_name} is available to ship\nQuantity: {quantity}\n{headers['referer']}")
                time.sleep(60)  # Wait before rechecking in case it's a temporary restock
                main()  # Recursive call to continue monitoring

        except Exception as e:
            print(f"Error on attempt {attempt}: {e}")
            time.sleep(10)
            attempt += 1


def alert(bot_message):
    # Configure your Telegram bot token and chat ID
    bot_token = "INSERT_BOT_TOKEN"
    bot_chat_id = "INSERT_CHAT_ID"

    # Telegram API URL
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={bot_message}'

    # Send message
    response = requests.get(send_text)
    return response.json()


# Main script execution with basic error handling
try:
    main()
except Exception as e:
    print(f'Fatal Error: {e} — retrying after 2 minutes...')
    time.sleep(120)
    main()
