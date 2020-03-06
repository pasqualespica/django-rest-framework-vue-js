from rest_framework.pagination import PageNumberPagination

class SmallSetPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "pagina"