#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2020/2/3
# IDE: PyCharm

## flask run --host=0.0.0.0 --port=6739
import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)

from ns4w.classifier import classify
from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def classifier():
    if request.method == 'POST':
        image_path = request.form.get('image_path')
    else:
        image_path = request.args.get('image_path')
    if image_path:
        if os.path.exists(image_path):
            sfw, nsfw = classify(image_path)
            return {
                "code": 200,
                "message": "success",
                "data": {
                    "sfw": sfw,
                    "nsfw": nsfw,
                }
            }
        else:
            return {
                "code": 400,
                "message": "image_path does not exist",
                "data": None
            }

    else:
        return {
            "code": 400,
            "message": "image_path does not provided",
            "data": None
        }
