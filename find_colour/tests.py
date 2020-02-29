from django.test import TestCase, TransactionTestCase

import cv2
from find_colour.models import ColourFinder
from find_colour.models import PredefinedColour


class ColourFinderModelTestCase(TestCase):
    """Test for the class ColourFinder"""

    def setUp(self):
        self.black = PredefinedColour()
        self.black.key = 'black'
        self.black.red = 0
        self.black.green = 0
        self.black.blue = 0
        self.white = PredefinedColour()
        self.white.key = 'white'
        self.white.red = 255
        self.white.green = 255
        self.white.blue = 255

    def test_for_black_image(self):
        image = cv2.imread('fixtures/test-sample-black.png')
        predefined_colours = [self.black, self.white]
        colour = ColourFinder(image, predefined_colours)
        dominant_colour = colour.find_images_dominant_colour()
        self.assertEqual('black', dominant_colour)

    def test_for_colour_without_close_match(self):
        image = cv2.imread('fixtures/yellow.jpg')
        predefined_colours = [self.black, self.white]
        colour = ColourFinder(image, predefined_colours)
        dominant_colour = colour.find_images_dominant_colour()
        self.assertEqual(None, dominant_colour)

    def test_for_very_low_quality_image(self):
        image = cv2.imread('fixtures/test-sample-compressed-black.png')
        predefined_colours = [self.black, self.white]
        colour = ColourFinder(image, predefined_colours)
        dominant_colour = colour.find_images_dominant_colour()
        self.assertEqual('black', dominant_colour)


class ColourFinderModelTransactionTestCase(TransactionTestCase):
    """Test for the class ColourFinder and use of the database"""
    fixtures = ['fixtures/unit-tests.json']

    def test_for_black_image(self):
        image = cv2.imread('fixtures/test-sample-black.png')
        predefined_colours = PredefinedColour.objects.all()
        colour = ColourFinder(image, predefined_colours)
        dominant_colour = colour.find_images_dominant_colour()
        self.assertEqual('black', dominant_colour)

