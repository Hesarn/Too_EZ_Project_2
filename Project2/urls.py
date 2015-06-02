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
    url(r'^post$', 'main.views.show_post', name='showPost'),
    url(r'^post/(\d+)/(\d+)$', 'main.views.show_post'),
    url(r'^profile$', 'main.views.show_user_profile', name='showProfile'),
    url(r'^profile/(\d+)$', 'main.views.show_other_profiles'),
    url(r'^ajax/(\d+)$', 'main.views.ajax_get_post'),
    url(r'^ajax/commentOnPost$', 'main.views.ajax_comment_on_post', name='comment'),
    url(r'^ajax/commentOnPost/(\d+)$', 'main.views.ajax_comment_on_post'),
    url(r'^ajax/LikePost$', 'main.views.ajax_like_post', name='likePost'),
    url(r'^ajax/LikePost/(\d+)$', 'main.views.ajax_like_post'),
    url(r'^users$', 'main.views.show_users', name='showUsers'),
    url(r'^users/(\w+)/(\d+)$', 'main.views.show_users'),
    url(r'^ajax/follow_unfollow$', 'main.views.follow_action', name='followUnfollow'),
    url(r'^ajax/follow_unfollow/(\d+)$', 'main.views.follow_action'),
    url(r'^search/$', 'main.views.search', name='search'),
    url(r'^search/(\w+)$', 'main.views.search'),
]
