# coding: utf-8

from bitmovin.models.response_status import ResponseStatus
from bitmovin.models.result_wrapper import ResultWrapper
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class ResponseEnvelope(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'request_id': 'str',
            'status': 'ResponseStatus',
            'data': 'ResultWrapper',
            'more': 'object'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'request_id': 'requestId',
            'status': 'status',
            'data': 'data',
            'more': 'more'
        }
        return attributes

    def __init__(self, request_id=None, status=None, data=None, more=None, *args, **kwargs):

        self._request_id = None
        self._status = None
        self._data = None
        self._more = None
        self.discriminator = None

        self.request_id = request_id
        self.status = status
        self.data = data
        if more is not None:
            self.more = more

    @property
    def request_id(self):
        """Gets the request_id of this ResponseEnvelope.

        Unique correlation id

        :return: The request_id of this ResponseEnvelope.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ResponseEnvelope.

        Unique correlation id

        :param request_id: The request_id of this ResponseEnvelope.
        :type: str
        """

        if request_id is not None:
            if not isinstance(request_id, str):
                raise TypeError("Invalid type for `request_id`, type has to be `str`")

            self._request_id = request_id


    @property
    def status(self):
        """Gets the status of this ResponseEnvelope.

        Response status information

        :return: The status of this ResponseEnvelope.
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseEnvelope.

        Response status information

        :param status: The status of this ResponseEnvelope.
        :type: ResponseStatus
        """

        if status is not None:
            if not isinstance(status, ResponseStatus):
                raise TypeError("Invalid type for `status`, type has to be `ResponseStatus`")

            self._status = status


    @property
    def data(self):
        """Gets the data of this ResponseEnvelope.

        Response information

        :return: The data of this ResponseEnvelope.
        :rtype: ResultWrapper
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResponseEnvelope.

        Response information

        :param data: The data of this ResponseEnvelope.
        :type: ResultWrapper
        """

        if data is not None:
            if not isinstance(data, ResultWrapper):
                raise TypeError("Invalid type for `data`, type has to be `ResultWrapper`")

            self._data = data


    @property
    def more(self):
        """Gets the more of this ResponseEnvelope.

        Additional endpoint specific information

        :return: The more of this ResponseEnvelope.
        :rtype: object
        """
        return self._more

    @more.setter
    def more(self, more):
        """Sets the more of this ResponseEnvelope.

        Additional endpoint specific information

        :param more: The more of this ResponseEnvelope.
        :type: object
        """

        if more is not None:
            if not isinstance(more, object):
                raise TypeError("Invalid type for `more`, type has to be `object`")

            self._more = more

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(ResponseEnvelope, dict):
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
        if not isinstance(other, ResponseEnvelope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
