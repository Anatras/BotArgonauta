from pyrogram import Client, Filters, Emoji, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import re
import time

app = Client(
    "Argonauta",
    bot_token="885550564:AAGN29Ua7Sr7oXd8k76z7of-uEJQrfkAeZg"
)

canale="argonautashop"
admin="XxNiko221xX"

@app.on_message(Filters.command(["start"]) & Filters.private &Filters.chat(admin))
def start(client,message):
	app.send_message(message.chat.id,"Ciao! Tu e solo tu sei abilitato all'utilizzo di questo bot (che culo).\nDigita qui /primo "+
	    "seguito dal messaggio che vuoi inviare sul canale "+Emoji.BEAMING_FACE_WITH_SMILING_EYES+"\n\nEs: /primo Ciao Mondo!")

@app.on_message(Filters.command(["primo"]) & Filters.private & Filters.chat(admin))
def primo(client,message):
	msg=message.command[1:]
	msg=" ".join(msg)
	if msg == "":
		msg="Clicca per primo per vincere!"
		app.send_message(admin,"Non hai inserito un testo, ho inviato un messaggio di default.")

	app.send_message(
		canale,
		msg,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						    "Clicca per Primo!",
						    callback_data="Primo"
						)
				]
			]

			)

		)

@app.on_callback_query()
def primoTast(client, callback_query):
	if callback_query.data=="Primo":
		time.sleep(0.1)
		message=callback_query.message
		message.edit(message.text+f"\n\n**Vincitore:** @{callback_query.from_user.username}")
		app.send_message(admin,f"@{callback_query.from_user.username} ha vinto {Emoji.PARTY_POPPER}!"
			)

app.run()