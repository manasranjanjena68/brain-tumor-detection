import json, os, requests
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ChatMessage

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

@login_required
def chatbot_view(request):
    history = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')[:20]
    return render(request, "chatbot/chatbot.html", {"history": history})

@csrf_exempt
@login_required
def ask_chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question = data.get("question", "")
        print("🚀 Received question:", question)

        try:
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json={
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant for brain tumor-related queries."},
                    {"role": "user", "content": question}
                ]
            })

            result = response.json()
            print("✅ Response:", result)

            if 'choices' not in result:
                raise Exception(result.get('error', {}).get('message', 'No valid response from Groq'))

            answer = result['choices'][0]['message']['content'].strip()

            ChatMessage.objects.create(user=request.user, question=question, answer=answer)

            return JsonResponse({"answer": answer})

        except Exception as e:
            print("❌ Chatbot Error:", e)
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@login_required
def chatbot_history(request):
    history = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, "chatbot/history.html", {"history": history})
