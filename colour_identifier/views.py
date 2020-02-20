from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def colour_picker(request):
    body = request.body

    # deserialize to request.body
    # create an image (model)
    # http client to make a GET request to the image's url
    # this will get back a photo
    # then, pass the photo to your colour_identification\colour_identification.py amazing code

    # image = serializers.deserialize("json", request.body)
    # print(image)

    return HttpResponse(body)
