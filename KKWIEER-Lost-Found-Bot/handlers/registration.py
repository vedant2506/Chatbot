from telebot.types import ReplyKeyboardRemove
from database import database
from utils import helpers, state, validators


def send_welcome(bot, message):
    chat_id = message.chat.id
    telegram_id = message.from_user.id
    state.clear_user(chat_id)
    try:
        bot.clear_step_handler_by_chat_id(chat_id)
    except Exception:
        pass

    try:
        user = database.get_user_by_telegram_id(telegram_id)
    except Exception:
        helpers.safe_send(bot, chat_id, "Something went wrong. Please try again.")
        return

    if user:
        if not user["is_active"]:
            helpers.safe_send(
                bot,
                chat_id,
                "Your account has been deactivated. Contact a college administrator if you need help.",
            )
            return
        try:
            database.update_user_username(telegram_id, message.from_user.username)
        except Exception:
            pass
        helpers.safe_send(bot, chat_id, "👋 Welcome back to KKWIEER Lost & Found!")
        helpers.show_main_menu(bot, message)
        return

    msg = bot.send_message(
        chat_id,
        "👋 Welcome to KKWIEER Lost & Found!\nLet's create your profile first.\n\nPlease enter your name:",
        reply_markup=ReplyKeyboardRemove(),
    )
    bot.register_next_step_handler(msg, lambda m: process_name_step(bot, m))


def process_name_step(bot, message):
    if message.content_type == "text" and message.text == "/start":
        send_welcome(bot, message)
        return
    ok, value = validators.is_valid_name(getattr(message, "text", None))
    if not ok:
        msg = bot.send_message(message.chat.id, value + " Try again:")
        bot.register_next_step_handler(msg, lambda m: process_name_step(bot, m))
        return
    try:
        existing = database.get_user_by_telegram_id(message.from_user.id)
        if existing:
            helpers.show_main_menu(bot, message, "You are already registered.")
            return
        database.create_user(message.from_user.id, message.from_user.username, value)
    except Exception:
        helpers.safe_send(bot, message.chat.id, "Something went wrong. Please try again.")
        return
    helpers.safe_send(bot, message.chat.id, f"Profile created successfully, {value}!")
    helpers.show_main_menu(bot, message)


def register(bot):
    @bot.message_handler(commands=["start"])
    def handle_start(message):
        send_welcome(bot, message)
