# 当pyppeteer下载Chromium失败时运行此脚本，找出浏览器应该存储的位置，手动下载该浏览器放到相应的路径下即可，下载地址：https://registry.npmmirror.com/binary.html?path=chromium-browser-snapshots/#/

import pyppeteer.chromium_downloader

print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))