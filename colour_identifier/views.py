from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
from find_colour.models import ColourFinder


@api_view(['POST'])
def colour_picker(request):
    body_unicode = request.body
    body = json.loads(body_unicode)
    colour = ColourFinder(next(iter(body.values())))
    dominant_colour = colour.find_images_dominant_colour()
    return HttpResponse(dominant_colour)
