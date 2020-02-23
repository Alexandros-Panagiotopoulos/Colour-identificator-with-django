import cv2
import webcolors
from collections import Counter
import ast


class ColourFinder:
    def __init__(self, image):
        self.image = image
        with open('predefined_colours.txt', 'r') as file_object:
            self.predefined_colours = ast.literal_eval(file_object.read())  # read predefined colours as a list of dicts
        self.reduced_x_pixels = 100  # controls the size of the pixels sample that handled and speed of code
        self.reduced_y_pixels = 100
        self.max_dist_squared = 255 ** 2 * 3  # maximum squared distance between two corners of rgb space
        self.match_factor = 0.02  # the lower the factor the closer match is demanded

    def get_closest_colour_from_css3_colours(self, requested_colour):
        min_colours = {}
        for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        min_dist = min(min_colours.keys())
        if min_dist > (self.max_dist_squared * self.match_factor):
            return None
        return min_colours[min_dist]

    def get_closest_colour_from_predefined_colours(self, requested_colour):
        min_colours = {}
        for predefined_colour in self.predefined_colours:
            r_c, g_c, b_c = predefined_colour["red"], predefined_colour["green"], predefined_colour["blue"],
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = predefined_colour["key"]
        min_dist = min(min_colours.keys())
        if min_dist > (self.max_dist_squared * self.match_factor):  # if there is no close match colour it returns None
            return None
        return min_colours[min_dist]

    def calculate_dominant_colour_of_all_pixels(self, image):
        colours = []
        for i in range(self.reduced_x_pixels - 1):
            for j in range(self.reduced_y_pixels - 1):
                colours.append(self.get_closest_colour_from_predefined_colours(image[j, i]))
        counter = Counter(colours)
        return max(counter,
                   key=counter.get)  # the colour of most pixels or None if most pixels have no close matched colour

    def find_images_dominant_colour(self):
        self.image = cv2.resize(self.image, (self.reduced_x_pixels, self.reduced_y_pixels))
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        dominant_colour = self.calculate_dominant_colour_of_all_pixels(self.image)
        return dominant_colour
