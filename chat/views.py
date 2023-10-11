from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


def index(request):
    # Your view logic here
    return render(request, 'chat/index.html')  # Adjust the template name as needed

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        content = request.POST.get('content')
        if sender and content:
            message = Message(sender=sender, content=content)
            message.save()
            return JsonResponse({'status': 'Message sent successfully'})
        else:
            return JsonResponse({'status': 'Sender and content are required'}, status=400)
    else:
        return JsonResponse({'status': 'Invalid request method'}, status=405)

def get_messages(request):
    if request.method == 'GET':
        messages = Message.objects.all().values('sender', 'content', 'timestamp')
        return JsonResponse({'messages': list(messages)})
    else:
        return JsonResponse({'status': 'Invalid request method'}, status=405)
