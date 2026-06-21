from django.urls import path
from . import views
from django.conf.urls.static import static, settings

urlpatterns=[
    path('',views.signup, name='signup'),
    path('login/',views.login_view, name='login')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)