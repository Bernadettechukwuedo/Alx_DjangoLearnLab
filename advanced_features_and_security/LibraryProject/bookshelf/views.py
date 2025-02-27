from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.views import View

# Create your views here.


class book_list(View):
    def get(self, request):
        return render(request, "book_list.html")


@permission_required("bookshelf.can_edit", raise_exception=True, login_url="/admin/")
def can_edit(request):
    return render(request, "can_edit.html")


@permission_required("bookshelf.can_view", raise_exception=True, login_url="/admin/")
def can_view(request):
    return render(request, "can_view.html")


@permission_required("bookshelf.can_delete", raise_exception=True, login_url="/admin/")
def can_delete(request):
    return render(request, "can_delete.html")
