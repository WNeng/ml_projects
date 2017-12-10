# /usr/bin/env python3.5
# -*- coding: utf-8 -*-

import webbrowser


# defend Movie class


class Movie():
    # 类初始化操作
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_url

    # 在浏览器中播放预告片
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
