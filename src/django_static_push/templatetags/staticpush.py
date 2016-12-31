from django import template
from django.templatetags.static import StaticNode

register = template.Library()


class StaticPushNode(StaticNode):

    def url(self, context):
        url = super(StaticPushNode, self).url(context)
        request = context.get('request', None)
        if request:
            request._staticpush.add(url)
        return url


@register.tag('staticpush')
def do_static_push(parser, token):
    return StaticPushNode.handle_token(parser, token)
