from unicodedata import name
from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "auctions"

urlpatterns = [
    path("admin/",admin.site.urls),
    path("register/",views.register_view, name="register"),
    path("", views.login_view  ,name="frontpage"),
    path("login/",views.login_view ,name="login"),
    path("items/",views.items_view,name="items"),
    path("profile/",views.profile_view,name="profiles"),
    path("profile/<int:id>",views.profile_detail),
    path('items/<int:id>',views.item_detail),
    path("comments/",views.comment_view,name="comments"),
    path("logout/",views.logoutView,name="logout"),
]

urlpatterns=format_suffix_patterns(urlpatterns)
   # path("", views.indexview, name="index"),
    #path("login/", views.login_view, name="login"),
    #path("logout", views.logout_view, name="logout"),
    #path("register", views.register, name="register"),
    #path("cards", views.cards_view, name="cards"),
    #path("add", views.add, name="add"),
    #path("add_comment", views.add_comment, name="add_comment"),
    #path("listing_details", views.listing_details_view, name="listing_details"),
    #path("watchlist", views.watchlist_view, name="watchlist"),
    #path("category_list", views.category_list, name="category_list"),
    #path("category_list/<str:category>", views.category_list_redirect, name="category_list_redirect"),
    #path("add_to_watchlist", views.add_to_watchlist, name="add_to_watchlist"),
    #path("place_bid", views.place_bid, name="place_bid"),
    #path("end_listing", views.end_listing, name="end_listing"),
    #path("auctions_history", views.auctions_history, name="auctions_history"),
    #path("delete_item_watchlist", views.delete_item_watchlist, name="delete_item_watchlist")
    