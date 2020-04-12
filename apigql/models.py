from django.db import models

from graphene_django import DjangoObjectType
import graphene
import graphql_geojson
from core.models import HelpRequest


#Meta for HelpRequest
class HelpRequestType(DjangoObjectType):
    class Meta:
        model = HelpRequest
        exclude_fields = ('search_vector',)

#Query
class Query(graphene.ObjectType):
    all_HelpRequests = graphene.List(HelpRequestType)

    def resolve_helprequests(self, info):
        return HelpRequest.objects.all()

schema = graphene.Schema(query=Query)

