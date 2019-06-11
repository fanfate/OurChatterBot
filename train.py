from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
import logging


class MyChat():
    def __init__(self):
        self.chatbot = ChatBot(
            "chat",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': '抱歉，听不懂。',
                    'maximum_similarity_threshold': 0.50
                }
            ],
            database_uri='sqlite:///db.sqlite3'
        )
        T = ChatterBotCorpusTrainer(self.chatbot)
        T.train("./data/chinese/")
        # UT = UbuntuCorpusTrainer(self.chatbot)
        # UT.train()

if __name__ == '__main__':
    chat = MyChat()
    print('生成数据库db.sqlite3')
