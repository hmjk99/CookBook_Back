from django.http import FileResponse
from django.conf import settings
import os

def get_image(request, image_name):
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')