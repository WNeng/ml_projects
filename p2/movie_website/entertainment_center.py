# /usr/bin/env python3.5
# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# 所有喜欢的电影标题列表
title_list = ['缝纫机乐队', '长城', '战狼2']

# 所有喜欢的电影简介列表
story_list = [
    '《缝纫机乐队》讲述了青年胡亮（乔杉 饰）为守护家乡小镇集安的摇滚公园，高薪请来音乐经纪人程宫（大鹏 饰）筹办演唱会',
    '电影讲述了在古代，一支中国精英部队为保卫人类，在举世闻名的长城上与怪兽饕餮进行生死决战的故事。',
    '被开除军籍的冷锋（吴京 饰）本是因找寻龙小云（余男 饰）来到非洲，但是却突然被卷入一场非洲国家的叛乱。'
]

# 所有喜欢的电影预览图片地址列表
poster_image_url_list = [
    'http://r1.ykimg.com/0516000059B646EEADBC09B9DA079660',
    'http://r1.ykimg.com/05160000581ACE6267BC3C3967012676',
    'http://r1.ykimg.com/0516000059EEA362ADBA1FA27503A6DF'
]

# 喜欢的电影列表预告片地址列表
trailer_url_list = [
    'http://v.youku.com/v_show/id_XMzAwNDk3ODk0OA==.html?spm=a2h0j.8191423.chasing.1~3!16~A',
    'http://v.youku.com/v_show/id_XMTgxODM1NTkwOA==.html?spm=a2h0j.8191423.chasing.1~3!20~A',
    'http://v.youku.com/v_show/id_XMjc3MTIyNjExNg==.html?spm=a2h0j.8191423.chasing.1~3!35~A'

]

# 喜欢的电影列表
movie_list = []


def create_movie_list():

    index = 0
    while index < len(title_list):

        movie_list.append(media.Movie(title_list[index],
                                      story_list[index],
                                      poster_image_url_list[index],
                                      trailer_url_list[index]))

        index += 1


# 调用生成电影列表
create_movie_list()

# 生成html网页
fresh_tomatoes.open_movies_page(movie_list)
