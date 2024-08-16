from django.shortcuts import render
from django.views import View

# Class-Based View (CBV)
class TopTipsView(View):
    def get(self, request):
        return render(request, 'top_tips/top_tips.html')
