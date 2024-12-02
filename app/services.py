billing_durations = [
    {"period": "Monthly", "multiplier": 1},
    {"period": "Semi-annually", "multiplier": 6},
    {"period": "Annually", "multiplier": 12}
]

equipment_option = [
    {"option": "Purchase Equipment", "value": 2000},
    {"option": "Pay in Installments", "value": 500},
    {"option": "Company Property", "value": 0}
]

def calculate_amount(amount, billing_period, equipment_choice):
    billing_multiplier = list(
        map(lambda item: item["multiplier"], filter(lambda item: item["period"] == billing_period, billing_durations))
    )[0]  
    equipment_value = list(
        map(lambda item: item["value"], filter(lambda item: item["option"] == equipment_choice, equipment_option))
    )[0]  
    total_amount = (amount * billing_multiplier) + equipment_value
    return total_amount

