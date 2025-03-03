from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from blogapp.views import register_user ,create_blog
urlpatterns = [
   
    path('', views.blog_list_page, name='blog_list_page'),  # Renders the blog list page
    # path('blog/<int:pk>/', views.blog_detail_page, name='blog_detail_page'),  # Renders a specific blog post
    # path('update-profile/', views.update_profile_page, name='update_profile_page'),  # Renders the profile update page
    # path('create-blog/', views.create_blog_page, name='create_blog_page'),  # Renders the create blog page
    
    path("register_user/",views.register_user, name="register_user"),
    path("create_blog/",views.create_blog,name="create_blog"),
    path("blog_list",views.blog_list,name="blog_list"),
    path("update_blog/<int:pk>/",views.update_blog,name="update_blog"),
    path("delete_blog/<int:pk>/", views.delete_blog, name="delete_blog"),
    path("update_user/", views.update_user_profile, name="update_user"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)