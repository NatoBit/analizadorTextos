EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PHONE_PATTERN = r'\+?\d[\d -]{8,12}\d'
DATE_PATTERN = r'\b\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}\b'
URL_PATTERN = r'(https?://\S+|www\.\S+)'
IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# Diccionario para manejar los patrones de forma más fácil
PATTERNS = {
    "email": EMAIL_PATTERN,
    "phone": PHONE_PATTERN,
    "date": DATE_PATTERN,
    "url": URL_PATTERN,
    "ip": IP_PATTERN,
}