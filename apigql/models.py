from django.db import models

from graphene_django import DjangoObjectType
import graphene
import graphql_geojson
from core.models import HelpRequest as HelpRequestModel


#Meta for HelpRequest
class HelpRequest(DjangoObjectType):
    class Meta:
        model = HelpRequestModel
        exclude_fields = ('search_vector','objects')

#Query
class Query(graphene.ObjectType):
    HelpRequests = graphene.List(HelpRequest)

    def resolve_helprequests(self, info):
        return HelpRequests.objects.all()

schema = graphene.Schema(query=Query)