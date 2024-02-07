from shop.models import Products
from django.db.models import Q


''' Организация поиска по сайту'''


def q_search(query):
    keyword = [word for word in query.split() if len(word) >= 1]
    q_object = Q()
    for token in keyword:
        q_object |= Q(description__icontains=token)
        q_object |= Q(name__icontains=token)
    return Products.objects.filter(q_object)
