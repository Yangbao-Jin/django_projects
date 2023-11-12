
# 设置你的OpenAI API密钥
#openai.api_key = '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'
#from django.core.files.storage import default_storagefrom django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
import requests

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        if not uploaded_file.name.endswith('.png'):
            return HttpResponse('请上传PNG格式的文件')

        files = {'image': uploaded_file}

        # OpenAI API 请求设置
        headers = {
            'Authorization': 'Bearer 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',  # 替换 YOUR_OPENAI_API_KEY 为你的API密钥
            #'Content-Type': 'application/json',
        }

        response = requests.post(
            'https://api.openai.com/v1/engines/image-alpha-001/completions',  # 替换 YOUR_MODEL_NAME 为你想使用的模型名称
            headers=headers,
            files=files
        )

        response_json = response.json()
        print(response_json) 
        if 'data' in response_json and 'choices' in response_json['data'] and len(response_json['data']['choices']) > 0:
            answer = response_json['data']['choices'][0]['answer']
            return render(request, 'graph_app/result.html', {'answer': answer})  # 替换 your_template_name.html 为你的模板文件名
        else:
            return HttpResponse('OpenAI API没有返回预期的数据')

    return render(request, 'graph_app/upload.html')  # 这是文件上传的HTML模板页面
