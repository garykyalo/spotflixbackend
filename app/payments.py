import requests,base64, datetime
from requests.auth import HTTPBasicAuth

from config import Config


## Generate token 
def generate_token():
    api_url = Config.TOKEN_API_URL
    response = requests.get(api_url, auth=HTTPBasicAuth(Config.CONSUMER_KEY, Config.CONSUMER_SECRET))
    json_response = response.json()
    access_token = json_response['access_token']
    return access_token



## Stk push logic 
def stk_push_function(phone_number, amount):  
    access_token = generate_token()
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f'{Config.BUSINESS_SHORT_CODE}{Config.LIPA_NA_MPESA_ONLINE_PASSKEY}{timestamp}'.encode('utf-8')).decode('utf-8')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        'BusinessShortCode': Config.BUSINESS_SHORT_CODE,
        'Password': password,
        'Timestamp': timestamp,
        'TransactionType': 'CustomerBuyGoodsOnline',
        'Amount': amount,
        'PartyA': phone_number,
        'PartyB': Config.TILL_NUMBER,
        'PhoneNumber': phone_number,
        'CallBackURL': Config.CALLBACK_URL,
        'AccountReference': 'Test123',
        'TransactionDesc': 'Payment for goods'
    }

    response = requests.post(Config.LIPA_NA_MPESA_ONLINE_URL, json=payload, headers=headers)
    response_data = response.json()

    if response_data.get('ResponseCode') == '0':
        status = 200
        message = 'Payment request sent successfully.'
    else:
        status = 400
        message = f"Error: {response_data.get('errorMessage', 'Unknown error')}"
    return {"status": status, "message": message}



