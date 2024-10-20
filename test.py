from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Функция для обработки команды /start


async def start(update: Update, context):
    await update.message.reply_text('Привет! Я ваш новый бот.')

# Функция для обработки команды /help


async def help_command(update: Update, context):
    await update.message.reply_text('Вот как я могу помочь: используйте команду /start для начала общения.')

# Основная функция для запуска бота
if __name__ == '__main__':
    # Вставьте свой токен
    TOKEN = 'Ваш токен здесь'

    # Создаем приложение бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Запуск бота
    print("Бот запущен...")
    app.run_polling()
