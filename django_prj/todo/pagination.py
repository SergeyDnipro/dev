from rest_framework import pagination

class MyPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'stranica'