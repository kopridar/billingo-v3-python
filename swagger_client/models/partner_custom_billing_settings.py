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

class PartnerCustomBillingSettings(object):
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
        'payment_method': 'PaymentMethod',
        'document_form': 'DocumentForm',
        'due_days': 'int',
        'document_currency': 'Currency',
        'template_language_code': 'DocumentLanguage',
        'discount': 'Discount'
    }

    attribute_map = {
        'payment_method': 'payment_method',
        'document_form': 'document_form',
        'due_days': 'due_days',
        'document_currency': 'document_currency',
        'template_language_code': 'template_language_code',
        'discount': 'discount'
    }

    def __init__(self, payment_method=None, document_form=None, due_days=None, document_currency=None, template_language_code=None, discount=None):  # noqa: E501
        """PartnerCustomBillingSettings - a model defined in Swagger"""  # noqa: E501
        self._payment_method = None
        self._document_form = None
        self._due_days = None
        self._document_currency = None
        self._template_language_code = None
        self._discount = None
        self.discriminator = None
        if payment_method is not None:
            self.payment_method = payment_method
        if document_form is not None:
            self.document_form = document_form
        if due_days is not None:
            self.due_days = due_days
        if document_currency is not None:
            self.document_currency = document_currency
        if template_language_code is not None:
            self.template_language_code = template_language_code
        if discount is not None:
            self.discount = discount

    @property
    def payment_method(self):
        """Gets the payment_method of this PartnerCustomBillingSettings.  # noqa: E501


        :return: The payment_method of this PartnerCustomBillingSettings.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PartnerCustomBillingSettings.


        :param payment_method: The payment_method of this PartnerCustomBillingSettings.  # noqa: E501
        :type: PaymentMethod
        """

        self._payment_method = payment_method

    @property
    def document_form(self):
        """Gets the document_form of this PartnerCustomBillingSettings.  # noqa: E501


        :return: The document_form of this PartnerCustomBillingSettings.  # noqa: E501
        :rtype: DocumentForm
        """
        return self._document_form

    @document_form.setter
    def document_form(self, document_form):
        """Sets the document_form of this PartnerCustomBillingSettings.


        :param document_form: The document_form of this PartnerCustomBillingSettings.  # noqa: E501
        :type: DocumentForm
        """

        self._document_form = document_form

    @property
    def due_days(self):
        """Gets the due_days of this PartnerCustomBillingSettings.  # noqa: E501


        :return: The due_days of this PartnerCustomBillingSettings.  # noqa: E501
        :rtype: int
        """
        return self._due_days

    @due_days.setter
    def due_days(self, due_days):
        """Sets the due_days of this PartnerCustomBillingSettings.


        :param due_days: The due_days of this PartnerCustomBillingSettings.  # noqa: E501
        :type: int
        """

        self._due_days = due_days

    @property
    def document_currency(self):
        """Gets the document_currency of this PartnerCustomBillingSettings.  # noqa: E501


        :return: The document_currency of this PartnerCustomBillingSettings.  # noqa: E501
        :rtype: Currency
        """
        return self._document_currency

    @document_currency.setter
    def document_currency(self, document_currency):
        """Sets the document_currency of this PartnerCustomBillingSettings.


        :param document_currency: The document_currency of this PartnerCustomBillingSettings.  # noqa: E501
        :type: Currency
        """

        self._document_currency = document_currency

    @property
    def template_language_code(self):
        """Gets the template_language_code of this PartnerCustomBillingSettings.  # noqa: E501


        :return: The template_language_code of this PartnerCustomBillingSettings.  # noqa: E501
        :rtype: DocumentLanguage
        """
        return self._template_language_code

    @template_language_code.setter
    def template_language_code(self, template_language_code):
        """Sets the template_language_code of this PartnerCustomBillingSettings.


        :param template_language_code: The template_language_code of this PartnerCustomBillingSettings.  # noqa: E501
        :type: DocumentLanguage
        """

        self._template_language_code = template_language_code

    @property
    def discount(self):
        """Gets the discount of this PartnerCustomBillingSettings.  # noqa: E501


        :return: The discount of this PartnerCustomBillingSettings.  # noqa: E501
        :rtype: Discount
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this PartnerCustomBillingSettings.


        :param discount: The discount of this PartnerCustomBillingSettings.  # noqa: E501
        :type: Discount
        """

        self._discount = discount

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
        if issubclass(PartnerCustomBillingSettings, dict):
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
        if not isinstance(other, PartnerCustomBillingSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
