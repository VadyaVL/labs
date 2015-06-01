from tastypie.resources import ModelResource
from models import *
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie import fields

class ViewEncumbranceResource(ModelResource):

    class Meta:
        queryset = ViewEncumbrance.objects.all()
        resource_name = 'viewencumbrance'
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
        bundle = super(ViewEncumbranceResource, self).obj_create(bundle, **kwargs)
        return bundle

class TypeOfEncumbranceResource(ModelResource):

    class Meta:
        queryset = TypeOfEncumbrance.objects.all()
        resource_name = 'typeofencumbrance'
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
        bundle = super(TypeOfEncumbranceResource, self).obj_create(bundle, **kwargs)
        return bundle

class TypeRegResource(ModelResource):

    class Meta:
        queryset = TypeReg.objects.all()
        resource_name = 'typereg'
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
        bundle = super(TypeRegResource, self).obj_create(bundle, **kwargs)
        return bundle

class TypeOfCurrencyResource(ModelResource):

    class Meta:
        queryset = TypeOfCurrency.objects.all()
        resource_name = 'typeofcurrency'
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
        bundle = super(TypeOfCurrencyResource, self).obj_create(bundle, **kwargs)
        return bundle

class AddressResource(ModelResource):

    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch', 'options']
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
        bundle = super(AddressResource, self).obj_create(bundle, **kwargs)
        return bundle

class PersonResource(ModelResource):

    Address = fields.ForeignKey(AddressResource, 'Address', full=True, null=True)

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

class ObjectResource(ModelResource):

    class Meta:
        queryset = Object.objects.all()
        resource_name = 'object'
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
        bundle = super(ObjectResource, self).obj_create(bundle, **kwargs)
        return bundle

class DocumentBaseResource(ModelResource):

    class Meta:
        queryset = DocumentBase.objects.all()
        resource_name = 'documentbase'
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
        bundle = super(DocumentBaseResource, self).obj_create(bundle, **kwargs)
        return bundle

class TermsResource(ModelResource):

    TypeOfCurrency = fields.ForeignKey(TypeOfCurrencyResource, 'TypeOfCurrency')

    class Meta:
        queryset = Terms.objects.all()
        resource_name = 'terms'
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
        bundle = super(TermsResource, self).obj_create(bundle, **kwargs)
        return bundle

class EncumbranceResource(ModelResource):

    TypeOfEncumbrance = fields.ForeignKey(TypeOfEncumbranceResource, 'TypeOfEncumbrance', full=True, null=True)
    TypeReg = fields.ForeignKey(TypeRegResource, 'TypeReg', full=True, null=True)
    ViewEncumbrance = fields.ForeignKey(ViewEncumbranceResource, 'ViewEncumbrance', full=True, null=True)
    WPerson = fields.ManyToManyField(PersonResource, 'WPerson', full=True, null=True)
    SPerson = fields.ManyToManyField(PersonResource, 'SPerson', full=True, null=True)

    Obj = fields.OneToOneField(ObjectResource, 'Obj', full=True, null=True)
    DocBase = fields.OneToOneField(DocumentBaseResource, 'DocBase', full=True, null=True)
    Term = fields.OneToOneField(TermsResource, 'Term', full=True, null=True)

    class Meta:
        queryset = Encumbrance.objects.all()
        resource_name = 'encumbrance'
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
        bundle = super(EncumbranceResource, self).obj_create(bundle, **kwargs)
        return bundle