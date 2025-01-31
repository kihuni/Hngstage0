from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone

def user_info(request):
    data = {
        "email": "stephenkihuni55@gmail.com",  
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/kihuni/hng-stage0"
    }
    return JsonResponse(data)