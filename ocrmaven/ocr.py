import requests
from PIL import Image, ImageFilter
from StringIO import StringIO
import pytesseract


def process_image(url):
    image = _get_image(url)
    # image.filter(ImageFilter.SHARPEN)
    try:
        text = pytesseract.image_to_string(image)
    except IOError as e:
        print "Warning IOError with url %s" % url
        print e
        text = ""
    return text


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))
