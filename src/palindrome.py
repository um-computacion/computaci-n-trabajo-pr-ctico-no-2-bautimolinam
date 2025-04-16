   
import re

def clean_text(text):
    
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def is_palindrome(text):
   
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]
