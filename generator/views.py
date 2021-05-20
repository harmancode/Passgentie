import random

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    specials = list('!@#$%^&*()_+[]{}"/.,-=`')
    # Copy list by value, not by reference
    available_chars = characters[:]
    use_uppercase = False
    use_numbers = False
    use_special = False
    # Use at least once
    uppercase_location = 0
    numbers_location = 0
    specials_location = 0

    if request.GET.get('uppercase'):
        use_uppercase = True
        available_chars.extend(uppercase)

    if request.GET.get('numbers'):
        use_numbers = True
        available_chars.extend(numbers)

    if request.GET.get('special'):
        use_special = True
        available_chars.extend(specials)

    length = int(request.GET.get('length', 12))
    # Safety check
    if length < 6:
        length = 6
    elif length > 16:
        length = 16

    # Use at least once in random places
    uppercase_location = random.randint(3, length - 1)
    numbers_location = uppercase_location - 1
    specials_location = uppercase_location - 2

    generated_password = ''

    for x in range(0, length):
        # Make sure that every kind of character is included
        if x == 0:
            generated_password += random.choice(characters)
            continue
        elif x == uppercase_location and use_uppercase:
            generated_password += random.choice(uppercase)
            continue
        elif x == numbers_location and use_numbers:
            generated_password += random.choice(numbers)
            continue
        elif x == specials_location and use_special:
            generated_password += random.choice(specials)
            continue
        generated_password += random.choice(available_chars)

    return render(request, 'generator/password.html', {'password':generated_password})

def about(request):
    return render(request, 'generator/about.html')