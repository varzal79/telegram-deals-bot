from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# הכנס את הטוקן שלך
TOKEN = "8153726499:AAFidSOZuGvSEBax17xjYMDlejBFOZ3uvVo"
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
    print("🚀 הבוט התחיל לרוץ ב-Render! מחכה להודעות...")
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("🔄 הבוט רץ עכשיו... חכה להודעות בטלגרם")
    updater.idle()

if __name__ == '__main__':
    main()
