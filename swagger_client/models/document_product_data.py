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

class DocumentProductData(object):
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
        'name': 'str',
        'unit_price': 'float',
        'unit_price_type': 'UnitPriceType',
        'quantity': 'float',
        'unit': 'str',
        'vat': 'Vat',
        'comment': 'str',
        'entitlement': 'Entitlement'
    }

    attribute_map = {
        'name': 'name',
        'unit_price': 'unit_price',
        'unit_price_type': 'unit_price_type',
        'quantity': 'quantity',
        'unit': 'unit',
        'vat': 'vat',
        'comment': 'comment',
        'entitlement': 'entitlement'
    }

    def __init__(self, name=None, unit_price=None, unit_price_type=None, quantity=None, unit=None, vat=None, comment=None, entitlement=None):  # noqa: E501
        """DocumentProductData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._unit_price = None
        self._unit_price_type = None
        self._quantity = None
        self._unit = None
        self._vat = None
        self._comment = None
        self._entitlement = None
        self.discriminator = None
        self.name = name
        self.unit_price = unit_price
        self.unit_price_type = unit_price_type
        self.quantity = quantity
        self.unit = unit
        self.vat = vat
        if comment is not None:
            self.comment = comment
        if entitlement is not None:
            self.entitlement = entitlement

    @property
    def name(self):
        """Gets the name of this DocumentProductData.  # noqa: E501


        :return: The name of this DocumentProductData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentProductData.


        :param name: The name of this DocumentProductData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unit_price(self):
        """Gets the unit_price of this DocumentProductData.  # noqa: E501


        :return: The unit_price of this DocumentProductData.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this DocumentProductData.


        :param unit_price: The unit_price of this DocumentProductData.  # noqa: E501
        :type: float
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def unit_price_type(self):
        """Gets the unit_price_type of this DocumentProductData.  # noqa: E501


        :return: The unit_price_type of this DocumentProductData.  # noqa: E501
        :rtype: UnitPriceType
        """
        return self._unit_price_type

    @unit_price_type.setter
    def unit_price_type(self, unit_price_type):
        """Sets the unit_price_type of this DocumentProductData.


        :param unit_price_type: The unit_price_type of this DocumentProductData.  # noqa: E501
        :type: UnitPriceType
        """
        if unit_price_type is None:
            raise ValueError("Invalid value for `unit_price_type`, must not be `None`")  # noqa: E501

        self._unit_price_type = unit_price_type

    @property
    def quantity(self):
        """Gets the quantity of this DocumentProductData.  # noqa: E501


        :return: The quantity of this DocumentProductData.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DocumentProductData.


        :param quantity: The quantity of this DocumentProductData.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def unit(self):
        """Gets the unit of this DocumentProductData.  # noqa: E501


        :return: The unit of this DocumentProductData.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DocumentProductData.


        :param unit: The unit of this DocumentProductData.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def vat(self):
        """Gets the vat of this DocumentProductData.  # noqa: E501


        :return: The vat of this DocumentProductData.  # noqa: E501
        :rtype: Vat
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this DocumentProductData.


        :param vat: The vat of this DocumentProductData.  # noqa: E501
        :type: Vat
        """
        if vat is None:
            raise ValueError("Invalid value for `vat`, must not be `None`")  # noqa: E501

        self._vat = vat

    @property
    def comment(self):
        """Gets the comment of this DocumentProductData.  # noqa: E501


        :return: The comment of this DocumentProductData.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DocumentProductData.


        :param comment: The comment of this DocumentProductData.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def entitlement(self):
        """Gets the entitlement of this DocumentProductData.  # noqa: E501


        :return: The entitlement of this DocumentProductData.  # noqa: E501
        :rtype: Entitlement
        """
        return self._entitlement

    @entitlement.setter
    def entitlement(self, entitlement):
        """Sets the entitlement of this DocumentProductData.


        :param entitlement: The entitlement of this DocumentProductData.  # noqa: E501
        :type: Entitlement
        """

        self._entitlement = entitlement

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
        if issubclass(DocumentProductData, dict):
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
        if not isinstance(other, DocumentProductData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
