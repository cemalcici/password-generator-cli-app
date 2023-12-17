from string import ascii_letters, punctuation, digits
from random import choices

def generate_password(
    count: int=8,
    add_number: bool=False,
    add_symbol: bool=False
) -> str:
    letter_weight = [round(count * 0.2) for _ in range(len(ascii_letters))]
    number_weight = [round(count * 0.4) for _ in range(len(digits))]
    symbol_weight = [round(count * 0.4) for _ in range(len(punctuation))]
    
    if add_number:
        if add_symbol:
            return ''.join(choices(
                ascii_letters + digits + punctuation,
                weights=letter_weight+number_weight+symbol_weight,
                k=count
            ))
        return ''.join(choices(
            ascii_letters + digits,
            weights=letter_weight+number_weight,
            k=count
        ))
    return ''.join(choices(
        ascii_letters,
        weights=letter_weight,
        k=count
    ))
