import re


value_conversions = {
    "feet": 0.3048,
    "ft": 0.3048,
    "inches": 2.54,
    "ins": 2.54,
    "miles": 1.60934,
    "mi": 1.60934,
    "lb": 0.45359,
    "lbs": 0.45359,
    "pounds": 0.45359,
    "oz": 28.3495,
    "ounces": 28.3495,
    "gallons": 3.78541,
    "gal": 3.78541
}

unit_conversions = {
    "feet": "meters",
    "ft": "meters",
    "inches": "centimeters",
    "ins": "centimeters",
    "miles": "kilometers",
    "mi": "kilometers",
    "lb": "kilograms",
    "lbs": "kilograms",
    "pounds": "kilograms",
    "oz": "grams",
    "ounces": "grams",
    "gallons": "liters",
    "gal": "liters"
}

# TODO: Write a regex to capture imperial units! 

regex = re.compile(r"\d*\.\d+\s?\w+\.|\d*\.\d+\s?\w+|\d+\.\s?\w+|\d+\s?\w+")

def get_units(pattern):
    imp_pattern = find_units(pattern.group())       
    val_conv = value_conversions.get(imp_pattern[1])
    unit_conv = unit_conversions.get(imp_pattern[1])
    #substitute to metric
    new_value = round(val_conv*float(imp_pattern[0]), 3)
    converted_pattern = str(new_value) + " " + unit_conv
    #print("Converted_pattern: ", converted_pattern)
    return converted_pattern

    
#takes input as string. Outputs new metric value and metric units as string
def find_units(pattern):
    #function to determine which imperial units are in a pattern.
    #Input to get_units as tuple   
    imp_num = re.findall(r"\d*\.\d+|\d+", pattern, flags=re.IGNORECASE)[0]
    imp_unit = re.findall(r"([a-z]+)", pattern.lower(), flags=re.IGNORECASE)[0].lower()
    if imp_unit in ["feet", "ft", "f"]:
        return (imp_num, "feet")
    elif imp_unit in ["inches", "inch", "inc", "ins", "in"]:
        return (imp_num, "inches")
    elif imp_unit in ["miles", "mi"]:
        return (imp_num, "miles")
    elif imp_unit in ["pounds", "lbs", "lb"]:
        return (imp_num, "pounds")
    elif imp_unit in ["ounces", "ounce", "oz"]:
        return (imp_num, "ounces")
    elif imp_unit in ["gallons", "gallon", "gal"]:
        return (imp_num, "gallons")    
    else: 
        pass 

def convert_units(text):
    #calls get_units function to get substituted/converted patterns 
    new_txt = re.sub(regex, get_units, text)
    #output text with converted units
    return new_txt
