from django.views.decorators.http import require_POST # 目前的 API 视图只能用于接收 POST 请求
from django.http import JsonResponse # 用于返回 JSON 数据
from django.conf import settings
from django.http import HttpResponse
from django.urls import path,re_path
import subprocess
from django.views.decorators.csrf import csrf_exempt

setting = {
    'DEBUG':True,
    'ROOT_URLCONF':__name__
}

settings.configure(**setting)


def home(request):
    with open('index.html','rb') as f:
        htmlf = f.read()
        return HttpResponse(htmlf)
    

import subprocess

def run_code(code):
    try:
        output = subprocess.check_output(['python3','-c',code],
                universal_newlines=True,
                stderr=subprocess.STDOUT,
                timeout=15)
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired as e:
        # 检查 e.output 是否为 None
        output_msg = e.output if e.output else ""
        output = '\r\n'.join(['Time Out!!!', output_msg])
    return output

