import os
from dotenv import load_dotenv

load_dotenv(override=True)

print("API KEY:")
print(os.getenv("GOOGLE_API_KEY"))