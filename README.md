Task

Write an HTTP endpoint that will take an image url, and return which colour it matches most
closely from a set of predefined references.
So - the predefined references might be (pseudo-code examples):
{ "key": "teal", red: 123, green: 123, blue: 123 }
{ "key": "grey", red: 0, green: 0, blue: 0 }
If passed the sample teal image from above, the endpoint should return 'teal', if passed the grey
image, it would return 'grey' etc.
If none of the colours are a close match - this should be flagged up by the endpoint
The solution does not need to be hosted for us to test, but evidence of its behaviour should be
included. Some screenshots, example requests and example JSON payloads should suffice.


Solution

The solution was created using Python 3.7 and Django 2.2

In order to run the additional libraries should be installed
-djangorestframework
-numpy
-opencv-python
-webcolors


The built Http endpoint receives a JSON POST request sent to server_name/colour, and reads the value of the first item. This value should be an image url. 
In this case the user will receive a responce which is a string indicating the colour of the most pixels of the image.

More specificaly there are some predefined colours stores at the external file 'predefined_colours.txt' in the form of the pseudo-code example provided.
A sample of 10000 pixels are being received from the picture and find the closer match colour from the stored colours. Then it returns the colour that
most pixels match to. So it returns the dominant colour without mixing the colours (ie if picture is 51% white and 49% black it will return black).
If most pixels has no close match (a factor was introduced to specify what considered close match), the a message that there is no close match will return to the user as a string.


The stracture of the solution is as follow:

The POST request is being received by the colour_identifier/urls.py and sent to colour_identifier/views.py
The function colour_picker deserialise the request, retrieve the actual image with the help of get_image_from_url function and send the image at the model of find_colour Jango app,
i.e. find_colour/models.py, at the ColourFinder class. At that point the last fuction 'find_images_dominant_colour' has the role of the main function, call other functions and send the
solution back at the colour_identifier/views.py. It should be noted that there is a currently unused fanction called 'get_closest_colour_from_css3_colours' which can be used if we want
to use the colours of an existing database like css3 instead of the predefined colours.

