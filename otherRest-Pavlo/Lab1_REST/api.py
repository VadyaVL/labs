from tastypie.resources import ModelResource
from models import *
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.exceptions import ImmediateHttpResponse
from django.http import HttpResponse

class CorsResource(ModelResource):
    """ adds CORS headers for cross-domain requests """
    def patch_response(self, response):

        allowed_headers = ['Content-Type', 'Authorization', 'DELETE']
        response['Access-Control-Allow-Methods'] = 'get, post, DELETE, put, PUT, patch'
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = ','.join(allowed_headers)
        return response

    def dispatch(self, *args, **kwargs):
        """ calls super and patches resonse headers
            or
            catches ImmediateHttpResponse, patches headers and re-raises
        """

        try:
            response = super(CorsResource, self).dispatch(*args, **kwargs)
            return self.patch_response(response)
        except ImmediateHttpResponse, e:
            response = self.patch_response(e.response)
            # re-raise - we could return a response but then anthing wrapping
            # this and expecting an exception would be confused
            raise ImmediateHttpResponse(response)

    def method_check(self, request, allowed=None):
        """ Handle OPTIONS requests """
        if request.method.upper() == 'OPTIONS':

            if allowed is None:
                allowed = []

            allows = ','.join([s.upper() for s in allowed])

            response = HttpResponse(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        return super(CorsResource, self).method_check(request, allowed)

class AddressResource(CorsResource):

    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'
        allowed_methods = ['get', 'post', 'delete', 'put', 'PUT', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(AddressResource, self).obj_create(bundle, **kwargs)
        return bundle

class PersonResource(CorsResource):

    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(PersonResource, self).obj_create(bundle, **kwargs)
        return bundle

class FormOfLegResource(CorsResource):

    class Meta:
        queryset = FormOfLeg.objects.all()
        resource_name = 'formofleg'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(FormOfLegResource, self).obj_create(bundle, **kwargs)
        return bundle

class TypeOfSocFormResource(CorsResource):

    class Meta:
        queryset = TypeOfSocForm.objects.all()
        resource_name = 'typeofsocform'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(TypeOfSocFormResource, self).obj_create(bundle, **kwargs)
        return bundle

class SocialFormationResource(CorsResource):

    Address = fields.ForeignKey(AddressResource, 'Address', full=True, null=True)
    Person = fields.ForeignKey(PersonResource, 'Person', full=True, null=True)
    TypeOfSocForm = fields.ForeignKey(TypeOfSocFormResource, 'TypeOfSocForm', full=True, null=True)
    FormOfLeg = fields.ForeignKey(FormOfLegResource, 'FormOfLeg', full=True, null=True)

    class Meta:
        queryset = SocialFormation.objects.all()
        resource_name = 'socialformation'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(SocialFormationResource, self).obj_create(bundle, **kwargs)
        return bundle

class FiliaResource(CorsResource):

    SocialFormation = fields.ForeignKey(SocialFormationResource, 'SocialFormation', full=True, null=True)
    Address = fields.ForeignKey(AddressResource, 'Address', full=True, null=True)
    Person = fields.ForeignKey(PersonResource, 'Person', full=True, null=True)

    class Meta:
        queryset = Filia.objects.all()
        resource_name = 'filia'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(FiliaResource, self).obj_create(bundle, **kwargs)
        return bundle



######################
'''
class AdresaResource(CorsResource):

    class Meta:
        queryset = Adresa.objects.all()
        resource_name = 'adresa'
        allowed_methods = ['get', 'post', 'delete', 'put', 'PUT', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        default_format = 'application/json'

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(AdresaResource, self).obj_create(bundle, **kwargs)

        return bundle

class ArbitrazhnijResource(CorsResource):

    Adresa = fields.ForeignKey(AdresaResource, 'Adresa', full=True, null=True)

    class Meta:
        queryset = Arbitrazhnij.objects.all()
        resource_name = 'arbitrazhnij'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        default_format = 'application/json'

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(ArbitrazhnijResource, self).obj_create(bundle, **kwargs)

        return bundle

class BorzhnikResource(CorsResource):

    Adresa = fields.ForeignKey(AdresaResource, 'Adresa', full=True, null=True)
    Arbitrazh = fields.ForeignKey(ArbitrazhnijResource, 'Arbitrazh', full=True, null=True)

    class Meta:
        queryset = Borzhnik.objects.all()
        resource_name = 'borzhnik'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        default_format = 'application/json'

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(BorzhnikResource, self).obj_create(bundle, **kwargs)

        return bundle

class KreditorResource(CorsResource):

    Adresa = fields.ForeignKey(AdresaResource, 'Adresa', full=True, null=True)

    class Meta:
        queryset = Kreditor.objects.all()
        resource_name = 'kreditor'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        default_format = 'application/json'

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(KreditorResource, self).obj_create(bundle, **kwargs)

        return bundle

class VimogiResource(CorsResource):

    Kreditor = fields.ForeignKey(KreditorResource, 'Kreditor', full=True, null=True)
    Borzhnik = fields.ForeignKey(BorzhnikResource, 'Borzhnik', full=True, null=True)

    class Meta:
        queryset = Vimogi.objects.all()
        resource_name = 'vimogi'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        default_format = 'application/json'

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(VimogiResource, self).obj_create(bundle, **kwargs)

        return bundle '''''