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

    url(r'^south-hanriver$', views.render_page, {'page_name': 'south-hanriver'}),

    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="project_robots_file"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
