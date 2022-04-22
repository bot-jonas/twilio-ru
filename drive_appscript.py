import requests
import base64
import os

def upload_file(file_bytes):
	APP_ID = os.environ.get("GOOGLE_APP_ID")
	BASE_URL = f"https://script.google.com/macros/s/{APP_ID}/exec"
	
	b64 = base64.b64encode(file_bytes)
	r = requests.post(BASE_URL, data={"file": b64})

	return r.json()