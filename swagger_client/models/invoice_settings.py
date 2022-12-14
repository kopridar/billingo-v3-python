# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.  # noqa: E501

    OpenAPI spec version: 3.0.14
    Contact: hello@billingo.hu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvoiceSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_type': 'DocumentType',
        'fulfillment_date': 'date',
        'due_date': 'date',
        'document_format': 'DocumentFormat',
        'comment': 'str'
    }

    attribute_map = {
        'document_type': 'document_type',
        'fulfillment_date': 'fulfillment_date',
        'due_date': 'due_date',
        'document_format': 'document_format',
        'comment': 'comment'
    }

    def __init__(self, document_type=None, fulfillment_date=None, due_date=None, document_format=None, comment=None):  # noqa: E501
        """InvoiceSettings - a model defined in Swagger"""  # noqa: E501
        self._document_type = None
        self._fulfillment_date = None
        self._due_date = None
        self._document_format = None
        self._comment = None
        self.discriminator = None
        if document_type is not None:
            self.document_type = document_type
        if fulfillment_date is not None:
            self.fulfillment_date = fulfillment_date
        if due_date is not None:
            self.due_date = due_date
        if document_format is not None:
            self.document_format = document_format
        if comment is not None:
            self.comment = comment

    @property
    def document_type(self):
        """Gets the document_type of this InvoiceSettings.  # noqa: E501


        :return: The document_type of this InvoiceSettings.  # noqa: E501
        :rtype: DocumentType
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this InvoiceSettings.


        :param document_type: The document_type of this InvoiceSettings.  # noqa: E501
        :type: DocumentType
        """

        self._document_type = document_type

    @property
    def fulfillment_date(self):
        """Gets the fulfillment_date of this InvoiceSettings.  # noqa: E501


        :return: The fulfillment_date of this InvoiceSettings.  # noqa: E501
        :rtype: date
        """
        return self._fulfillment_date

    @fulfillment_date.setter
    def fulfillment_date(self, fulfillment_date):
        """Sets the fulfillment_date of this InvoiceSettings.


        :param fulfillment_date: The fulfillment_date of this InvoiceSettings.  # noqa: E501
        :type: date
        """

        self._fulfillment_date = fulfillment_date

    @property
    def due_date(self):
        """Gets the due_date of this InvoiceSettings.  # noqa: E501


        :return: The due_date of this InvoiceSettings.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this InvoiceSettings.


        :param due_date: The due_date of this InvoiceSettings.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def document_format(self):
        """Gets the document_format of this InvoiceSettings.  # noqa: E501


        :return: The document_format of this InvoiceSettings.  # noqa: E501
        :rtype: DocumentFormat
        """
        return self._document_format

    @document_format.setter
    def document_format(self, document_format):
        """Sets the document_format of this InvoiceSettings.


        :param document_format: The document_format of this InvoiceSettings.  # noqa: E501
        :type: DocumentFormat
        """

        self._document_format = document_format

    @property
    def comment(self):
        """Gets the comment of this InvoiceSettings.  # noqa: E501


        :return: The comment of this InvoiceSettings.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this InvoiceSettings.


        :param comment: The comment of this InvoiceSettings.  # noqa: E501
        :type: str
        """

        self._comment = comment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InvoiceSettings, dict):
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
        if not isinstance(other, InvoiceSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
