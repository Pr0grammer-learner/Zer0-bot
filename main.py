import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token = "49b75e030896337ba10c207a46e79d59b58f313a646b5a3f8ca9b4415680348c5037c9e1dcf8477ebd731")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

privet = ["привет","hi","здарова","ку","приветствую","доброе утро","добрый день","хай","hello","приветик","приветос","здравствуйте","здравствуй"]
greetings = "Привет, меня зовут Zer0 и я бот, мой создатель (Тимофей) пока ничему меня не научил! Жди обновлений, они наверное будут)"
commands = ["/help - Cписок всех команд"]
unknown = "Привет, я пока не знаю как на это реагировать! Скоро такой функционал появится)"



def send_message(id, some_text, keyboard=None):
    post = {"user_id":id,
            "message":some_text,
            "random_id": 0,
            "keyboard": keyboard
            }
    vk_session.method("messages.send",post)
def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            if message == "начать" or message == "все команды":
                if message == "начать":
                    send_message(id, greetings)
                    send_message(id, "Cписок команд")
                    for i in range(0, len(commands)):
                        send_message(id, commands[i])
                else:
                    send_message(id, "Cписок команд")
                    for i in range(0,len(commands)):
                        send_message(id, commands[i])
            else:
                keyboard = {
                    "one_time": False,
                    "buttons": [
                        [get_but("Все команды", "positive")], [get_but("Тестовая кнопка", "primary")]
                    ]
                }
                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                keyboard = str(keyboard.decode('utf-8'))
                send_message(id, unknown, keyboard)




