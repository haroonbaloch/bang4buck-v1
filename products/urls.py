from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from bang4buck import settings
from . import views
app_name = 'products'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('compare/', views.compare, name='compare'),

    path('compare/<int:category_id>/<int:product1_id>/<int:product2_id>/', views.compare, name='compare'),
    path('add_product/', views.add_product, name='add_product'),
    path('categories/', views.all_categories, name='all_categories'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    path('admin/products/attributes/<int:attribute_id>/subattributes/', views.get_subattributes,
         name='get_subattributes'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)