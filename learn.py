from chatterbot import ChatBot
from chatterbot.conversation import Statement


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
            ]
        )

    def get_feedback(self):
        text = input()

        if 'y' in text.lower():
            return True
        elif 'n' in text.lower():
            return False
        else:
            print('Please type either "y" or "n"')
            return self.get_feedback()

    def get_response(self, info):
        return str(self.chatbot.get_response(info))



if __name__ == '__main__':
    chat = MyChat()
    print('Type something to begin...')
    while True:
        try:
            input_statement = Statement(text=input())
            response = chat.chatbot.generate_response(
                input_statement
            )

            print('\n Is "{}" a correct response to "{}"? \n'.format(
                response.text,
                input_statement.text
            ))
            if chat.get_feedback() == False:
                print('please input the correct one')
                correct_response = Statement(text=input())
                chat.chatbot.learn_response(correct_response, input_statement)
                print('Responses added to bot!')
            print('Next...')
        except (KeyboardInterrupt, KeyError, SystemExit):
            break


# bot = ChatBot(
#     "test",
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         {
#             'import_path': 'chatterbot.logic.BestMatch',
#             'default_response': '抱歉，听不懂。',
#             'maximum_similarity_threshold': 0.50
#         }
#     ]
# )


# def get_feedback():

#     text = input()

#     if 'y' in text.lower():
#         return True
#     elif 'n' in text.lower():
#         return False
#     else:
#         print('Please type either "y" or "n"')
#         return get_feedback()


# print('Type something to begin...')

# # The following loop will execute each time the user enters input
# while True:
#     try:
#         input_statement = Statement(text=input())
#         response = bot.generate_response(
#             input_statement
#         )

#         print('\n Is "{}" a coherent response to "{}"? \n'.format(
#             response.text,
#             input_statement.text
#         ))
#         if get_feedback() == False:
#             print('please input the correct one')
#             correct_response = Statement(text=input())
#             bot.learn_response(correct_response, input_statement)
#             print('Responses added to bot!')
#         print('Next...')

#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break
