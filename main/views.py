from django.shortcuts import render
from .model import goods
from django.views.generic import ListView


class GoodsAll(ListView):
  model = goods
  template_name = 'main/goodsall.html'