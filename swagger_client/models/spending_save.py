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

class SpendingSave(object):
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
        'currency': 'Currency',
        'conversion_rate': 'float',
        'total_gross': 'float',
        'total_gross_huf': 'float',
        'total_vat_amount': 'float',
        'total_vat_amount_huf': 'float',
        'fulfillment_date': 'date',
        'paid_at': 'date',
        'category': 'Category',
        'comment': 'str',
        'invoice_number': 'str',
        'invoice_date': 'date',
        'due_date': 'date',
        'payment_method': 'SpendingPaymentMethod',
        'partner_id': 'int'
    }

    attribute_map = {
        'currency': 'currency',
        'conversion_rate': 'conversion_rate',
        'total_gross': 'total_gross',
        'total_gross_huf': 'total_gross_huf',
        'total_vat_amount': 'total_vat_amount',
        'total_vat_amount_huf': 'total_vat_amount_huf',
        'fulfillment_date': 'fulfillment_date',
        'paid_at': 'paid_at',
        'category': 'category',
        'comment': 'comment',
        'invoice_number': 'invoice_number',
        'invoice_date': 'invoice_date',
        'due_date': 'due_date',
        'payment_method': 'payment_method',
        'partner_id': 'partner_id'
    }

    def __init__(self, currency=None, conversion_rate=None, total_gross=None, total_gross_huf=None, total_vat_amount=None, total_vat_amount_huf=None, fulfillment_date=None, paid_at=None, category=None, comment=None, invoice_number=None, invoice_date=None, due_date=None, payment_method=None, partner_id=None):  # noqa: E501
        """SpendingSave - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._conversion_rate = None
        self._total_gross = None
        self._total_gross_huf = None
        self._total_vat_amount = None
        self._total_vat_amount_huf = None
        self._fulfillment_date = None
        self._paid_at = None
        self._category = None
        self._comment = None
        self._invoice_number = None
        self._invoice_date = None
        self._due_date = None
        self._payment_method = None
        self._partner_id = None
        self.discriminator = None
        self.currency = currency
        if conversion_rate is not None:
            self.conversion_rate = conversion_rate
        self.total_gross = total_gross
        self.total_gross_huf = total_gross_huf
        self.total_vat_amount = total_vat_amount
        self.total_vat_amount_huf = total_vat_amount_huf
        self.fulfillment_date = fulfillment_date
        if paid_at is not None:
            self.paid_at = paid_at
        self.category = category
        if comment is not None:
            self.comment = comment
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if due_date is not None:
            self.due_date = due_date
        self.payment_method = payment_method
        if partner_id is not None:
            self.partner_id = partner_id

    @property
    def currency(self):
        """Gets the currency of this SpendingSave.  # noqa: E501


        :return: The currency of this SpendingSave.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SpendingSave.


        :param currency: The currency of this SpendingSave.  # noqa: E501
        :type: Currency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def conversion_rate(self):
        """Gets the conversion_rate of this SpendingSave.  # noqa: E501


        :return: The conversion_rate of this SpendingSave.  # noqa: E501
        :rtype: float
        """
        return self._conversion_rate

    @conversion_rate.setter
    def conversion_rate(self, conversion_rate):
        """Sets the conversion_rate of this SpendingSave.


        :param conversion_rate: The conversion_rate of this SpendingSave.  # noqa: E501
        :type: float
        """

        self._conversion_rate = conversion_rate

    @property
    def total_gross(self):
        """Gets the total_gross of this SpendingSave.  # noqa: E501


        :return: The total_gross of this SpendingSave.  # noqa: E501
        :rtype: float
        """
        return self._total_gross

    @total_gross.setter
    def total_gross(self, total_gross):
        """Sets the total_gross of this SpendingSave.


        :param total_gross: The total_gross of this SpendingSave.  # noqa: E501
        :type: float
        """
        if total_gross is None:
            raise ValueError("Invalid value for `total_gross`, must not be `None`")  # noqa: E501

        self._total_gross = total_gross

    @property
    def total_gross_huf(self):
        """Gets the total_gross_huf of this SpendingSave.  # noqa: E501


        :return: The total_gross_huf of this SpendingSave.  # noqa: E501
        :rtype: float
        """
        return self._total_gross_huf

    @total_gross_huf.setter
    def total_gross_huf(self, total_gross_huf):
        """Sets the total_gross_huf of this SpendingSave.


        :param total_gross_huf: The total_gross_huf of this SpendingSave.  # noqa: E501
        :type: float
        """
        if total_gross_huf is None:
            raise ValueError("Invalid value for `total_gross_huf`, must not be `None`")  # noqa: E501

        self._total_gross_huf = total_gross_huf

    @property
    def total_vat_amount(self):
        """Gets the total_vat_amount of this SpendingSave.  # noqa: E501


        :return: The total_vat_amount of this SpendingSave.  # noqa: E501
        :rtype: float
        """
        return self._total_vat_amount

    @total_vat_amount.setter
    def total_vat_amount(self, total_vat_amount):
        """Sets the total_vat_amount of this SpendingSave.


        :param total_vat_amount: The total_vat_amount of this SpendingSave.  # noqa: E501
        :type: float
        """
        if total_vat_amount is None:
            raise ValueError("Invalid value for `total_vat_amount`, must not be `None`")  # noqa: E501

        self._total_vat_amount = total_vat_amount

    @property
    def total_vat_amount_huf(self):
        """Gets the total_vat_amount_huf of this SpendingSave.  # noqa: E501


        :return: The total_vat_amount_huf of this SpendingSave.  # noqa: E501
        :rtype: float
        """
        return self._total_vat_amount_huf

    @total_vat_amount_huf.setter
    def total_vat_amount_huf(self, total_vat_amount_huf):
        """Sets the total_vat_amount_huf of this SpendingSave.


        :param total_vat_amount_huf: The total_vat_amount_huf of this SpendingSave.  # noqa: E501
        :type: float
        """
        if total_vat_amount_huf is None:
            raise ValueError("Invalid value for `total_vat_amount_huf`, must not be `None`")  # noqa: E501

        self._total_vat_amount_huf = total_vat_amount_huf

    @property
    def fulfillment_date(self):
        """Gets the fulfillment_date of this SpendingSave.  # noqa: E501


        :return: The fulfillment_date of this SpendingSave.  # noqa: E501
        :rtype: date
        """
        return self._fulfillment_date

    @fulfillment_date.setter
    def fulfillment_date(self, fulfillment_date):
        """Sets the fulfillment_date of this SpendingSave.


        :param fulfillment_date: The fulfillment_date of this SpendingSave.  # noqa: E501
        :type: date
        """
        if fulfillment_date is None:
            raise ValueError("Invalid value for `fulfillment_date`, must not be `None`")  # noqa: E501

        self._fulfillment_date = fulfillment_date

    @property
    def paid_at(self):
        """Gets the paid_at of this SpendingSave.  # noqa: E501


        :return: The paid_at of this SpendingSave.  # noqa: E501
        :rtype: date
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at):
        """Sets the paid_at of this SpendingSave.


        :param paid_at: The paid_at of this SpendingSave.  # noqa: E501
        :type: date
        """

        self._paid_at = paid_at

    @property
    def category(self):
        """Gets the category of this SpendingSave.  # noqa: E501


        :return: The category of this SpendingSave.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SpendingSave.


        :param category: The category of this SpendingSave.  # noqa: E501
        :type: Category
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def comment(self):
        """Gets the comment of this SpendingSave.  # noqa: E501


        :return: The comment of this SpendingSave.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SpendingSave.


        :param comment: The comment of this SpendingSave.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def invoice_number(self):
        """Gets the invoice_number of this SpendingSave.  # noqa: E501


        :return: The invoice_number of this SpendingSave.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this SpendingSave.


        :param invoice_number: The invoice_number of this SpendingSave.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def invoice_date(self):
        """Gets the invoice_date of this SpendingSave.  # noqa: E501


        :return: The invoice_date of this SpendingSave.  # noqa: E501
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this SpendingSave.


        :param invoice_date: The invoice_date of this SpendingSave.  # noqa: E501
        :type: date
        """

        self._invoice_date = invoice_date

    @property
    def due_date(self):
        """Gets the due_date of this SpendingSave.  # noqa: E501


        :return: The due_date of this SpendingSave.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this SpendingSave.


        :param due_date: The due_date of this SpendingSave.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def payment_method(self):
        """Gets the payment_method of this SpendingSave.  # noqa: E501


        :return: The payment_method of this SpendingSave.  # noqa: E501
        :rtype: SpendingPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this SpendingSave.


        :param payment_method: The payment_method of this SpendingSave.  # noqa: E501
        :type: SpendingPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def partner_id(self):
        """Gets the partner_id of this SpendingSave.  # noqa: E501


        :return: The partner_id of this SpendingSave.  # noqa: E501
        :rtype: int
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        """Sets the partner_id of this SpendingSave.


        :param partner_id: The partner_id of this SpendingSave.  # noqa: E501
        :type: int
        """

        self._partner_id = partner_id

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
        if issubclass(SpendingSave, dict):
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
        if not isinstance(other, SpendingSave):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other