from django.core.exceptions import ValidationError
from PIL import Image


def check_for_letter(value):

    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def resize_file_image(image_object):
    img_width = 640
    img_height = 480

    img = Image.open(image_object)

    if img.width > img_width and img.height > img_height:
        img.thumbnail((640, 480))

    img.save(image_object.path)


def image_count(images):
    max_pics = 5

    if len(images) > max_pics:
        raise ValidationError(_("You can upload up to 5 pictures."))

