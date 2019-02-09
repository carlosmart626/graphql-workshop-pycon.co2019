"""pycon_graphql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

from graphene_django.views import GraphQLView

from pycon_graphql.schemas import schema, private_schema


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    url(r"^private-graphql", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=private_schema))),
    path('', include('frontend.urls')),
]


if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
    urlpatterns = [
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
