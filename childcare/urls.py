
from django.conf.urls import url, include
from django.contrib import admin
from app.views import PinView, ChildCreateView, ChildUpdateView, ChildListView, ReportCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', PinView.as_view(), name="pin_view"),
    url(r'^report/create/$', ReportCreateView.as_view(), name="report_create_view"),
    url(r'^facility/$', ChildListView.as_view(), name="child_list_view"),
    url(r'^facility/create/$', ChildCreateView.as_view(), name="child_create_view"),


]
