from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ваш токен бота
TOKEN = '7450558480:AAEGOj9wUoO1ViehRoAPIxk78lzwW39vj6A'

# Ответ на команду /faq
def faq(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "О проекте: \n\n"
        "➡️ Ringgame.co\n\n"
        "🔝 NFT collection RING\n\n"
        "💰 AIRDROP\n\n"
        "➡️ Наш дружный чат\n\n"
        "😕 Admin\n\n"
        "Проголосовать за RING\n\n"
        "Ссылка для друзей: @ringgame\n\n"
        "Собрали для вас навигацию по важным статьям:\n\n"
        "1. Кто мы?\n\n"
        "2. Планы нашего проекта\n\n"
        "3. Игра «Турнирный кликер»\n\n"
        "4. Ответ на ваши вопросы (1):\n\n"
        "5. Ответ на ваши вопросы (2):\n\n"
        "6. Ответ на ваши вопросы (3):\n\n"
        "7. Ответы на ваши вопросы (4):\n\n"
        "8. Как вас бреют 🐹 🪒\n\n"
        "9. Процесс создания Бэна\n\n"
        "10. Наши персонажи:\n\n"
        "11. Почему web3\n\n"
        "12. Что ждет нас и TON\n\n"
        "@ringgame"
    )

# Ответ на команду /kak
def kak(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "👉 Запускаем AIRDROP\n\n"
        "Вы сможете получить мем-токены $BEN и билеты на турнир с призами более 20.000$ просто приглашая друзей\n\n"
        "Условия — @ringairdropbot\n\n"
        "Будет проведена серьезная проверка на наличие ботов и мульти-аккаунтов. Все токены человека, который их привел будут сожжены 🔥\n\n"
        "CLAIM токенов будет доступен 03.06.2024\n\n"
        "Действуйте честно и все будет хорошо. Кто приводил ботов и мультиаки - не получит ничего\n\n"
        "Наш чат 💬 - доступ\n\n"
        "❗️ЕСЛИ вам начисляют за premium друзей как за обычных - дождитесь вечера, произойдет автоматический перерасчет"
    )

def main() -> None:
    # Создание Updater и передача ему токена бота
    updater = Updater(TOKEN)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("faq", faq))
    dispatcher.add_handler(CommandHandler("kak", kak))

    # Запуск бота
    updater.start_polling()

    # Работа до прерывания
    updater.idle()

if __name__ == '__main__':
    main()
