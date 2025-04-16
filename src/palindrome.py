
   
import re

def clean_text(text):
    
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def is_palindrome(text):
   
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    try:
        while True:
            user_input = input("Ingrese una palabra o frase: ")
            if is_palindrome(user_input):
                print(f'"{user_input}" es un palíndromo\n')
            else:
                print(f'"{user_input}" no es un palíndromo\n')
    except KeyboardInterrupt:
        print("\nPrograma terminado.")



