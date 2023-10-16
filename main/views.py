from django.shortcuts import render
from .model import buyers
from django.views.generic import ListView, CreateView


class BuyersList(ListView):
  model = buyers
  template_name = 'main/buyerslist.html'