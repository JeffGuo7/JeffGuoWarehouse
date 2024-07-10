import asyncio, time
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, dumpio=True, autoClose=False,
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
    page = await browser.newPage()  # 打开新的标签页
    await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
    await page.goto('https://www.baidu.com/?tn=99669880_hao_pg')  # 访问主页

    # evaluate()是执行js的方法，js逆向时如果需要在浏览器环境下执行js代码的话可以利用这个方法
    # js为设置webdriver的值，防止网站检测
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # await page.screenshot({'path': './1.jpg'})   # 截图保存路径

    page_text = await page.content()  # 获取网页源码
    print(page_text)
    time.sleep(1)

asyncio.run(main())
# asyncio.get_event_loop().run_until_complete(main())  # 调用