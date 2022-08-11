# Main menu
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import main_menu_callback, account_main_callback, support_callback

main_menu = InlineKeyboardMarkup(
            inline_keyboard=
            [
                [
                    InlineKeyboardButton(text="🎮   Выбрать игру   🎮", callback_data=main_menu_callback.new(
                        menu_choice="choice_game"
                    ))
                ],
                [
                    InlineKeyboardButton(text="💼   Личный кабинет   💼", callback_data=account_main_callback.new(
                        enter="true"
                    )),
                ],
                [
                    InlineKeyboardButton(text="📋  Тех. Поддержка  📋", callback_data=support_callback.new(
                            to_do="get_info"
                    ))
                ]
            ],
            resize_keyboard=True,
)
def to_menu():
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text="В меню", callback_data=main_menu_callback.new(menu_choice="main_menu")))
    return markup