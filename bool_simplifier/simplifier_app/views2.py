from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pyeda.inter import expr
from io import BytesIO
import schemdraw
import schemdraw.elements as elm

@csrf_exempt
def simplify_expression(request):
    if request.method == 'POST':
        try:
            expression = request.POST.get('expression')
            bexpr = expr(expression)
            simplified = bexpr.simplify()
            
            # Generate a circuit diagram image
            circuit_image = generate_circuit_image(simplified)
            
            # Convert image to bytes for sending in the response
            img_bytes = BytesIO()
            circuit_image.save(img_bytes, format='PNG')
            img_bytes = img_bytes.getvalue()
            
            return JsonResponse({'result': str(simplified), 'circuit_image': img_bytes.decode('latin-1')})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        # 返回一个信息告知该端点仅接受POST请求
        return JsonResponse({'message': 'This endpoint accepts only POST requests.'})

def generate_circuit_image(simplified_expression):
    # Generate a circuit diagram using schemdraw or any other library you prefer
    # Here's a simple example using schemdraw
    d = schemdraw.Drawing()
    d += schemdraw.elements.and2().inputs(w=0, n='A', s='B')  # Use and2 instead of And
    
    # Convert the diagram to an image
    img = d.draw()
    
    # You can customize the image as needed, e.g., add labels, etc.
    
    return img

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
