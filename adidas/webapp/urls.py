from django.urls import path

from webapp.views import AdidasListView, CostumesListView, ProductDetailView, CapsAndHastsListView, HoodiesListView, \
    JacketsListView, ShoesListView, TShirtsListView, TrousersListView, VestsListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView
from django.contrib.auth import views as auth_views

app_name = "webapp"

urlpatterns = [
    path('', AdidasListView.as_view(), name="index"),
    path('costumes/', CostumesListView.as_view(), name="costumes_list"),
    path('caps_and_hats/', CapsAndHastsListView.as_view(), name="caps_and_hats_list"),
    path('hoodies/', HoodiesListView.as_view(), name="hoodies_list"),
    path('jackets/', JacketsListView.as_view(), name="jackets_list"),
    path('shoes/', ShoesListView.as_view(), name="shoes_list"),
    path('t-shirts/', TShirtsListView.as_view(), name="t-shirts_list"),
    path('trousers/', TrousersListView.as_view(), name="trousers_list"),
    path('vests/', VestsListView.as_view(), name="vests_list"),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
