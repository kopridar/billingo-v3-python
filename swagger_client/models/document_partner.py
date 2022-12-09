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

class DocumentPartner(object):
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
        'id': 'int',
        'name': 'str',
        'address': 'Address',
        'emails': 'list[str]',
        'taxcode': 'str',
        'iban': 'str',
        'swift': 'str',
        'account_number': 'str',
        'phone': 'str',
        'tax_type': 'PartnerTaxType'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'emails': 'emails',
        'taxcode': 'taxcode',
        'iban': 'iban',
        'swift': 'swift',
        'account_number': 'account_number',
        'phone': 'phone',
        'tax_type': 'tax_type'
    }

    def __init__(self, id=None, name=None, address=None, emails=None, taxcode=None, iban=None, swift=None, account_number=None, phone=None, tax_type=None):  # noqa: E501
        """DocumentPartner - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._address = None
        self._emails = None
        self._taxcode = None
        self._iban = None
        self._swift = None
        self._account_number = None
        self._phone = None
        self._tax_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if emails is not None:
            self.emails = emails
        if taxcode is not None:
            self.taxcode = taxcode
        if iban is not None:
            self.iban = iban
        if swift is not None:
            self.swift = swift
        if account_number is not None:
            self.account_number = account_number
        if phone is not None:
            self.phone = phone
        if tax_type is not None:
            self.tax_type = tax_type

    @property
    def id(self):
        """Gets the id of this DocumentPartner.  # noqa: E501


        :return: The id of this DocumentPartner.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentPartner.


        :param id: The id of this DocumentPartner.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DocumentPartner.  # noqa: E501


        :return: The name of this DocumentPartner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentPartner.


        :param name: The name of this DocumentPartner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this DocumentPartner.  # noqa: E501


        :return: The address of this DocumentPartner.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DocumentPartner.


        :param address: The address of this DocumentPartner.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def emails(self):
        """Gets the emails of this DocumentPartner.  # noqa: E501


        :return: The emails of this DocumentPartner.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this DocumentPartner.


        :param emails: The emails of this DocumentPartner.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def taxcode(self):
        """Gets the taxcode of this DocumentPartner.  # noqa: E501


        :return: The taxcode of this DocumentPartner.  # noqa: E501
        :rtype: str
        """
        return self._taxcode

    @taxcode.setter
    def taxcode(self, taxcode):
        """Sets the taxcode of this DocumentPartner.


        :param taxcode: The taxcode of this DocumentPartner.  # noqa: E501
        :type: str
        """

        self._taxcode = taxcode

    @property
    def iban(self):
        """Gets the iban of this DocumentPartner.  # noqa: E501


        :return: The iban of this DocumentPartner.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this DocumentPartner.


        :param iban: The iban of this DocumentPartner.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def swift(self):
        """Gets the swift of this DocumentPartner.  # noqa: E501


        :return: The swift of this DocumentPartner.  # noqa: E501
        :rtype: str
        """
        return self._swift

    @swift.setter
    def swift(self, swift):
        """Sets the swift of this DocumentPartner.


        :param swift: The swift of this DocumentPartner.  # noqa: E501
        :type: str
        """

        self._swift = swift

    @property
    def account_number(self):
        """Gets the account_number of this DocumentPartner.  # noqa: E501


        :return: The account_number of this DocumentPartner.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this DocumentPartner.


        :param account_number: The account_number of this DocumentPartner.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def phone(self):
        """Gets the phone of this DocumentPartner.  # noqa: E501


        :return: The phone of this DocumentPartner.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this DocumentPartner.


        :param phone: The phone of this DocumentPartner.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def tax_type(self):
        """Gets the tax_type of this DocumentPartner.  # noqa: E501


        :return: The tax_type of this DocumentPartner.  # noqa: E501
        :rtype: PartnerTaxType
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this DocumentPartner.


        :param tax_type: The tax_type of this DocumentPartner.  # noqa: E501
        :type: PartnerTaxType
        """

        self._tax_type = tax_type

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
        if issubclass(DocumentPartner, dict):
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
        if not isinstance(other, DocumentPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
