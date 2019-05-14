# vim:fileencoding=utf-8
import json
import six
from django.template.loader import render_to_string

__version__ = '0.3.2+whyfly.2'


class SirTrevorContent(six.text_type):
    @property
    def html(self):
        html = []
        if len(self):
            content = json.loads(self)
            for block in content['data']:
                template_name = 'sirtrevor/blocks/%s.html' % block['type']
                html.append(render_to_string(template_name, block['data']))
        return u''.join(html)


custom_blocks_registry = {}


def register_block(block, name=None):
    if name is None:
        name = block.name
    custom_blocks_registry[name] = block
