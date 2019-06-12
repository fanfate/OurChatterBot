from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
from chatterbot import ChatBot

class MyChat():
    
    def __init__(self):
        self.chatbot = ChatBot(
            "chat",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    
                }
            ],
            database_uri='sqlite:///../db.sqlite3',
            read_only=True
        )

    def get_response(self, info):
        return str(self.chatbot.get_response(info))


@csrf_exempt
def hello(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request, 'hello.html', context)

@csrf_exempt
def chatView(request):
    context = {}
    context['role'] = 1
    chatbot = MyChat()
    user_word = ''
    if ('words' in request.POST):
        user_word = request.POST['words']
    
    if (user_word == ''):
        context['content'] = '很高兴为您服务'
        return render(request, 'chat.html', {'data': context})
    reply = chatbot.get_response(user_word)
    context['context'] = reply
    
    
    # if (user_word == '你好'):
    #     context['content'] = '你好'
    # elif (user_word == ''):
    #     context['content'] = '很高兴为您服务'
    #     return render(request, 'chat.html', {'data': context})
    # else:
    #     context['content'] = '不好意思，我无法理解您的意思'

    return render_to_response('chat.html', {'data': context})


@csrf_exempt
def getResponse(request):
    context = {}
    context['role'] = 1
    user_word = ''
    if ('words' in request.POST):
        user_word = request.POST['words']
    
    chatbot = MyChat()
    if (user_word == ''):
        context['content'] = '很高兴为您服务'
        return render(request, 'chat.html', {'data': context})
    reply = chatbot.get_response(user_word)
    print(user_word)
    print(reply)
    context['content'] = reply
    # if (user_word == '你好'):
    #     context['content'] = '你好'
    # elif (user_word == ''):
    #     context['content'] = '很高兴为您服务'
    # else:
    #     context['content'] = '不好意思，我无法理解您的意思'
    return HttpResponse(json.dumps(context))