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


class V1ContainerImage(object):
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
        'names': 'list[str]',
        'size_bytes': 'int'
    }

    attribute_map = {
        'names': 'names',
        'size_bytes': 'sizeBytes'
    }

    def __init__(self, names=None, size_bytes=None):  # noqa: E501
        """V1ContainerImage - a model defined in OpenAPI"""  # noqa: E501

        self._names = None
        self._size_bytes = None
        self.discriminator = None

        self.names = names
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def names(self):
        """Gets the names of this V1ContainerImage.  # noqa: E501

        Names by which this image is known. e.g. [\"k8s.gcr.io/hyperkube:v1.0.7\", \"dockerhub.io/google_containers/hyperkube:v1.0.7\"]  # noqa: E501

        :return: The names of this V1ContainerImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this V1ContainerImage.

        Names by which this image is known. e.g. [\"k8s.gcr.io/hyperkube:v1.0.7\", \"dockerhub.io/google_containers/hyperkube:v1.0.7\"]  # noqa: E501

        :param names: The names of this V1ContainerImage.  # noqa: E501
        :type: list[str]
        """
        if names is None:
            raise ValueError("Invalid value for `names`, must not be `None`")  # noqa: E501

        self._names = names

    @property
    def size_bytes(self):
        """Gets the size_bytes of this V1ContainerImage.  # noqa: E501

        The size of the image in bytes.  # noqa: E501

        :return: The size_bytes of this V1ContainerImage.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this V1ContainerImage.

        The size of the image in bytes.  # noqa: E501

        :param size_bytes: The size_bytes of this V1ContainerImage.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

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
        if not isinstance(other, V1ContainerImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
