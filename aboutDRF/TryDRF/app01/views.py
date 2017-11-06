# coding=utf-8
from django.shortcuts import render
from app01.serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from app01.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from app01.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets

# @api_view(['GET','POST'])
# def publisher_list(request):
#     queryset = Publisher.objects.all()

    # 1:最原始的方法
    # data = []
    # for i in queryset:
    #     p_tmp = {
    #         'name':i.name,
    #         'address':i.address
    #     }
    #
    #     data.append(p_tmp)
    # print(data)

    # 2:此方法有局限性，比如图片这类字段没办法转，但是比刚才那个高级一点
    # data = []
    # from django.forms.models import model_to_dict
    # for i in queryset:
    #     data.append(model_to_dict(i))
    #
    # import json
    # return HttpResponse(json.dumps(data),content_type='application/json')

    # 3:方法3
    # from django.core import serializers
    # data = serializers.serialize('json',queryset)
    # return HttpResponse(data, content_type='application/json')

    # 从方法１到方法３体现了一种哲学思想，也有一种数学思维，举个例子说明这种数学思维：
    # 如果某条公理可以推导出某一个定理．那么只需要记住公理就够了

    # 4:方法4

    # from app01 import serializers
    # serializer = serializers.PublisherSerializer(queryset,many=True)
    # import json
    # return HttpResponse(json.dumps(serializer.data),content_type='application/json')

    # 然而这些都是浮云，他们只能单单提供数据库信息，
    # 我们今天学得djangorestframework,它提供了一套更高级别的序列化
    # 那么他有啥好处：
    # 不仅是把数据库的数据以json格式展示给客户，还需要把客户端通过API提交的字符串转化为数据库中的数据，
    # 也就是需要一个json与model之间互相的转换
    # 完成查询，修改，新添信息
    # 这时候我们不能再用django自带的序列化了，必须用到djangorestframework提供的序列化




# @api_view(['GET','POST'])
# def publisher_list(request):
#     queryset = Publisher.objects.all()
#     """
#     get:列出所有的出版社．post创建一个新的出版社
#     """
#
#     if request.method == 'GET':
#         queryset = Publisher.objects.all()
#         s = PublisherSerializer(queryset, many=True)
#         return Response(s.data)
#
#     elif request.method == 'POST':
#         s = PublisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def publisher_detail(request, pk):
#     try:
#         publisher = Publisher.objects.get(pk=pk)
#     except:
#         return Response(status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         s = PublisherSerializer(publisher)
#         return Response(s.data)
#
#     elif request.method == 'PUT':
#         s = PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class PublisherList(APIView):
#     # 　查询所有的出版社
#     def get(self, request, farmat=None):
#         queryset =  Publisher.objects.all()
#         s = PublisherSerializer(queryset, many=True)
#         return Response(s.data)
#
#     # 添加出版社
#     def post(self, request, format=None):
#         s = PublisherSerializer(data=request.data)
#         if s.is_valid():   # 如果数据没问题
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status.HTTP_400_BAD_REQUEST)
#
#
# class PublisherDetail(APIView):
#     """
#     单个出版社，查看，修改，删除
#     """
#
#     def get_object(self, pk):
#         try:
#             return Publisher.objects.get(pk=pk)
#         except Publisher.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = PublisherSerializer(publisher)
#         return Response(s.data)
#
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = PublisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 使用混合(非常重要)


# class PublisherList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PublisherDetail(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# 从混合类到类视图
# class PublisherList(generics.ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#     """
#     默认必须有用户登录才能与数据面对面，但是缺点是任何用户都有读写的权限
#     如何只让数据的拥有者拥有写的权限呢，那就因引入第二个参数IsOwnerOrReadOnly
#     结果就是只有数据的拥有者才有权利改变数据
#     当然直接清空下面表达式的话，就是无论登录与否都拥有读写权限
#     """
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(operator=self.request.user)
#
# class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#
# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'publisher':reverse('publisher-list', request=request, format=format),
#         'books':reverse('book-list', request=request, format=format)
#     })

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'publisher':reverse('publisher-list', request=request, format=format),
#         'books':reverse('book-list', request=request, format=format)
#     })







