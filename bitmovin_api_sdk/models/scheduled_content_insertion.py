# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.scheduled_content_insertion_status import ScheduledContentInsertionStatus
import pprint
import six


class ScheduledContentInsertion(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 content_id=None,
                 run_at=None,
                 duration_in_seconds=None,
                 status=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, datetime, float, ScheduledContentInsertionStatus) -> None
        super(ScheduledContentInsertion, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._content_id = None
        self._run_at = None
        self._duration_in_seconds = None
        self._status = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if run_at is not None:
            self.run_at = run_at
        if duration_in_seconds is not None:
            self.duration_in_seconds = duration_in_seconds
        if status is not None:
            self.status = status

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ScheduledContentInsertion, self), 'openapi_types'):
            types = getattr(super(ScheduledContentInsertion, self), 'openapi_types')

        types.update({
            'content_id': 'string_types',
            'run_at': 'datetime',
            'duration_in_seconds': 'float',
            'status': 'ScheduledContentInsertionStatus'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ScheduledContentInsertion, self), 'attribute_map'):
            attributes = getattr(super(ScheduledContentInsertion, self), 'attribute_map')

        attributes.update({
            'content_id': 'contentId',
            'run_at': 'runAt',
            'duration_in_seconds': 'durationInSeconds',
            'status': 'status'
        })
        return attributes

    @property
    def content_id(self):
        # type: () -> string_types
        """Gets the content_id of this ScheduledContentInsertion.

        Id of the insertable content to play instead of the live stream (required)

        :return: The content_id of this ScheduledContentInsertion.
        :rtype: string_types
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        # type: (string_types) -> None
        """Sets the content_id of this ScheduledContentInsertion.

        Id of the insertable content to play instead of the live stream (required)

        :param content_id: The content_id of this ScheduledContentInsertion.
        :type: string_types
        """

        if content_id is not None:
            if not isinstance(content_id, string_types):
                raise TypeError("Invalid type for `content_id`, type has to be `string_types`")

        self._content_id = content_id

    @property
    def run_at(self):
        # type: () -> datetime
        """Gets the run_at of this ScheduledContentInsertion.

        Time to to play the content in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The run_at of this ScheduledContentInsertion.
        :rtype: datetime
        """
        return self._run_at

    @run_at.setter
    def run_at(self, run_at):
        # type: (datetime) -> None
        """Sets the run_at of this ScheduledContentInsertion.

        Time to to play the content in UTC: YYYY-MM-DDThh:mm:ssZ

        :param run_at: The run_at of this ScheduledContentInsertion.
        :type: datetime
        """

        if run_at is not None:
            if not isinstance(run_at, datetime):
                raise TypeError("Invalid type for `run_at`, type has to be `datetime`")

        self._run_at = run_at

    @property
    def duration_in_seconds(self):
        # type: () -> float
        """Gets the duration_in_seconds of this ScheduledContentInsertion.

        Duration for how long to play the content. Cut off if shorter, loop if longer than actual duration.

        :return: The duration_in_seconds of this ScheduledContentInsertion.
        :rtype: float
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds):
        # type: (float) -> None
        """Sets the duration_in_seconds of this ScheduledContentInsertion.

        Duration for how long to play the content. Cut off if shorter, loop if longer than actual duration.

        :param duration_in_seconds: The duration_in_seconds of this ScheduledContentInsertion.
        :type: float
        """

        if duration_in_seconds is not None:
            if not isinstance(duration_in_seconds, (float, int)):
                raise TypeError("Invalid type for `duration_in_seconds`, type has to be `float`")

        self._duration_in_seconds = duration_in_seconds

    @property
    def status(self):
        # type: () -> ScheduledContentInsertionStatus
        """Gets the status of this ScheduledContentInsertion.

        Status of the scheduled content insertion.

        :return: The status of this ScheduledContentInsertion.
        :rtype: ScheduledContentInsertionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (ScheduledContentInsertionStatus) -> None
        """Sets the status of this ScheduledContentInsertion.

        Status of the scheduled content insertion.

        :param status: The status of this ScheduledContentInsertion.
        :type: ScheduledContentInsertionStatus
        """

        if status is not None:
            if not isinstance(status, ScheduledContentInsertionStatus):
                raise TypeError("Invalid type for `status`, type has to be `ScheduledContentInsertionStatus`")

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ScheduledContentInsertion, self), "to_dict"):
            result = super(ScheduledContentInsertion, self).to_dict()
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
        if not isinstance(other, ScheduledContentInsertion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
