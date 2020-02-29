# Task

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


# Solution

The solution was created using Python 3.7 and Django 2.2

In order to run the code, the following libraries should be installed:
- jangorestframework
- numpy
- opencv-python
- webcolors


The endpoint receives a JSON POST with the url of an image.  
Then it makes a GET request to read the image.  
Lastly it calculates which colour is more frequently met in the image's pixels and returns that colour.  

### Request
```
POST /colour

{
"url": "path/to/image" 
}
```

### Response
```
"dominant_colour"
```

A list of predefined colours is stored in a database.  
A sample of 10000 pixels are being received from the picture and the code finds the closest colour match to the list of stored colours.  
So it returns the dominant colour without mixing the colours (ie if picture is 51% white and 49% black it will return black).  
If most pixels have no close match (a factor was introduced to specify what is considered close match), then a message that there is no close match will be returned to the user as a string.


### The structure of the solution

The POST request is being received by the colour_identifier/urls.py and sent to colour_identifier/views.py  

The function `colour_picker()` deserialises the request, retrieves the actual image with the help of `get_image_from_url()` function and sends the image at the model of find_colour Django app,
i.e. find_colour/models.py, at the ColourFinder class.  

At that point the last function `find_images_dominant_colour()` has the role of the main function; 
it calls other functions and sends the solution back at the colour_identifier/views.py.  
 
It should be noted that there is a currently unused function called 'get_closest_colour_from_css3_colours' which can be used if we want to use the colours of an existing database like css3. instead of the predefined colours.

