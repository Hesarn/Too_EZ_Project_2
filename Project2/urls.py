from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT

urlpatterns = [
    # Examples:
    # url(r'^$', 'Project2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, }),

    url(r'^captcha/', include('captcha.urls')),

    url(r'^login/$', 'main.views.login_user', name="login"),
    url(r'^signup/$', 'main.views.signup', name="signup"),
    url(r'^forget/$', 'main.views.forget', name="forget"),
    url(r'^timeline/$', 'main.views.timeLine', name="timeLine"),
    url(r'^logout/$', 'main.views.logout_user', name="logout"),
    url(r'^movieProfile$', 'main.views.movie_profile', name="movieProfile"),
    url(r'^movieProfile/(\w+)$', 'main.views.movie_profile'),
]
