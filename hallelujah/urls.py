"""saturn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from hallelujah import settings
from app import views, apis
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_page, {'page_name': 'index'}),
    url(r'^sangjo$', views.render_page, {'page_name': 'sangjo'}),

    url(r'^north-hanriver$', views.render_page, {'page_name': 'north-hanriver'}),
    url(r'^north-hanriver/daeja/', views.render_page, {'page_name': 'daeja'}),
    url(r'^north-hanriver/ilsan/', views.render_page, {'page_name': 'ilsan'}),
    url(r'^north-hanriver/paju/', views.render_page, {'page_name': 'paju'}),
    url(r'^north-hanriver/byeokje/', views.render_page, {'page_name': 'byeokje'}),
    url(r'^north-hanriver/yangju/', views.render_page, {'page_name': 'yangju'}),
    url(r'^north-hanriver/yeoncheon/', views.render_page, {'page_name': 'yeoncheon'}),

    url(r'^forestpark$', views.render_page, {'page_name': 'forestpark'}),
    url(r'^forestpark/gimpo$', views.render_page, {'page_name': 'forestpark-gimpo'}),
    url(r'^forestpark/yangju$', views.render_page, {'page_name': 'forestpark-yangju'}),
    url(r'^forestpark/anseong$', views.render_page, {'page_name': 'forestpark-anseong'}),
    url(r'^forestpark/yongin$', views.render_page, {'page_name': 'forestpark-yongin'}),
    url(r'^forestpark/yeoncheon$', views.render_page, {'page_name': 'forestpark-yeoncheon'}),

    url(r'^south-hanriver$', views.render_page, {'page_name': 'south-hanriver'}),
    url(r'^south-hanriver/bundang$', views.render_page, {'page_name': 'south-bundang'}),
    url(r'^south-hanriver/pyeongtaek$', views.render_page, {'page_name': 'south-pyeongtaek'}),
    url(r'^south-hanriver/yongin$', views.render_page, {'page_name': 'south-yongin'}),
    url(r'^south-hanriver/anseong$', views.render_page, {'page_name': 'south-anseong'}),

    url(r'^cemetery$', views.render_page, {'page_name': 'cemetery'}),
    url(r'^cemetery/yongin$', views.render_page, {'page_name': 'cemetery-yongin'}),
    url(r'^cemetery/gwangju$', views.render_page, {'page_name': 'cemetery-gwangju'}),
    url(r'^cemetery/yangpyeong$', views.render_page, {'page_name': 'cemetery-yangpyeong'}),
    url(r'^cemetery/dongducheon$', views.render_page, {'page_name': 'cemetery-dongducheon'}),

    url(r'^burial$', views.render_page, {'page_name': 'move'}),
    url(r'^burial/move$', views.render_page, {'page_name': 'move'}),
    url(r'^burial/open$', views.render_page, {'page_name': 'open'}),

    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="project_robots_file"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
