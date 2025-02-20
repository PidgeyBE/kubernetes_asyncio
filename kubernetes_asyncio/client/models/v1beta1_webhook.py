# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.13.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1beta1Webhook(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'client_config': 'AdmissionregistrationV1beta1WebhookClientConfig',
        'failure_policy': 'str',
        'name': 'str',
        'namespace_selector': 'V1LabelSelector',
        'rules': 'list[V1beta1RuleWithOperations]',
        'side_effects': 'str'
    }

    attribute_map = {
        'client_config': 'clientConfig',
        'failure_policy': 'failurePolicy',
        'name': 'name',
        'namespace_selector': 'namespaceSelector',
        'rules': 'rules',
        'side_effects': 'sideEffects'
    }

    def __init__(self, client_config=None, failure_policy=None, name=None, namespace_selector=None, rules=None, side_effects=None):  # noqa: E501
        """V1beta1Webhook - a model defined in OpenAPI"""  # noqa: E501

        self._client_config = None
        self._failure_policy = None
        self._name = None
        self._namespace_selector = None
        self._rules = None
        self._side_effects = None
        self.discriminator = None

        self.client_config = client_config
        if failure_policy is not None:
            self.failure_policy = failure_policy
        self.name = name
        if namespace_selector is not None:
            self.namespace_selector = namespace_selector
        if rules is not None:
            self.rules = rules
        if side_effects is not None:
            self.side_effects = side_effects

    @property
    def client_config(self):
        """Gets the client_config of this V1beta1Webhook.  # noqa: E501


        :return: The client_config of this V1beta1Webhook.  # noqa: E501
        :rtype: AdmissionregistrationV1beta1WebhookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """Sets the client_config of this V1beta1Webhook.


        :param client_config: The client_config of this V1beta1Webhook.  # noqa: E501
        :type: AdmissionregistrationV1beta1WebhookClientConfig
        """
        if client_config is None:
            raise ValueError("Invalid value for `client_config`, must not be `None`")  # noqa: E501

        self._client_config = client_config

    @property
    def failure_policy(self):
        """Gets the failure_policy of this V1beta1Webhook.  # noqa: E501

        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.  # noqa: E501

        :return: The failure_policy of this V1beta1Webhook.  # noqa: E501
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """Sets the failure_policy of this V1beta1Webhook.

        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.  # noqa: E501

        :param failure_policy: The failure_policy of this V1beta1Webhook.  # noqa: E501
        :type: str
        """

        self._failure_policy = failure_policy

    @property
    def name(self):
        """Gets the name of this V1beta1Webhook.  # noqa: E501

        The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.  # noqa: E501

        :return: The name of this V1beta1Webhook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1Webhook.

        The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.  # noqa: E501

        :param name: The name of this V1beta1Webhook.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace_selector(self):
        """Gets the namespace_selector of this V1beta1Webhook.  # noqa: E501


        :return: The namespace_selector of this V1beta1Webhook.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """Sets the namespace_selector of this V1beta1Webhook.


        :param namespace_selector: The namespace_selector of this V1beta1Webhook.  # noqa: E501
        :type: V1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def rules(self):
        """Gets the rules of this V1beta1Webhook.  # noqa: E501

        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.  # noqa: E501

        :return: The rules of this V1beta1Webhook.  # noqa: E501
        :rtype: list[V1beta1RuleWithOperations]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this V1beta1Webhook.

        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.  # noqa: E501

        :param rules: The rules of this V1beta1Webhook.  # noqa: E501
        :type: list[V1beta1RuleWithOperations]
        """

        self._rules = rules

    @property
    def side_effects(self):
        """Gets the side_effects of this V1beta1Webhook.  # noqa: E501

        SideEffects states whether this webhookk has side effects. Acceptable values are: Unknown, None, Some, NoneOnDryRun Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission change and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Defaults to Unknown.  # noqa: E501

        :return: The side_effects of this V1beta1Webhook.  # noqa: E501
        :rtype: str
        """
        return self._side_effects

    @side_effects.setter
    def side_effects(self, side_effects):
        """Sets the side_effects of this V1beta1Webhook.

        SideEffects states whether this webhookk has side effects. Acceptable values are: Unknown, None, Some, NoneOnDryRun Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission change and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Defaults to Unknown.  # noqa: E501

        :param side_effects: The side_effects of this V1beta1Webhook.  # noqa: E501
        :type: str
        """

        self._side_effects = side_effects

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
