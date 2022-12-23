from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.count),
            # если нужны ссылки пагинации взад и вперед разкомментировать
            # ('next', self.get_next_link()),
            # ('previous', self.get_previous_link()),
            ('items', data)
        ]))