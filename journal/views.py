from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView

# Create your views here.

class JournalListView(ListView):
    model = Journal
    template_name = "journal/journal_list.html"from django.shortcuts import render

