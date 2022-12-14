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

class ConversationRate(object):
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
        'from_currency': 'Currency',
        'to_currency': 'Currency',
        'conversation_rate': 'float',
        '_date': 'date'
    }

    attribute_map = {
        'from_currency': 'from_currency',
        'to_currency': 'to_currency',
        'conversation_rate': 'conversation_rate',
        '_date': 'date'
    }

    def __init__(self, from_currency=None, to_currency=None, conversation_rate=None, _date=None):  # noqa: E501
        """ConversationRate - a model defined in Swagger"""  # noqa: E501
        self._from_currency = None
        self._to_currency = None
        self._conversation_rate = None
        self.__date = None
        self.discriminator = None
        if from_currency is not None:
            self.from_currency = from_currency
        if to_currency is not None:
            self.to_currency = to_currency
        if conversation_rate is not None:
            self.conversation_rate = conversation_rate
        if _date is not None:
            self._date = _date

    @property
    def from_currency(self):
        """Gets the from_currency of this ConversationRate.  # noqa: E501


        :return: The from_currency of this ConversationRate.  # noqa: E501
        :rtype: Currency
        """
        return self._from_currency

    @from_currency.setter
    def from_currency(self, from_currency):
        """Sets the from_currency of this ConversationRate.


        :param from_currency: The from_currency of this ConversationRate.  # noqa: E501
        :type: Currency
        """

        self._from_currency = from_currency

    @property
    def to_currency(self):
        """Gets the to_currency of this ConversationRate.  # noqa: E501


        :return: The to_currency of this ConversationRate.  # noqa: E501
        :rtype: Currency
        """
        return self._to_currency

    @to_currency.setter
    def to_currency(self, to_currency):
        """Sets the to_currency of this ConversationRate.


        :param to_currency: The to_currency of this ConversationRate.  # noqa: E501
        :type: Currency
        """

        self._to_currency = to_currency

    @property
    def conversation_rate(self):
        """Gets the conversation_rate of this ConversationRate.  # noqa: E501


        :return: The conversation_rate of this ConversationRate.  # noqa: E501
        :rtype: float
        """
        return self._conversation_rate

    @conversation_rate.setter
    def conversation_rate(self, conversation_rate):
        """Sets the conversation_rate of this ConversationRate.


        :param conversation_rate: The conversation_rate of this ConversationRate.  # noqa: E501
        :type: float
        """

        self._conversation_rate = conversation_rate

    @property
    def _date(self):
        """Gets the _date of this ConversationRate.  # noqa: E501


        :return: The _date of this ConversationRate.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ConversationRate.


        :param _date: The _date of this ConversationRate.  # noqa: E501
        :type: date
        """

        self.__date = _date

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
        if issubclass(ConversationRate, dict):
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
        if not isinstance(other, ConversationRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
