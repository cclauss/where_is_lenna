#!/usr/bin/env python3
# coding: utf-8

import asyncio
from aiohttp import web
#import aiohttp_jinja2
#from jinja2 import FileSystemLoader as FSLoader
from jinja2 import Environment, FileSystemLoader
import webbrowser
import os

PORT = 8080


def launch_browser(host_and_port):
    asyncio.sleep(0.1)  # give the server a tenth of a second to come up
    webbrowser.open(host_and_port)


def get_html(context_dict):
    env = Environment(loader=FileSystemLoader(os.curdir))
    template = env.get_template('index.jinja2')
    return template.render(context_dict)


async def handler(request):
    return web.Response(body=get_html({'title': 'Lenna'}).encode())


def run_webserver(port=8080):
    app = web.Application()
    app.router.add_route('GET', '/', handler)
    lenna = app.router.add_resource('/Lenna.png', name='Lenna')
    web.run_app(app, port=port)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, launch_browser, 'localhost:{}'.format(PORT))
    run_webserver(port=PORT)
