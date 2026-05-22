from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Criando o endpoint:


@csrf_exempt
@api_view(['POST'])
def api_send_to_upper(request):
    """
    Recebe um texto via JSON, processa e retorna em maiúsculas.
    """
    initial_text = request.data.get('texto', '')

    processed_text = str(initial_text).upper()

    return Response({
        'original': initial_text,
        'resultado': processed_text
    })

# View para renderizar a página index


def index(request):
    return render(request, 'index.html')
