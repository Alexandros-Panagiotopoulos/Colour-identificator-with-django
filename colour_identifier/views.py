from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
import urllib.request
import numpy as np
import cv2
from find_colour.models import ColourFinder
from find_colour.models import PredefinedColour


@api_view(['POST'])
def colour_picker(request):
    body_unicode = request.body
    body = json.loads(body_unicode)
    image = get_image_from_url(next(iter(body.values())))
    predefined_colours = get_predefined_colours()
    colour = ColourFinder(image, predefined_colours)
    dominant_colour = colour.find_images_dominant_colour()
    if not dominant_colour:
        message = 'Most pixels have no close match among the predefined colours'
        return HttpResponse(message)
    return HttpResponse(dominant_colour)


def get_image_from_url(url):
    response = urllib.request.urlopen(url)
    image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def get_predefined_colours():
    predefined_colours = PredefinedColour.objects.all()
    return predefined_colours
