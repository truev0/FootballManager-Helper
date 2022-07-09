# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os

# BASE DIRECTORY
from gui import BASE_DIR


# SET SVG ICON
# ///////////////////////////////////////////////////////////////
def set_svg_icon(icon_name):
    """
    It takes the name of an SVG icon file as a string, and returns the full path to that file

    :param icon_name: The name of the icon file
    :return: The path to the icon.
    """
    folder = "images/svg_icons/"
    path = os.path.join(BASE_DIR, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon


# SET SVG IMAGE
# ///////////////////////////////////////////////////////////////
def set_svg_image(icon_name):
    """
    It takes the name of an SVG image file as a string, and returns the full path to that file

    :param icon_name: The name of the icon you want to use
    :return: The path to the icon.
    """
    folder = "images/svg_images/"
    path = os.path.join(BASE_DIR, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon


# SET IMAGE
# ///////////////////////////////////////////////////////////////
def set_image(image_name):
    """
    It takes the name of an image file as an argument, and returns the full path to that image file

    :param image_name: The name of the image you want to use
    :return: The image is being returned.
    """
    folder = "images/png_images/"
    path = os.path.join(BASE_DIR, folder)
    image = os.path.normpath(os.path.join(path, image_name))
    return image
