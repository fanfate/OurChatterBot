from chatterbot import ChatBot

class MyChat():
    
    def __init__(self):
        self.chatbot = ChatBot(
            "chat",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                }
            ],
            database_uri='sqlite:///db.sqlite3',
            read_only=True
        )

    def get_response(self, info):
        return str(self.chatbot.get_response(info))

if __name__ == '__main__':
    chat = MyChat()
    while True:
        try:
            reply = chat.get_response(input('>'))
            print(reply)
        except (KeyboardInterrupt, KeyError, SystemExit):
            break