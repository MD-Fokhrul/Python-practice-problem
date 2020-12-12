def convert(number):
    if len(div_3(number)) or len(div_5(number)) or len(div_7(number)) != 0:
        return div_3(number) + div_5(number) + div_7(number)
    else:
        return str(number)
    
    
    
def div_3(n):
    if n % 3 == 0:
        return "Pling"
    else:
        return ""
            
def div_5(n):
    if n % 5 == 0:
        return "Plang"
    else:
        return ""

def div_7(n):
    if n % 7 == 0:
        return "Plong"
    else:
        return ""
