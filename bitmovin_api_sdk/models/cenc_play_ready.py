# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CencPlayReady(object):
    @poscheck_model
    def __init__(self,
                 la_url=None,
                 pssh=None):
        # type: (string_types, string_types) -> None

        self._la_url = None
        self._pssh = None
        self.discriminator = None

        if la_url is not None:
            self.la_url = la_url
        if pssh is not None:
            self.pssh = pssh

    @property
    def openapi_types(self):
        types = {
            'la_url': 'string_types',
            'pssh': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'la_url': 'laUrl',
            'pssh': 'pssh'
        }
        return attributes

    @property
    def la_url(self):
        # type: () -> string_types
        """Gets the la_url of this CencPlayReady.

        Url of the license server. Either the laUrl or the pssh needs to be provided.

        :return: The la_url of this CencPlayReady.
        :rtype: string_types
        """
        return self._la_url

    @la_url.setter
    def la_url(self, la_url):
        # type: (string_types) -> None
        """Sets the la_url of this CencPlayReady.

        Url of the license server. Either the laUrl or the pssh needs to be provided.

        :param la_url: The la_url of this CencPlayReady.
        :type: string_types
        """

        if la_url is not None:
            if not isinstance(la_url, string_types):
                raise TypeError("Invalid type for `la_url`, type has to be `string_types`")

        self._la_url = la_url

    @property
    def pssh(self):
        # type: () -> string_types
        """Gets the pssh of this CencPlayReady.

        Base64 encoded pssh payload.

        :return: The pssh of this CencPlayReady.
        :rtype: string_types
        """
        return self._pssh

    @pssh.setter
    def pssh(self, pssh):
        # type: (string_types) -> None
        """Sets the pssh of this CencPlayReady.

        Base64 encoded pssh payload.

        :param pssh: The pssh of this CencPlayReady.
        :type: string_types
        """

        if pssh is not None:
            if not isinstance(pssh, string_types):
                raise TypeError("Invalid type for `pssh`, type has to be `string_types`")

        self._pssh = pssh

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CencPlayReady):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
