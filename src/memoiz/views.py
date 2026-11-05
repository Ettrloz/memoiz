from django.shortcuts import render
from .models import Memo


def index(request):
    memos = Memo.objects.all().order_by('-created_at')
    return render(request, 'memoiz/index.html', {'memos': memos})


def detail(request, memo_id):
    memo = Memo.objects.get(pk=memo_id)
    return render(request, 'memoiz/detail.html', {'memo': memo})