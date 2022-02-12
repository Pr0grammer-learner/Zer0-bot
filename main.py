import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token = "ae6f355f004d04a1cfa474ddbd7cd0a31d44a006729eb4b8250e3df63f1898a77928acc4ba856a1cb3aad")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

privet = ["привет","hi","здарова","ку","приветствую","доброе утро","добрый день","хай","hello","приветик","приветос","здравствуйте","здравствуй"]

def button_create():
    keyboard = VkKeyboard()
    keyboard.add_button("Все команды", VkKeyboardColor.POSITIVE)

def send_some_message(id, some_text, keyboard = None):
    post = {"user_id":id,
            "message":some_text,
            "random_id":0}
    if keyboard != None:
        post[keyboard] = keyboard.get_keyboard()
    else:
        post = post
    vk_session.method("messages.send",post)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            if message in privet:
                    button_create()
                    send_some_message(id,"Привет, меня зовут Zer0 и я бот, мой создатель (Тимофей) пока ничему меня не научил! Жди обновлений, они наверное будут)")
            else:
                button_create()
                send_some_message(id,"Привет, я пока не знаю как на это реагировать! Скоро такой функционал появится)")



