from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Post
from .documents import PostDocument
import json


class SearchView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, *args, **kwargs):
        q = self.request.GET.get("q")
        if q:
            posts = PostDocument.search().query("match", title=q)
        else:
            posts = [{"title": "Not founda", "image": None}]
        context = super().get_context_data(**kwargs)
        context["objects"] = posts
        print(posts)
        for post in posts:
            print(post)
        # context["json_objects"] = json.dumps(posts)
        return context


# Create your views here.
