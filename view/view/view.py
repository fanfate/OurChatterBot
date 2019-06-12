from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
from chatterbot import ChatBot
import json
import urllib.request

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


@csrf_exempt
def tulling(request):
    context = {}
    context['role'] = 1
    user_word = ''
    if ('words' in request.POST):
        user_word = request.POST['words']
    try:
        api_url = "http://openapi.tuling123.com/openapi/api/v2"

        req = {
            "reqType": 0,  # 输入类型 0-文本, 1-图片, 2-音频
            "perception":  # 信息参数
            {
                "inputText":  # 文本信息
                {
                    "text": user_word
                },

                "selfInfo":  # 用户参数
                {
                    "location":
                    {
                        "city": "北京",  # 所在城市
                        "province": "北京",  # 省份
                    }
                }
            },
            "userInfo":
            {
                "apiKey": "32fc4ae3f6904af5b4f4fedc60d06bcc",  # 改为自己申请的key
                "userId": "0001"  # 用户唯一标识(随便填, 非密钥)
            }
        }
        # print(req)
        # 将字典格式的req编码为utf8
        req = json.dumps(req).encode('utf8')
        # print(req)
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        # print(response_str)
        response_dic = json.loads(response_str)
        # print(response_dic)
        intent_code = response_dic['intent']['code']
        results_text = response_dic['results'][0]['values']['text']
        context['content'] = results_text
        # print('code：' + str(intent_code))
    except KeyError:
        context['content'] = '出错啦~~, 下次别问这样的问题了'
    return HttpResponse(json.dumps(context))