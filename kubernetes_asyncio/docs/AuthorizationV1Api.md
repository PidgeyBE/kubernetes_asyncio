# kubernetes_asyncio.client.AuthorizationV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_local_subject_access_review**](AuthorizationV1Api.md#create_namespaced_local_subject_access_review) | **POST** /apis/authorization.k8s.io/v1/namespaces/{namespace}/localsubjectaccessreviews | 
[**create_self_subject_access_review**](AuthorizationV1Api.md#create_self_subject_access_review) | **POST** /apis/authorization.k8s.io/v1/selfsubjectaccessreviews | 
[**create_self_subject_rules_review**](AuthorizationV1Api.md#create_self_subject_rules_review) | **POST** /apis/authorization.k8s.io/v1/selfsubjectrulesreviews | 
[**create_subject_access_review**](AuthorizationV1Api.md#create_subject_access_review) | **POST** /apis/authorization.k8s.io/v1/subjectaccessreviews | 
[**get_api_resources**](AuthorizationV1Api.md#get_api_resources) | **GET** /apis/authorization.k8s.io/v1/ | 


# **create_namespaced_local_subject_access_review**
> V1LocalSubjectAccessReview create_namespaced_local_subject_access_review(namespace, body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)



create a LocalSubjectAccessReview

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes_asyncio.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes_asyncio.client.AuthorizationV1Api(kubernetes_asyncio.client.ApiClient(configuration))
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes_asyncio.client.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
include_uninitialized = True # bool | If IncludeUninitialized is specified, the object may be returned without completing initialization. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_namespaced_local_subject_access_review(namespace, body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_namespaced_local_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **include_uninitialized** | **bool**| If IncludeUninitialized is specified, the object may be returned without completing initialization. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_self_subject_access_review**
> V1SelfSubjectAccessReview create_self_subject_access_review(body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)



create a SelfSubjectAccessReview

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes_asyncio.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes_asyncio.client.AuthorizationV1Api(kubernetes_asyncio.client.ApiClient(configuration))
body = kubernetes_asyncio.client.V1SelfSubjectAccessReview() # V1SelfSubjectAccessReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
include_uninitialized = True # bool | If IncludeUninitialized is specified, the object may be returned without completing initialization. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_self_subject_access_review(body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_self_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SelfSubjectAccessReview**](V1SelfSubjectAccessReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **include_uninitialized** | **bool**| If IncludeUninitialized is specified, the object may be returned without completing initialization. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SelfSubjectAccessReview**](V1SelfSubjectAccessReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_self_subject_rules_review**
> V1SelfSubjectRulesReview create_self_subject_rules_review(body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)



create a SelfSubjectRulesReview

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes_asyncio.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes_asyncio.client.AuthorizationV1Api(kubernetes_asyncio.client.ApiClient(configuration))
body = kubernetes_asyncio.client.V1SelfSubjectRulesReview() # V1SelfSubjectRulesReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
include_uninitialized = True # bool | If IncludeUninitialized is specified, the object may be returned without completing initialization. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_self_subject_rules_review(body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_self_subject_rules_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SelfSubjectRulesReview**](V1SelfSubjectRulesReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **include_uninitialized** | **bool**| If IncludeUninitialized is specified, the object may be returned without completing initialization. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SelfSubjectRulesReview**](V1SelfSubjectRulesReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subject_access_review**
> V1SubjectAccessReview create_subject_access_review(body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)



create a SubjectAccessReview

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes_asyncio.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes_asyncio.client.AuthorizationV1Api(kubernetes_asyncio.client.ApiClient(configuration))
body = kubernetes_asyncio.client.V1SubjectAccessReview() # V1SubjectAccessReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
include_uninitialized = True # bool | If IncludeUninitialized is specified, the object may be returned without completing initialization. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_subject_access_review(body, dry_run=dry_run, include_uninitialized=include_uninitialized, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SubjectAccessReview**](V1SubjectAccessReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **include_uninitialized** | **bool**| If IncludeUninitialized is specified, the object may be returned without completing initialization. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SubjectAccessReview**](V1SubjectAccessReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> V1APIResourceList get_api_resources()



get available resources

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes_asyncio.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes_asyncio.client.AuthorizationV1Api(kubernetes_asyncio.client.ApiClient(configuration))

try:
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->get_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIResourceList**](V1APIResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

