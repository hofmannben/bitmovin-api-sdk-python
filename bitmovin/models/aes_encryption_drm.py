# coding: utf-8

from bitmovin.models.aes_encryption_method import AesEncryptionMethod
from bitmovin.models.drm import Drm
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class AesEncryptionDrm(Drm):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AesEncryptionDrm, self).openapi_types
        types.update({
            'key': 'str',
            'iv': 'str',
            'key_file_uri': 'str',
            'method': 'AesEncryptionMethod'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AesEncryptionDrm, self).attribute_map
        attributes.update({
            'key': 'key',
            'iv': 'iv',
            'key_file_uri': 'keyFileUri',
            'method': 'method'
        })
        return attributes

    def __init__(self, key=None, iv=None, key_file_uri=None, method=None, *args, **kwargs):
        super(AesEncryptionDrm, self).__init__(*args, **kwargs)

        self._key = None
        self._iv = None
        self._key_file_uri = None
        self._method = None
        self.discriminator = None

        self.key = key
        if iv is not None:
            self.iv = iv
        if key_file_uri is not None:
            self.key_file_uri = key_file_uri
        self.method = method

    @property
    def key(self):
        """Gets the key of this AesEncryptionDrm.

        16 byte Encryption key, 32 hexadecimal characters

        :return: The key of this AesEncryptionDrm.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AesEncryptionDrm.

        16 byte Encryption key, 32 hexadecimal characters

        :param key: The key of this AesEncryptionDrm.
        :type: str
        """

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Invalid type for `key`, type has to be `str`")

            self._key = key


    @property
    def iv(self):
        """Gets the iv of this AesEncryptionDrm.

        16 byte initialization vector

        :return: The iv of this AesEncryptionDrm.
        :rtype: str
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        """Sets the iv of this AesEncryptionDrm.

        16 byte initialization vector

        :param iv: The iv of this AesEncryptionDrm.
        :type: str
        """

        if iv is not None:
            if not isinstance(iv, str):
                raise TypeError("Invalid type for `iv`, type has to be `str`")

            self._iv = iv


    @property
    def key_file_uri(self):
        """Gets the key_file_uri of this AesEncryptionDrm.

        Path relative to the output for referencing in the manifest. If this value is not set the key file will be written automatically to the output folder.

        :return: The key_file_uri of this AesEncryptionDrm.
        :rtype: str
        """
        return self._key_file_uri

    @key_file_uri.setter
    def key_file_uri(self, key_file_uri):
        """Sets the key_file_uri of this AesEncryptionDrm.

        Path relative to the output for referencing in the manifest. If this value is not set the key file will be written automatically to the output folder.

        :param key_file_uri: The key_file_uri of this AesEncryptionDrm.
        :type: str
        """

        if key_file_uri is not None:
            if not isinstance(key_file_uri, str):
                raise TypeError("Invalid type for `key_file_uri`, type has to be `str`")

            self._key_file_uri = key_file_uri


    @property
    def method(self):
        """Gets the method of this AesEncryptionDrm.


        :return: The method of this AesEncryptionDrm.
        :rtype: AesEncryptionMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AesEncryptionDrm.


        :param method: The method of this AesEncryptionDrm.
        :type: AesEncryptionMethod
        """

        if method is not None:
            if not isinstance(method, AesEncryptionMethod):
                raise TypeError("Invalid type for `method`, type has to be `AesEncryptionMethod`")

            self._method = method

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AesEncryptionDrm, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(AesEncryptionDrm, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AesEncryptionDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
