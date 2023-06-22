# IMPORTO LE LIBRERIE CHE MI SERVONO PER OPERARE CON IL BOT TELEGRAM
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes, filters, MessageHandler, ApplicationBuilder, ContextTypes

import logging

import sqlite3
from aiogram import Bot, Dispatcher, executor, types

def execute_query(query):
    conn = sqlite3.connect('Strutture.db')
    cursor = conn.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def format_results(results):
    formatted = ''
    for row in results:
        formatted += "ID: {}, Username: {}, Name: {}\n".format(row[0], row[1], row[2])
    return formatted

from telegram.ext import Updater, CommandHandler

#bottone 1
async def bott1(update, context):
    query = "SELECT * FROM Bussolengo"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 2
async def bott2(update, context):
    query = "SELECT * FROM Castelnuovo"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 3
async def bott3(update, context):
    keyboard = [
        [InlineKeyboardButton("Bussolengo", callback_data='button1')],
        [InlineKeyboardButton("Castelnuovo", callback_data='button2')],
        [InlineKeyboardButton("Mozzecane", callback_data='button3')]]
    if query.data == 'button1':
        print("1")
    elif query.data == 'button2':
        print("2")
    elif query.data == 'button3':
        print("3")
        '''
    query = "SELECT * FROM Mozzecane"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    '''

#bottone 4
async def bott4(update, context):
    query = "SELECT * FROM Pastrengo"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 5
async def bott5(update, context):
    query = "SELECT * FROM Pescantina"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 6
async def bott6(update, context):
    query = "SELECT * FROM Sommacampagna"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 7
async def bott7(update, context):
    query = "SELECT * FROM Sona"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 8
async def bott8(update, context):
    query = "SELECT * FROM Valeggio"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 9
async def bott9(update, context):
    query = "SELECT * FROM Villafranca"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 10
async def bott10(update, context):
    query = "SELECT * FROM Vigasio"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco utenti:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


# Installing
# You can install or upgrade python-telegram-bot via
# pip install python-telegram-bot --upgrade

# QUI LEGGIAMO DAL FILE TOKEN.txt IL TOKEN DEL BOT
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

# QUESTA FUNZIONE PRENDE LA LINGUA DELL'UTENTE (ITALIANO, INGLESE) 
# E IL SUO NOME NELLA STRUTTURA update.effective_user
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = "linguaggio utilizzato: " +update.effective_user.language_code
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {lang}')

# QUESTA FUNZIONE PRENDE OGNI COSA CHE SCRIVIAMO SUL BOT
# CHE NON SIA UN COMANDO E LO RISCRIVE A SCHERMO
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# QUESTA FUNZIONE PRENDE L'INPUT DELL'UTENTE (context.args) E LO 
# RESTITUISCE ALL'UTENTE
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    received_input = context.args
    text_caps = ' '.join(received_input).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    

# Funzione per gestire il comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Creazione dei bottoni
    keyboard = [
        [InlineKeyboardButton("Bussolengo", callback_data='button1')],
        [InlineKeyboardButton("Castelnuovo", callback_data='button2')],
        [InlineKeyboardButton("Mozzecane", callback_data='button3')],
        [InlineKeyboardButton("Pastrengo", callback_data='button4')],
        [InlineKeyboardButton("Pescantina", callback_data='button5')],
        [InlineKeyboardButton("Sommacampagna", callback_data='button6')],
        [InlineKeyboardButton("Sona", callback_data='button7')],
        [InlineKeyboardButton("Valeggio", callback_data='button8')],
        [InlineKeyboardButton("Villafranca", callback_data='button9')],
        [InlineKeyboardButton("Vigasio", callback_data='button1')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Invio dei bottoni all'utente
    await update.message.reply_text('Clicca su uno dei bottoni:', reply_markup=reply_markup)

# Funzione per gestire la pressione dei bottoni
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # Esempio di gestione della pressione dei bottoni
    if query.data == 'button1':
        await bott1(update, context)
    elif query.data == 'button2':
        await bott2(update, context)
    elif query.data == 'button3':
        await bott3(update, context)
    elif query.data == 'button4':
        await bott4(update, context)
    elif query.data == 'button5':
        await bott5(update, context)
    elif query.data == 'button6':
        await bott6(update, context)
    elif query.data == 'button7':
        await bott7(update, context)
    elif query.data == 'button8':
        await bott8(update, context)
    elif query.data == 'button9':
        await bott9(update, context)
    elif query.data == 'button10':
        await bott10(update, context)

    
# IL MAIN CONTIENE TUTTI I COMANDI CHE L'UTENTE PUò ESEGUIRE
def main():
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler('caps', caps))

    # Aggiungi un handler per il comando /start
    app.add_handler(CommandHandler("start", start))

    # Aggiungi un handler per i bottoni
    app.add_handler(CallbackQueryHandler(button))


    app.add_handler(echo_handler)
    app.run_polling()


if __name__=='__main__':
   main()



