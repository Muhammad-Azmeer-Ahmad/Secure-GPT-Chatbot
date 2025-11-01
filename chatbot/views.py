from django.shortcuts import render
from django.http import JsonResponse
import openai
import os


def home(request):
    return render(request, "index.html")

def chat_api(request):
    if request.method == "POST":
        message = request.POST.get("message")
        # Replace with your actual API logic
        response_text = f"Mock response to: {message}"
        return JsonResponse({"response": response_text})
