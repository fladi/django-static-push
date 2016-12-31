# -*- coding: utf-8 -*-


class StaticPush(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_staticpush', set())
        response = self.get_response(request)
        assets = getattr(request, '_staticpush', set())
        if assets:
            response.setdefault(
                'Link',
                ','.join(
                    map(
                        lambda x: '<{}>;rel=preload'.format(x),
                        assets
                    )
                )
            )
        delattr(request, '_staticpush')
        return response
