from fastapi import APIRouter, HTTPException
from fastapi import Request
from . payments import stk_push_function
from .services import calculate_amount


router = APIRouter()
@router.api_route("/", methods=["GET", "POST"])
def hello_world():
    return {"message": "Hello, World!"}


@router.api_route("/api/payment", methods=["GET", "POST"])
async def Payment(request: Request):
    try:
        payment_data = await request.json()
  
        phone_number = payment_data.get("phoneNumber")
        billingDuration = payment_data.get("billingDuration")
        equipmentOption = payment_data.get("equipmentOption")
        if phone_number and phone_number.startswith("0"):
            phone_number = "254" + phone_number[1:]
        amount = int(payment_data.get("packagePrice").replace(",",""))
        total_amount = calculate_amount(amount,  billingDuration, equipmentOption)
    
        message = stk_push_function(phone_number, total_amount)
    
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the payment data.")
    

@router.api_route("/callback", methods=["GET", "POST"])
async def Callback(request: Request):
    callback_data = await request.json()
  
       
    return "OK", 200 
    

