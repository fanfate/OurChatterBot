from chatterbot import ChatBot
import hug

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



@hug.get()  
def get_response(user_input):
    chatbot = MyChat()
    response = chatbot.get_response(user_input)
    return {"response":response}