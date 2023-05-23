"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "PRS"
admin.site.index_title = "Welcome to PRS"
admin.site.site_title = " our website"
urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.handleSignup, name="handelSignup"),
    
#    for daraz
    path("product_detail/<int:productId>", views.productDetail,name="product_detail"),
    # for sastodeal
    path("product_detail_sastodeal/<int:productId>", views.product_detail_sastodeal,name="product_detail_sastodeal"),


    # for socheko
    path("product_detail_socheko/<int:productId>", views.product_detail_socheko,name="product_detail_socheko"),



    path("daraz",views.daraz, name="daraz"),
    path("sastodeal",views.sastodeal, name="sastodeal"),
    path("socheko",views.socheko, name="socheko"),


#    review and rating
    path("submit_review_daraz/<int:product_id>", views.submit_review_daraz, name="submit_review_daraz"),
    path("submit_review_sastodeal/<int:product_id>", views.submit_review_sastodeal, name="submit_review_sastodeal"),
    path("submit_review_socheko/<int:product_id>", views.submit_review_socheko, name="submit_review_socheko")

]
