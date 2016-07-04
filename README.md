# where_is_lenna
Trying to access local files in aiohttp_jinja2 generated pages.  __Lenna.png__ is at the root and in the `static` directory but the html files can not find her.

__aiohttp_jinja2__ is able to render the __index.jinja2__ template, filling in the name "_Lenna_" in all the right places, but I can not access the local __Lenna.png__ image file no matter how hard I try...

`python3 where_is_lenna.py`

# Solution:
Thanks, @asvetlov -- app.router.add_static() was the key!  

```python
app.router.add_static('/static/', path='./static', name='static')
```

https://github.com/aio-libs/aiohttp_jinja2/issues/26
