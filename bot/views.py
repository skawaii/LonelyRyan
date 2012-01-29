from django.http import HttpResponse
from django.views.decorators.http import require_POST

@require_POST
def message(request):
  return HttpResponse('hello, %s' % request.POST['name'])

