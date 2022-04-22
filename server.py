import os
import json
from flask import Flask, request, make_response
from twilio.twiml.messaging_response import MessagingResponse

from pdf_util import generate_pdf
from drive_appscript import upload_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def received_message():
	body = request.values.get('Body', None)

	resp = MessagingResponse()

	filename = "./cardapio.pdf"

	if body == 'cardapio':
		msg = resp.message("Cardápio dessa semana: ")

		generate_pdf(filename)

		with open(filename, "rb") as f:
			data = upload_file(f.read())

		msg.media(data["download"])
	else:
		resp.message("Envie \"cardapio\" para receber o cardápio dessa semana.")

	return str(resp)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 8000))
	app.run(host='0.0.0.0', port=port)