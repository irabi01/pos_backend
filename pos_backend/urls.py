from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from graphene_django.views import GraphQLView
from pos_backend.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^pos/api/data/77_/graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^gql/', csrf_exempt(GraphQLView.as_view(batch=True))),
]
