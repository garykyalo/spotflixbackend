import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") 

    ## payment configurations 
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    BUSINESS_SHORT_CODE = os.environ.get("BUSINESS_SHORT_CODE")
    TILL_NUMBER = os.environ.get("TILL_NUMBER")
    LIPA_NA_MPESA_ONLINE_PASSKEY = os.environ.get("LIPA_NA_MPESA_ONLINE_PASSKEY")
    LIPA_NA_MPESA_ONLINE_URL = os.environ.get("LIPA_NA_MPESA_ONLINE_URL")
    CALLBACK_URL= os.environ.get("CALLBACK_URL")
    TOKEN_API_URL = os.environ.get("TOKEN_API_URL")


