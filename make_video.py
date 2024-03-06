#!/usr/bin/env python

"""make_video.py: Make video out of images."""

__author__      = "FC"


import ffmpeg

video = ffmpeg.input('cds_images/*.png', pattern_type='glob',framerate=1).output("video.mp4").run()

