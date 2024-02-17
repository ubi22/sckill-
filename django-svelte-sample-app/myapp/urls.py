from django.contrib import admin
from django.urls import path, include
from myapp.spa.views import SpaView

app_name = 'myapp'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SpaView.as_view(), name="spa"),
    path('account/', include('user.urls'))
]
