# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from PIL import Image
import pytesseract
import argparse
import cv2
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from cookbook.models import Page

# Get an instance of a logger
logger = logging.getLogger(__name__)
# logging.disable(logging.ERROR)

# The purpose of this command is to perform OCR on recipe page images
class Command(BaseCommand):
    help = 'Performs OCR on recipe images and saves text result in Page object'

    def add_arguments(self, parser):
        parser.add_argument('--num', nargs=1, help="the number of prs to import. -1 imports all.")
        parser.add_argument('--tag', nargs=1, help="string tag for this batch")

    def handle(self, *args, **options):

        num = int(options['num'][0] if options['num'] else 0)
        if num:
            logger.debug("number of items to import: %s" % num)

        pages = Page.objects.all()

        logger.debug("Perform OCR on %u pages" % pages.count())

        blur = False
        threshold = False

        for page in pages[:10]:
            from skimage import io
            image = io.imread(page.img_lg_url)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # write the grayscale image to disk as a temporary file so we can
            # apply OCR to it
            filename = "{}.png".format(os.getpid())
            cv2.imwrite(filename, gray)
            # load the image as a PIL/Pillow image, apply OCR, and then delete
            # the temporary file
            text = pytesseract.image_to_string(Image.open(filename))
            os.remove(filename)
            page.ocr_search_text = text
            page.save()
