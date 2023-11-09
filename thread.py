import threading
import requests
import time
import multiprocessing
import asyncio


# import aiohttp


def time_func(function):
    global wrapped

    def wrapped(*args, **kwargs):
        start_time = time.time()
        time_ = function(*args, **kwargs)
        print(f"время скачивание = {start_time - time.time()}")
        return time_

    return wrapped


# @time_func
# async def get_url_asyn(img):
#     async with aiohttp.Clientsession() as s:
#         async with s.get(img) as responce:
#             with open(f'images/{img.split('/')[-1]}', 'wb') as image:
#                 images = await responce.content()
#                 image.write(images)


@time_func
def get_url(img):
    try:
        if img not in ['1', '2', '3']:
            response = requests.get(img)
            with open(f'images/{img.split('/')[-1]}', 'wb') as image:
                image.write(response.content)

            print(f'изображение {img.split('/')[-1]} успешно добавленно')
    except:
        print(f'ups "{img}" не URL')


def treads_(urls):
    ts = time.time()
    treads = []
    for url in urls:
        t = threading.Thread(target=get_url, args=(url,))
        treads.append(t)
        t.start()

    for tread in treads:
        tread.join()
    tf = time.time()
    print(f'общее время загрузки {tf - ts}')


def proc(urls):
    ts = time.time()
    proces = []
    for url in urls:
        t = multiprocessing.Process(target=get_url, args=(url,))
        proces.append(t)
        t.start()

    for proc in proces:
        proc.join()
    tf = time.time()
    print(f'общее время загрузки {tf - ts}')


async def main(urls):
    tasks = []
    for url in urls:
        tasks.append(get_url(url, ))
    await asyncio.gather(*tasks)
