from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import PageViewCount


@require_http_methods(["GET"])
def hello_view(request):
    counter, _ = PageViewCount.objects.get_or_create(title="hello")
    counter.count += 1
    counter.save()
    return HttpResponse(f"Hello world. The counter is: {counter.count}")


@require_http_methods(["GET"])
def goodbye_view(request):
    return HttpResponse(f"Goodbye world")
