from .functions import generate_password

k = input('How many characters your password? (default 8)')
add_num = input('Does your password contain numbers? [Y/n]')
add_symbl = input('Does your password contain symbols? [Y/n]')

k = 8 if k == '' else int(k)

print("Generated Password:")
print(generate_password(
    count=k,
    add_number=add_num.upper() == 'Y',
    add_symbol=add_symbl.upper() == 'Y'
))