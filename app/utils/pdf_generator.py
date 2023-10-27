import os

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

DIR = os.getcwd()
font_config = FontConfiguration()


class PdfGenerator:
    """generate several pages pdf base on default assets that exists in project"""

    def __init__(
        self,
        main_html: object,
        css: object = None,
        header_html: object = None,
        footer_html: object = None,
        base_url: str = None,
        side_margin: int = 5,
        extra_vertical_margin: int = 30,
    ) -> None:
        self.main_html: object = main_html
        # NOTE
        # if you use footer and header from septate file
        # this method is slow and i personally don't recommend
        self.header_html: object = header_html
        self.footer_html: object = footer_html

        # css file for html access
        self.css_file: str = css
        # base url for html images or html
        self.base_url: str = f"{DIR}/{base_url}"

        self.side_margin: int = side_margin
        self.extra_vertical_margin: int = extra_vertical_margin
        self.overlay_layout: str = "@page {size: A4 portrait; margin: 0;}"

    async def compute_overlay_element(self, element: str) -> tuple:
        html = HTML(string=getattr(self, f"{element}_html"), base_url=self.base_url)
        stylesheets = [CSS(string=self.overlay_layout)]

        if self.css_file:
            stylesheets.append(CSS(self.css_file, font_config=font_config))

        element_doc = html.render(stylesheets=stylesheets, font_config=font_config)
        element_page = element_doc.pages[0]
        element_body = await PdfGenerator.get_element(element_page._page_box.all_children(), "body")
        element_body = element_body.copy_with_children(element_body.all_children())
        element_html = await PdfGenerator.get_element(element_page._page_box.all_children(), element)

        if element == "header":
            element_height = element_html.height
        if element == "footer":
            element_height = element_page.height - element_html.position_y

        return element_body, element_height

    async def apply_overlay_on_main(self, main_doc, header_body=None, footer_body=None) -> None:
        for page in main_doc.pages:
            page_body = await PdfGenerator.get_element(page._page_box.all_children(), "body")

            if header_body:
                page_body.children += header_body.all_children()
            if footer_body:
                page_body.children += footer_body.all_children()

    async def render_pdf(self) -> object:
        if self.header_html:
            header_body, header_height = await self.compute_overlay_element("header")
        else:
            header_body, header_height = None, 0

        if self.footer_html:
            footer_body, footer_height = await self.compute_overlay_element("footer")
        else:
            footer_body, footer_height = None, 0

        margins = "{header_size}px {side_margin} {footer_size}px {side_margin}".format(
            header_size=header_height + self.extra_vertical_margin,
            footer_size=footer_height + self.extra_vertical_margin,
            side_margin=f"{self.side_margin}cm",
        )
        content_print_layout = "@page {size: A4 portrait; margin: %s;}" % margins

        html = HTML(string=self.main_html, base_url=self.base_url)
        stylesheets = [CSS(string=content_print_layout)]

        if self.css_file:
            stylesheets.append(CSS(self.css_file, font_config=font_config))

        main_doc = html.render(stylesheets=stylesheets, font_config=font_config)

        if self.header_html or self.footer_html:
            await self.apply_overlay_on_main(main_doc, header_body, footer_body)
        pdf = main_doc.write_pdf()

        return pdf

    @staticmethod
    async def get_element(boxes: str, element: str):
        for box in boxes:
            if box.element_tag == element:
                return box
            return await PdfGenerator.get_element(box.all_children(), element)
