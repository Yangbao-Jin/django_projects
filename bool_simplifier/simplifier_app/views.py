
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pyeda.inter import expr

@csrf_exempt
def simplify_expression(request):
    if request.method == 'POST':
        try:
            expression = request.POST.get('expression')
            bexpr = expr(expression)
            simplified = bexpr.simplify()
            return JsonResponse({'result': str(simplified)})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        # 返回一个信息告知该端点仅接受POST请求
        return JsonResponse({'message': 'This endpoint accepts only POST requests.'})

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')