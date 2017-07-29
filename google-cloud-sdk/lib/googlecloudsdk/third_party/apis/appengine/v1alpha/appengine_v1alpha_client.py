"""Generated client library for appengine version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.appengine.v1alpha import appengine_v1alpha_messages as messages


class AppengineV1alpha(base_api.BaseApiClient):
  """Generated client library for service appengine version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://appengine.googleapis.com/'

  _PACKAGE = u'appengine'
  _SCOPES = [u'https://www.googleapis.com/auth/appengine.admin', u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = u'v1alpha'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'AppengineV1alpha'
  _URL_VERSION = u'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new appengine handle."""
    url = url or self.BASE_URL
    super(AppengineV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.apps_authorizedCertificates = self.AppsAuthorizedCertificatesService(self)
    self.apps_authorizedDomains = self.AppsAuthorizedDomainsService(self)
    self.apps_domainMappings = self.AppsDomainMappingsService(self)
    self.apps_locations = self.AppsLocationsService(self)
    self.apps_operations = self.AppsOperationsService(self)
    self.apps = self.AppsService(self)

  class AppsAuthorizedCertificatesService(base_api.BaseApiService):
    """Service class for the apps_authorizedCertificates resource."""

    _NAME = u'apps_authorizedCertificates'

    def __init__(self, client):
      super(AppengineV1alpha.AppsAuthorizedCertificatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Uploads the specified SSL certificate.

      Args:
        request: (AppengineAppsAuthorizedCertificatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizedCertificate) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/authorizedCertificates',
        http_method=u'POST',
        method_id=u'appengine.apps.authorizedCertificates.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha/{+parent}/authorizedCertificates',
        request_field=u'authorizedCertificate',
        request_type_name=u'AppengineAppsAuthorizedCertificatesCreateRequest',
        response_type_name=u'AuthorizedCertificate',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the specified SSL certificate.

      Args:
        request: (AppengineAppsAuthorizedCertificatesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}',
        http_method=u'DELETE',
        method_id=u'appengine.apps.authorizedCertificates.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsAuthorizedCertificatesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the specified SSL certificate.

      Args:
        request: (AppengineAppsAuthorizedCertificatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizedCertificate) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}',
        http_method=u'GET',
        method_id=u'appengine.apps.authorizedCertificates.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'view'],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsAuthorizedCertificatesGetRequest',
        response_type_name=u'AuthorizedCertificate',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all SSL certificates the user is authorized to administer.

      Args:
        request: (AppengineAppsAuthorizedCertificatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAuthorizedCertificatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/authorizedCertificates',
        http_method=u'GET',
        method_id=u'appengine.apps.authorizedCertificates.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+parent}/authorizedCertificates',
        request_field='',
        request_type_name=u'AppengineAppsAuthorizedCertificatesListRequest',
        response_type_name=u'ListAuthorizedCertificatesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated.

      Args:
        request: (AppengineAppsAuthorizedCertificatesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizedCertificate) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}',
        http_method=u'PATCH',
        method_id=u'appengine.apps.authorizedCertificates.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha/{+name}',
        request_field=u'authorizedCertificate',
        request_type_name=u'AppengineAppsAuthorizedCertificatesPatchRequest',
        response_type_name=u'AuthorizedCertificate',
        supports_download=False,
    )

  class AppsAuthorizedDomainsService(base_api.BaseApiService):
    """Service class for the apps_authorizedDomains resource."""

    _NAME = u'apps_authorizedDomains'

    def __init__(self, client):
      super(AppengineV1alpha.AppsAuthorizedDomainsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists all domains the user is authorized to administer.

      Args:
        request: (AppengineAppsAuthorizedDomainsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAuthorizedDomainsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/authorizedDomains',
        http_method=u'GET',
        method_id=u'appengine.apps.authorizedDomains.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+parent}/authorizedDomains',
        request_field='',
        request_type_name=u'AppengineAppsAuthorizedDomainsListRequest',
        response_type_name=u'ListAuthorizedDomainsResponse',
        supports_download=False,
    )

  class AppsDomainMappingsService(base_api.BaseApiService):
    """Service class for the apps_domainMappings resource."""

    _NAME = u'apps_domainMappings'

    def __init__(self, client):
      super(AppengineV1alpha.AppsDomainMappingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains.

      Args:
        request: (AppengineAppsDomainMappingsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/domainMappings',
        http_method=u'POST',
        method_id=u'appengine.apps.domainMappings.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'noManagedCertificate'],
        relative_path=u'v1alpha/{+parent}/domainMappings',
        request_field=u'domainMapping',
        request_type_name=u'AppengineAppsDomainMappingsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource.

      Args:
        request: (AppengineAppsDomainMappingsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/domainMappings/{domainMappingsId}',
        http_method=u'DELETE',
        method_id=u'appengine.apps.domainMappings.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsDomainMappingsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the specified domain mapping.

      Args:
        request: (AppengineAppsDomainMappingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/domainMappings/{domainMappingsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.domainMappings.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsDomainMappingsGetRequest',
        response_type_name=u'DomainMapping',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the domain mappings on an application.

      Args:
        request: (AppengineAppsDomainMappingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDomainMappingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/domainMappings',
        http_method=u'GET',
        method_id=u'appengine.apps.domainMappings.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+parent}/domainMappings',
        request_field='',
        request_type_name=u'AppengineAppsDomainMappingsListRequest',
        response_type_name=u'ListDomainMappingsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource.

      Args:
        request: (AppengineAppsDomainMappingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/domainMappings/{domainMappingsId}',
        http_method=u'PATCH',
        method_id=u'appengine.apps.domainMappings.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'noManagedCertificate', u'updateMask'],
        relative_path=u'v1alpha/{+name}',
        request_field=u'domainMapping',
        request_type_name=u'AppengineAppsDomainMappingsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class AppsLocationsService(base_api.BaseApiService):
    """Service class for the apps_locations resource."""

    _NAME = u'apps_locations'

    def __init__(self, client):
      super(AppengineV1alpha.AppsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Get information about a location.

      Args:
        request: (AppengineAppsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists information about the supported locations for this service.

      Args:
        request: (AppengineAppsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/locations',
        http_method=u'GET',
        method_id=u'appengine.apps.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+name}/locations',
        request_field='',
        request_type_name=u'AppengineAppsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class AppsOperationsService(base_api.BaseApiService):
    """Service class for the apps_operations resource."""

    _NAME = u'apps_operations'

    def __init__(self, client):
      super(AppengineV1alpha.AppsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (AppengineAppsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'appengine.apps.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AppengineAppsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.NOTE: the name binding allows API services to override the binding to use different resource name schemes, such as users/*/operations. To override the binding, API services can add a binding such as "/v1/{name=users/*}/operations" to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (AppengineAppsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/apps/{appsId}/operations',
        http_method=u'GET',
        method_id=u'appengine.apps.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+name}/operations',
        request_field='',
        request_type_name=u'AppengineAppsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class AppsService(base_api.BaseApiService):
    """Service class for the apps resource."""

    _NAME = u'apps'

    def __init__(self, client):
      super(AppengineV1alpha.AppsService, self).__init__(client)
      self._upload_configs = {
          }
