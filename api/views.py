import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

'''
def api_home(request, *args, **kwargs):
    """
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET) # url query params
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers # request.META -> 
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
"""
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price'])
    return JsonResponse(data)
        # json_data_str =json.dumps(data)
        
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        
        # model instance (model_data)
        # turn a python dict
        # serialization
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})
    
    '''
    
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id','title','price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
