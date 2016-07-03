#!/usr/bin/env python3
# coding: utf-8

import asyncio
from aiohttp import web
import aiohttp_jinja2
from jinja2 import FileSystemLoader as FSLoader
import webbrowser
# import multiprocessing
import os

PORT = 8080


def launch_browser(host_and_port):
    asyncio.sleep(0.1)  # give the server a tenth of a second to come up
    webbrowser.open(host_and_port)


@aiohttp_jinja2.template('index.jinja2')
async def handler(request):
    return {'title': 'Lenna'}


def run_webserver(port=8080):
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=FSLoader(os.curdir, followlinks=True))
    app.router.add_route('GET', '/', handler)
    web.run_app(app, port=port)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, launch_browser, 'localhost:{}'.format(PORT))
    run_webserver(port=PORT)
