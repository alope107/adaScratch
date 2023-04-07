# Price per square foot in cents
CARPET_TYPE_PRICE = {
    "berber": 509,
    "texture": 369,
    "pattern": 289
}

# Price in cents
CARPET_OPTION_PRICE = {
    "10yr warranty": 10000,
    "delivery": 3500,
    "installation": 7500,
    "stain guard": 3000
}

PROMO_CODE_TO_OPTION = {
    "ADAROCKS": "installation"
}

def cents_as_dollar_string(cents):
    return f"${cents//100}.{cents%100:02}"

def carpet_quote_estimator(room, carpet_type, options, promo_code):
    base_price = room[0] * room[1] * CARPET_TYPE_PRICE[carpet_type]

    option_total = 0
    for option in options:
        if promo_code in PROMO_CODE_TO_OPTION and \
           PROMO_CODE_TO_OPTION[promo_code] == option:
            continue

        option_total += CARPET_OPTION_PRICE[option]

    total_price = base_price + option_total

    print(f"The cost is {cents_as_dollar_string(total_price)}")

'''
### Example 1
#### Input (arguments of the function)
```
room = [10, 10]
carpet_type = "berber"
options = ["delivery", "installation"]
promo_code = ""
```
#### Output (printed by the function)
```
The cost is $619.00
```
'''
carpet_quote_estimator([10, 10], "berber", ["delivery", "installation"], "")

'''

### Example 2
#### Input (arguments of the function)
```
room = [8, 10]
carpet_type = "texture"
options = ["delivery", "10yr warranty", "stain guard"]
promo_code = ""
```
#### Output (printed by the function)
```
The cost is $460.20
```
'''
carpet_quote_estimator([8, 10], "texture", ["delivery", "10yr warranty", "stain guard"], "")
'''

### Example 3
#### Input (arguments of the function)
```
room = [9, 11]
carpet_type = "pattern"
options = ["delivery", "installation", "10yr warranty", "stain guard"]
promo_code = "ADAROCKS"
```
#### Output (printed by the function)
```
The cost is $451.11
```
'''

carpet_quote_estimator([9, 11], "pattern", ["delivery", "installation", "10yr warranty", "stain guard"], "ADAROCKS")