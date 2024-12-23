from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .models import Event

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

class EventsList(generic.ListView):


    model = Event
    template_name = "index.html"
    paginate_by = 12


def event_detail(request, event_id):


    queryset = Event.objects.all()
    event = get_object_or_404(queryset, event_id=event_id)
    
    return render(
        request,
        "events/event_detsil.html",
        {"event": event}
    )