
import base64
from .constants import SHORT_URL_LEN

# Generates a random Base62 string containing SHORT_URL_LEN characters
def generate_short_url(original_url):
    # Using base64 to encode the original url and returning first 5 letters of it
    message = original_url
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    short_url = base64_message[:SHORT_URL_LEN]
    return short_url