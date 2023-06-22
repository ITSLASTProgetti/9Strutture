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
        formatted += "NOME STRUTTURA: {}\n, INDIRIZZO: {}\n\n".format(row[0], row[1])
    return formatted

from telegram.ext import Updater, CommandHandler

#bottone 1 - Bussolengo
async def bott1(update, context):
    # Creazione dei bottoni
    kbBus = [
        [InlineKeyboardButton("Agriturismo", callback_data='bus_agri')],
        [InlineKeyboardButton("B&B", callback_data='bus_bb')],
        [InlineKeyboardButton("Hotel", callback_data='bus_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbBus)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Bussolengo:', reply_markup=reply_markup)

async def bus_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Bussolengo where tipostruttura in ('Locazione turistica','Casa vacanza','Bed and Breakfast','Affittacamere')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def bus_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Bussolengo where tipostruttura in ('Albergo, Villaggio albergo, Albergo diffuso Residenze turistiche alberghiere Campeggi, villaggi turistici')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Hotel:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def bus_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Bussolengo where tipostruttura in ('Agriturismo')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 2 - Castelnuovo
async def bott2(update, context):
    # Creazione dei bottoni
    kbCas = [
        [InlineKeyboardButton("Agriturismo", callback_data='cas_agri')],
        [InlineKeyboardButton("B&B", callback_data='cas_bb')],
        [InlineKeyboardButton("Hotel", callback_data='cas_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbCas)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Castelnuovo:', reply_markup=reply_markup)

async def cas_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Castelnuovo where tipostruttura in ('Casa vacanza','Bed and Breakfast', 'Locanda','Campeggio','Affittacamere') limit 5"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def cas_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Castelnuovo where tipostruttura in ('Albergo', 'Altre strutture extralberghiere', 'Villaggio','Residence')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Hotel:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def cas_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Castelnuovo where tipostruttura in ('Agriturismo')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 3 _ Mozzecane
async def bott3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Creazione dei bottoni
    kbMozz = [
        [InlineKeyboardButton("BB", callback_data='moz_bb')],
        [InlineKeyboardButton("Hotel", callback_data='moz_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbMozz)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Mozzecane:', reply_markup=reply_markup)

async def moz_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Mozzecane where tipostruttura = 'B&B'"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def moz_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Mozzecane where tipostruttura = 'Alberghiero'"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Alberghi:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 4 - Pastrengo
async def bott4(update, context):
    # Creazione dei bottoni
    kbPas = [
        [InlineKeyboardButton("B&B", callback_data='pas_bb')],
        [InlineKeyboardButton("Hotel", callback_data='pas_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbPas)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Pastrengo:', reply_markup=reply_markup)

async def pas_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Pastrengo where tipostruttura in ('B&B')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def pas_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Pastrengo where tipostruttura in ('Alberghiero')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Hotel:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


#bottone 5 - Pescantina
async def bott5(update, context):
# Creazione dei bottoni
    kbPes = [
        [InlineKeyboardButton("B&B", callback_data='pes_bb')],
        [InlineKeyboardButton("Hotel", callback_data='pes_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbPes)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Pescantina:', reply_markup=reply_markup)

async def pes_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Pescantina where tipostruttura in ('B&B')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def pes_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Pescantina where tipostruttura in ('Hotel')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Hotel:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 6 - Sommacampagna
async def bott6(update, context):
    # Creazione dei bottoni
    kbSom = [
        [InlineKeyboardButton("Agriturismo", callback_data='som_agri')],
        [InlineKeyboardButton("B&B", callback_data='som_bb')],
        [InlineKeyboardButton("Hotel", callback_data='som_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbSom)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Sommacampagna:', reply_markup=reply_markup)

async def som_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Sommacampagna where tipostruttura in ('B&B','LOCAZIONE TURISTICA', 'ALLOGGIO TURISTICO','STRUTTURA TURISTICA CLASSIFICATA')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def som_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Sommacampagna where tipostruttura in ('STRUTTURA RICETTIVA ALBERGHIERA', 'STRUTTURA RICETTIVA COMPLEMENTARE', 'STRUTTURA RICETTIVA COMPLEMENTARE CLASSIFICATA')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Hotel:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def som_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Sommacampagna where tipostruttura in ('AGRITURISMO')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


#bottone 7 - Sona
async def bott7(update, context):
    # Creazione dei bottoni
    kbSo = [
        [InlineKeyboardButton("Agriturismo", callback_data='so_agri')],
        [InlineKeyboardButton("B&B", callback_data='so_bb')]
    ]
    reply_markup = InlineKeyboardMarkup(kbSo)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Sona:', reply_markup=reply_markup)

async def so_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Sona where tipostruttura in ('B&B')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def so_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Sona where tipostruttura in ('Alberghiero')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 8 - Valeggio
async def bott8(update, context):
    # Creazione dei bottoni
    kbVal = [
        [InlineKeyboardButton("Agriturismo", callback_data='val_agri')],
        [InlineKeyboardButton("B&B", callback_data='val_bb')]
    ]
    reply_markup = InlineKeyboardMarkup(kbVal)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Valeggio:', reply_markup=reply_markup)

async def val_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Valeggio where tipostruttura in ('B&B')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def val_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Valeggio where tipostruttura in ('Alberghiero')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 9 - Villafranca
async def bott9(update, context):
    # Creazione dei bottoni
    kbVil = [
        [InlineKeyboardButton("Agriturismo", callback_data='vil_agri')],
        [InlineKeyboardButton("B&B", callback_data='vil_bb')],
        [InlineKeyboardButton("Hotel", callback_data='vil_hotel')]
    ]
    reply_markup = InlineKeyboardMarkup(kbVil)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Villafranca:', reply_markup=reply_markup)

async def vil_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Villafranca where tipostruttura in ('B&B','Affittacamere', 'Locazioni turistiche','Unità abitative')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def vil_hotel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Villafranca where tipostruttura in ('Alberghiero', '', '')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Hotel:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def vil_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Villafranca where tipostruttura in ('Agriturismo','Enoturismo', 'Fattorie Sociali','Agricampeggio','Turismo rurale')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

#bottone 10 - Vigasio
async def bott10(update, context):
    # Creazione dei bottoni
    kbVi = [
        [InlineKeyboardButton("Agriturismo", callback_data='vi_agri')],
        [InlineKeyboardButton("B&B", callback_data='vi_bb')]
    ]
    reply_markup = InlineKeyboardMarkup(kbVi)
    # Invio dei bottoni all'utente
    await update.callback_query.message.edit_text(text='Vieggio:', reply_markup=reply_markup)

async def vi_bb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Vigasio where tipostruttura in ('B&B')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco B&B:\n" + formatted_results
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def vi_agri(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = "SELECT * FROM Vigasio where tipostruttura in ('Alberghiero')"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco Agriturismo:\n" + formatted_results
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
        [InlineKeyboardButton("Vigasio", callback_data='button10')],
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

    elif query.data == 'moz_bb':
        await moz_bb(update, context)
    elif query.data == 'moz_hotel':
        await moz_hotel(update, context)

    elif query.data == 'som_agri':
        await som_agri(update, context)
    elif query.data == 'som_bb':
        await som_bb(update, context)
    elif query.data == 'som_hotel':
        await som_hotel(update, context)

    elif query.data == 'so_agri':
        await so_agri(update, context)
    elif query.data == 'so_bb':
        await so_bb(update, context)

    elif query.data == 'val_agri':
        await val_agri(update, context)
    elif query.data == 'val_bb':
        await val_bb(update, context)

    elif query.data == 'vi_agri':
        await vi_agri(update, context)
    elif query.data == 'vi_bb':
        await vi_bb(update, context)
    
    elif query.data == 'cas_agri':
        await cas_agri(update, context)
    elif query.data == 'cas_bb':
        await cas_bb(update, context)
    elif query.data == 'cas_hotel':
        await cas_hotel(update, context)

    elif query.data == 'bus_agri':
        await bus_agri(update, context)
    elif query.data == 'bus_bb':
        await bus_bb(update, context)
    elif query.data == 'bus_hotel':
        await bus_hotel(update, context)
    
    elif query.data == 'pas_bb':
        await pas_bb(update, context)
    elif query.data == 'pas_hotel':
        await pas_hotel(update, context)

    elif query.data == 'pes_bb':
        await pes_bb(update, context)
    elif query.data == 'pes_hotel':
        await pes_hotel(update, context)

    elif query.data == 'vil_agri':
        await vil_agri(update, context)
    elif query.data == 'vil_bb':
        await vil_bb(update, context)
    elif query.data == 'vil_hotel':
        await vil_hotel(update, context)
    


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



