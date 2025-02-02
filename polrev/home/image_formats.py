from django.utils.html import format_html
from wagtail.images.formats import Format, register_image_format


class CaptionedLeft(Format):

    def image_to_html(self, image, alt_text, extra_attributes=None):

        default_html = super().image_to_html(image, alt_text, extra_attributes)

        return format_html(
            '<figure class="figure richtext-image left">{}<figcaption class="figure-caption">{}</figcaption></figure>',
            default_html,
            alt_text,
        )


register_image_format(
    CaptionedLeft(
        "captioned_left", "Left-aligned Captioned", "richtext-image", "width-750"
    )
)


class CaptionedRight(Format):

    def image_to_html(self, image, alt_text, extra_attributes=None):

        default_html = super().image_to_html(image, alt_text, extra_attributes)

        return format_html(
            '<figure class="figure richtext-image right">{}<figcaption class="figure-caption">{}</figcaption></figure>',
            default_html,
            alt_text,
        )


register_image_format(
    CaptionedRight(
        "captioned_right", "Right-aligned Captioned", "richtext-image", "width-750"
    )
)
