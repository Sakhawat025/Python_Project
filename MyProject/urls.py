from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # <-- add include
from users import views as userviews
from myapp import views as myviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home, name='home'),
    path('products/', myviews.product_list, name='product_list'),
    path('products_details/<str:id>', myviews.product_details, name='product_details'),
    path('upload/', myviews.upload_product, name='upload_product'),
    path('update/<str:id>', myviews.update_product, name='update_product'),
    path('loyality/', myviews.loyality, name='loyality'),
    path('delete/<str:id>', myviews.delete_product, name='delete'),
    path('login/', userviews.login_view, name='login'),
    path('signup/', userviews.register_view, name='signup'),
    path('rent/<int:product_id>/', myviews.rent_product, name='rent_product'),
    path('users/', include('users.urls')),
    path('booknow/', myviews.booknow, name='booknow'),
    path('membership/', myviews.membership, name='membership'),
    path('detailing/', myviews.detailing, name='detailing'),
    path('home/', myviews.home, name='home'),
    path('become_member/', myviews.become_member,
          name='become_member'),
    path('autowash/', myviews.autowash, name='autowash'),
    path('garage/', myviews.garage, name='garage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

