import requests
from PIL import Image, ImageFilter
from StringIO import StringIO
import pytesseract
from bs4 import BeautifulSoup


def process_image(url):
    image = _get_image(url)
    # image.filter(ImageFilter.SHARPEN)
    try:
        html = pytesseract.image_to_string(image, config="-c tessedit_create_hocr=1")
        text = _parse_html(html, conf_threshold=80)
    except IOError as e:
        print "Warning IOError with url %s" % url
        print e
        text = ""
    return text


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

def _parse_html(html, conf_threshold=80):
    text = u" "
    soup = BeautifulSoup(html, "html5lib")
    for span in soup.find_all('span', class_='ocrx_word'):
        conf = span.attrs['title'].split()[-1]
        if conf > conf_threshold:
            text += span.text.strip() + " "
    text = text.replace(u'\u2018', "'").replace(u'\u2019', "'")[:-1]
    return text
