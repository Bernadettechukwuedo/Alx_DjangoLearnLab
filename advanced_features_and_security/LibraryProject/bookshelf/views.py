from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.views import View
from .forms import Form

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


def form_example(request):
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            print(name)

    return render(request, "bookshelf/form_example.html", {"form": form})
