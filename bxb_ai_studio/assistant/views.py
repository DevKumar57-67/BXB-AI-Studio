
from django.shortcuts import render
from django.http import JsonResponse
from .engine.router import get_reply


def chat_page(request):
    return render(request, "assistant/chat.html")


def chat_response(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST requests only."},
            status=405,
        )

    message = request.POST.get("message", "").strip()

    if not message:
        return JsonResponse(
            {"error": "Please type a message."},
            status=400,
        )

    result = get_reply(message)

    return JsonResponse({
        "reply": result["reply"],
        "intent": result["intent"],
        "confidence": result["confidence"],
    })