from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Project2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'main.views.login', name="login"),
    url(r'^signup/$', 'main.views.signup', name="signup"),
    url(r'^forget/$', 'main.views.forget', name="forget"),
]
