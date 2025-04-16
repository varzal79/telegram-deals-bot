from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
# הטוקן שלך מ-BotFather
TOKEN = "8153726499:AAFS9sZkUGvSU2X2MS2P02bQmTT6NjAOzog"
def start(update, context):
    update.message.reply_text("היי! אני הבוט שלך לדילים. שלח לי קישור ואני אבדוק אם אפשר להמיר אותו לאפיליאייט 💸")

def handle_message(update, context):
    text = update.message.text

    if "amazon" in text.lower():
        update.message.reply_text("זה נראה כמו קישור של אמזון! 🔗 בקרוב אחליף אותו לקישור אפיליאייט שלך.")
    elif "aliexpress" in text.lower():
        update.message.reply_text("מצאתי קישור של אליאקספרס 🧧 – מוכן להחלפה.")
    else:
        update.message.reply_text(f"קיבלתי ממך:\n{text}")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("🚀 הבוט רץ עכשיו... מחכה להודעות בטלגרם")

    # במקום updater.idle() – נשאיר את התהליך רץ
    while True:
        time.sleep(15)

if __name__ == '__main__':
    main()
