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
    url(r'^byeokje/', views.render_page, {'page_name': 'byeokje'}),
    url(r'^byeokje_info/', views.render_page, {'page_name': 'byeokje_info'}),
    url(r'^byeokje_photo/', views.render_page, {'page_name': 'byeokje_photo'}),

    url(r'^gimpo/', views.render_page, {'page_name': 'gimpo'}),
    url(r'^gimpo_info/', views.render_page, {'page_name': 'gimpo_info'}),
    url(r'^gimpo_photo/', views.render_page, {'page_name': 'gimpo_photo'}),

    url(r'^yangju/', views.render_page, {'page_name': 'yangju'}),
    url(r'^yangju_info/', views.render_page, {'page_name': 'yangju_info'}),
    url(r'^yangju_photo/', views.render_page, {'page_name': 'yangju_photo'}),

    url(r'^namyangju/', views.render_page, {'page_name': 'namyangju'}),
    url(r'^namyangju_info/', views.render_page, {'page_name': 'namyangju_info'}),
    url(r'^namyangju_photo/', views.render_page, {'page_name': 'namyangju_photo'}),

    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="project_robots_file"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
