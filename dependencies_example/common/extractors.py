import re

# Extract email addresses from a text using regex
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

# Extract hashtags from a text using regex
def extract_hashtags(text):
    pattern = r'\#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags

# Extract URLs from a text using regex
def extract_urls(text):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(pattern, text)
    return urls

# Extract phone numbers from a text using regex
def extract_phone_numbers(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

# Extract mentions from a text using regex
def extract_mentions(text):
    pattern = r'\@\w+'
    mentions = re.findall(pattern, text)
    return mentions

# Example usage
text = "I love #Python programming. Email me at john@example.com or visit https://example.com"
print(extract_emails(text))
print(extract_hashtags(text))
print(extract_urls(text))
print(extract_phone_numbers(text))
