from jinja2 import Template


async def open_file_from_assets(path: str, **kwarg) -> object:
    """renders the html file from assets folder and with data input
    return them as object

    Args:
        path (str): file name of the html with maybe the path (no need for .html)

    Returns:
        object: rendered html object
    """
    with open(path) as html:
        template_str = html.read()
        template = Template(template_str)
        rendered_data = template.render(**kwarg)
        return rendered_data
