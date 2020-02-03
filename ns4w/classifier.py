#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2020/2/3
# IDE: PyCharm

import PIL.Image as Image

from nsfw import classify

def classify_image(image_path):
    image = Image.open(image_path)
    sfw, nsfw = classify(image)
    return sfw, nsfw
    # print("SFW Probability: {}".format(sfw))
    # print("NSFW Probability: {}".format(nsfw))

if __name__ == '__main__':
    pass