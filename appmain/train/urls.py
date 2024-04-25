from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("dialog_display/", views.main_page, name="dialog_display"),
    path("theory_page/", views.theory_page, name="theory_page"),
    path('theory_page/<str:topic>/', views.topic_page, name='topic_page'),
    path("test_page/", views.test_page, name="test_page"),
    path("tusks_page/", views.tusks_page, name="tusks_page"),
    path("formuls_page/", views.formuls_page, name="formuls_page"),
    path("constants_page/", views.constants_page, name="constants_page"),
    path('registration', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout_my'),
    path('login/', views.login_view, name='login_my'),



    path('sw.js', views.ServiceWorkerView.as_view(), name=views.ServiceWorkerView.name,)
]