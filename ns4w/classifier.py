#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2020/2/3
# IDE: PyCharm

import PIL.Image as Image
from nsfw import classify
from io import BytesIO

def classify_image(image_path=None, response=None):
    if image_path:
        image = Image.open(image_path)
    else:  ## response:
        image = Image.open(BytesIO(response.content))
    sfw, nsfw = classify(image)
    return sfw, nsfw

if __name__ == '__main__':
    pass