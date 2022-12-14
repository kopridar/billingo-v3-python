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

class ModificationDocumentInsert(object):
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
        'due_date': 'date',
        'comment': 'str',
        'payment_method': 'PaymentMethod',
        'without_financial_fulfillment': 'bool',
        'items': 'list[OneOfModificationDocumentInsertItemsItems]'
    }

    attribute_map = {
        'due_date': 'due_date',
        'comment': 'comment',
        'payment_method': 'payment_method',
        'without_financial_fulfillment': 'without_financial_fulfillment',
        'items': 'items'
    }

    def __init__(self, due_date=None, comment=None, payment_method=None, without_financial_fulfillment=False, items=None):  # noqa: E501
        """ModificationDocumentInsert - a model defined in Swagger"""  # noqa: E501
        self._due_date = None
        self._comment = None
        self._payment_method = None
        self._without_financial_fulfillment = None
        self._items = None
        self.discriminator = None
        if due_date is not None:
            self.due_date = due_date
        if comment is not None:
            self.comment = comment
        if payment_method is not None:
            self.payment_method = payment_method
        if without_financial_fulfillment is not None:
            self.without_financial_fulfillment = without_financial_fulfillment
        if items is not None:
            self.items = items

    @property
    def due_date(self):
        """Gets the due_date of this ModificationDocumentInsert.  # noqa: E501


        :return: The due_date of this ModificationDocumentInsert.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this ModificationDocumentInsert.


        :param due_date: The due_date of this ModificationDocumentInsert.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def comment(self):
        """Gets the comment of this ModificationDocumentInsert.  # noqa: E501


        :return: The comment of this ModificationDocumentInsert.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ModificationDocumentInsert.


        :param comment: The comment of this ModificationDocumentInsert.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def payment_method(self):
        """Gets the payment_method of this ModificationDocumentInsert.  # noqa: E501


        :return: The payment_method of this ModificationDocumentInsert.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this ModificationDocumentInsert.


        :param payment_method: The payment_method of this ModificationDocumentInsert.  # noqa: E501
        :type: PaymentMethod
        """

        self._payment_method = payment_method

    @property
    def without_financial_fulfillment(self):
        """Gets the without_financial_fulfillment of this ModificationDocumentInsert.  # noqa: E501


        :return: The without_financial_fulfillment of this ModificationDocumentInsert.  # noqa: E501
        :rtype: bool
        """
        return self._without_financial_fulfillment

    @without_financial_fulfillment.setter
    def without_financial_fulfillment(self, without_financial_fulfillment):
        """Sets the without_financial_fulfillment of this ModificationDocumentInsert.


        :param without_financial_fulfillment: The without_financial_fulfillment of this ModificationDocumentInsert.  # noqa: E501
        :type: bool
        """

        self._without_financial_fulfillment = without_financial_fulfillment

    @property
    def items(self):
        """Gets the items of this ModificationDocumentInsert.  # noqa: E501


        :return: The items of this ModificationDocumentInsert.  # noqa: E501
        :rtype: list[OneOfModificationDocumentInsertItemsItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ModificationDocumentInsert.


        :param items: The items of this ModificationDocumentInsert.  # noqa: E501
        :type: list[OneOfModificationDocumentInsertItemsItems]
        """

        self._items = items

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
        if issubclass(ModificationDocumentInsert, dict):
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
        if not isinstance(other, ModificationDocumentInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
