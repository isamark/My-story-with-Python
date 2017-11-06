from django.conf.urls import url, include
from django.contrib import admin
from app01 import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


# book_list = views.BookViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
#
# book_detail = views.BookViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    # url(r'^publishers/$',views.publisher_list),
    # url(r'^publishers/(?P<pk>[0-9]+)$', views.publisher_detail),
    # url(r'^$', views.api_root),
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title='图书管理系统')),
    # url(r'^publishers/$', views.PublisherList.as_view(), name="publisher-list"),
    # url(r'^publishers/(?P<pk>[0-9]+)$', views.PublisherDetail.as_view(), name='publisher-detail'),
    # url(r'^books/$',views.BookList.as_view(), name='book-list'),
    # url(r'^books/(?P<pk>[0-9]+)$', views.BookDetail.as_view(), name='book-detail'),
    # url(r'^books/$',book_list, name='book-list'),
    # url(r'^books/(?P<pk>[0-9]+)$', book_detail, name='book-detail'),
    url(r'^api-auto/',include('rest_framework.urls', namespace='rest_framework')),

]