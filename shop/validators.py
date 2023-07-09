from django.core.exceptions import ValidationError


def check_for_letter(value):

    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

