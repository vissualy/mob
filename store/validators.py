from django.core.exceptions import ValidationError
def filesize(value):
    filesize = value.size
    if filesize > 419430400:
        raise ValidationError("maximum size is 50mb")