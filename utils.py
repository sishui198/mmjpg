#!/usr/bin/env python
# coding=utf-8

import os
import json

PATH = "https://raw.githubusercontent.com/chenjiandongx/mmjpg/master/yummy/{}"


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            yield PATH.format(file)


def gen_json(paths):
    d = []
    for path in paths:
        d.append({"imgSrc": path})
    with open("yummy.json", "w+") as f:
        json.dump(d, f)


if __name__ == "__main__":
    gen_json(file_name('yummy'))
