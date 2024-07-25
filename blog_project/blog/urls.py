from django.urls import path
from .import views

urlpatterns = [
    path('',views.Post_List,name='Post_List'),
    path('Register',views.Register,name='Register'),
    path('Login',views.Login,name='Login'),
    path('logout',views.logout,name="logout"),
    path('CreatePost',views.CreatePost,name='CreatePost'),
    path('allpost',views.allpost,name='allpost'),
    path('deletepost/<int:post_id>/',views.deletepost,name='deletepost'),
    path('editpost/<int:post_id>/',views.editpost,name='editpost'),
    path('addcomment/<int:post_id>/',views.addcomment,name='addcomment'),
    path('viewcomment/<int:post_id>',views.viewcomment,name='viewcomment'),

    

]
