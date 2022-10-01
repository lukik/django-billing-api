"""
Defined API Exceptions. These are exceptions that are thrown in Serializers & Views
"""
__author__ = 'Muchai Noah'

import requests
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from core.api_codes import API_CODE


REQUESTS_EXCEPTIONS = (
    requests.exceptions.Timeout,
    requests.exceptions.ConnectionError,
    requests.exceptions.ConnectTimeout,
    requests.exceptions.HTTPError
)


# Custom Exception Handler
class MaxLoopException(Exception):
    """Raised when a function exceeds a set number of loops"""

    def __init__(self):
        Exception.__init__(self, "function exceeds the set number of loops")


def custom_exception_handler(exc, context):
    """
    This just adds the field "errors" to all exceptions thrown by the API
    """
    # Call REST framework's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    # Update the structure of the response data.
    if response is not None:
        customized_response = {
            'errors': [response.data]
        }
        response.data = customized_response

    return response


# Shared Exceptions

class UnknownError(APIException):
    api_code = API_CODE.UnknownError
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_message = 'Application encountered an error. Please contact us'

    def __init__(self, message, field, status_code=None):
        if status_code: self.status_code = status_code
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class FieldIsRequired(APIException):
    api_code = API_CODE.FieldIsRequired
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _("This field cannot be null")

    def __init__(self, message, field):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class FieldCannotBeNull(APIException):
    api_code = API_CODE.FieldCannotBeNull
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _("This field cannot be null")

    def __init__(self, message, field):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class DateOneMustBeEarlierThanDateTwo(APIException):
    api_code = API_CODE.DateOneMustBeEarlierThanDateTwo
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = ""

    def __init__(self, date_one, date_two):
        self.default_message = f"{date_one} value must be earlier than {date_two} value"
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class DateRangeNotAllowedToOverlap(APIException):
    api_code = API_CODE.DateRangeNotAllowedToOverlap
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _("The provided date range is overlapping.")

    def __init__(self, message):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class DateMustBeWithinGivenRange(APIException):
    api_code = API_CODE.DateMustBeWithinGivenRange
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = ""

    def __init__(self, date_field_to_check, lower_date_range, upper_date_range):
        self.default_message = f"{date_field_to_check} value must be between {lower_date_range} and " \
            f"{upper_date_range} values"
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class InvalidDataValue(APIException):
    api_code = API_CODE.InvalidDataValue
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = "Invalid data value provided"

    def __init__(self, message, field='', extra_info={}):
        if message: self.default_message = message
        if extra_info:
            if field:
                self.detail = {
                    'code': self.api_code,
                    'message': {field: force_str(self.default_message)},
                    'extra_info': extra_info
                }
                return
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class FileNotFound(APIException):
    api_code = API_CODE.FileNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('File not found')

    def __init__(self, message="", field=""):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class FileAlreadyProcessed(APIException):
    api_code = API_CODE.FileAlreadyProcessed
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('File already processed')

    def __init__(self, message="", field=""):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class InvalidFileName(APIException):
    api_code = API_CODE.InvalidFileName
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Invalid File Name')

    def __init__(self, message="", field=""):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class DuplicateRecord(APIException):
    api_code = API_CODE.DuplicateRecord
    status_code = status.HTTP_409_CONFLICT
    default_message = _("Duplicate record found")

    def __init__(self, message, field=""):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class RecordNotFound(APIException):
    api_code = API_CODE.RecordNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _("Record not found")

    def __init__(self, message="", field=""):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class MissingKeyError(APIException):
    """Raised when a dict is missing some mandatory key
    """
    api_code = API_CODE.MissingKeyError
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Missing Key')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class BlankKeyError(APIException):
    """
    Raised when a dict has a key but the value is blank/empty/none
    """
    api_code = API_CODE.BlankKeyError
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Missing Key')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class InvalidKeyError(APIException):
    """
    Raised when a dict has a key that should not be part of the collection
    """
    api_code = API_CODE.InvalidKeyError
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Invalid Key')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class RelatedObjectRequired(APIException):
    """
    A related item is required e.g. A child object
    """
    api_code = API_CODE.RelatedObjectRequired
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Invalid Key')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class EditingNotAllowed(APIException):
    """
    Cannot edit the object or field
    """
    api_code = API_CODE.EditingNotAllowed
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Editing not allowed')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class InvalidParameterValueError(APIException):
    """
    Raised when a dict has a key that should not be part of the collection
    """
    api_code = API_CODE.InvalidParameterValue
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Invalid Parameter Value')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class PermissionDenied(APIException):
    """
    Raised when a dict has a key that should not be part of the collection
    """
    api_code = API_CODE.PermissionDenied
    status_code = status.HTTP_403_FORBIDDEN
    default_message = _('Permission Denied')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class RequiredParameter(APIException):
    """
    Raised when a required URL parameter is not supplied
    """
    api_code = API_CODE.RequiredParameter
    status_code = status.HTTP_403_FORBIDDEN
    default_message = _('Require Parameter')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class DeleteError(APIException):
    """
    Raised when a required URL parameter is not supplied
    """
    api_code = API_CODE.DeleteError
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Require Parameter')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


# Authy Exceptions

class InvalidUserToken(APIException):
    api_code = API_CODE.InvalidUserToken
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('The Token provided is invalid or expired')

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class UserAccountAlreadyExists(APIException):
    api_code = API_CODE.UserAccountAlreadyExists
    status_code = status.HTTP_409_CONFLICT
    default_message = ''

    def __init__(self, message):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class InvalidLoginCredentials(APIException):
    api_code = API_CODE.InvalidLoginCredentials
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = _('Invalid login credentials')

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class MobileNumberDoesNotMatch(APIException):
    """
    Mobile number provided does not match the number on the profile
    """
    api_code = API_CODE.MobileNumberDoesNotMatch
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _("The Mobile Number provided does not match what is on the profile. Please try again")

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class AccountDetailsNotVerified(APIException):
    """
    Raise an exception if Email or Mobile Number is not verified
    """
    api_code = API_CODE.AccountDetailsNotVerified
    status_code = status.HTTP_403_FORBIDDEN
    default_message = _("Verification Required")

    def __init__(self, email_verified, mobile_verified, message=""):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message),
            'email_is_verified': email_verified,
            'mobile_is_verified': mobile_verified
        }


class UserAccountNotActive(APIException):
    api_code = API_CODE.UserAccountNotActive
    status_code = status.HTTP_403_FORBIDDEN
    default_message = _('Your account is not active. Please activate it first by clicking on the button below.')

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class UserNotFound(APIException):
    api_code = API_CODE.UserNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('User not found. Please try again.')

    def __init__(self, message='', field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message),
                'field': force_str(field)
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


# Billing Exceptions

class InvoiceNotFound(APIException):
    api_code = API_CODE.InvoiceNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('Invoice not found')

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class BillNotFound(APIException):
    api_code = API_CODE.BillNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('Bill not found')

    def __init__(self, message, trx_id):
        if message: self.default_message = message
        if trx_id:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message),
                'trx_id': force_str(trx_id)
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class InvoiceAlreadyPaid(APIException):
    api_code = API_CODE.InvoiceAlreadyPaid
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Invoice already paid in part or full')

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class InvoiceAlreadyCancelled(APIException):
    api_code = API_CODE.InvoiceAlreadyCancelled
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Invoice already cancelled')

    def __init__(self, message=''):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


# Finance

class ChartOfAccountNotFound(APIException):
    """Raised when a Preset COA cannot be retrieved"""
    api_code = API_CODE.ChartOfAccountNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('Chart of Account not found')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class UndefinedPresetAccount(APIException):
    """Raised when a Preset COA cannot be retrieved"""
    api_code = API_CODE.UndefinedPresetAccount
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_message = _('Account setup not complete')

    def __init__(self, message):
        if message: self.default_message = message
        self.detail = {
            'code': self.api_code,
            'message': force_str(self.default_message)
        }


class AccountNumberNotFound(APIException):
    api_code = API_CODE.AccountNumberNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('Account Number not found. Has the account been setup by the admin?')

    def __init__(self, message, trx_id):
        if message: self.default_message = message
        if trx_id:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message),
                'trx_id': force_str(trx_id)
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }


class ClientAccountNotFound(APIException):
    api_code = API_CODE.AccountNumberNotFound
    status_code = status.HTTP_404_NOT_FOUND
    default_message = _('Client account not found. Please contact the system administrator')

    def __init__(self, message, field=''):
        if message: self.default_message = message
        if field:
            self.detail = {
                'code': self.api_code,
                'message': {field: force_str(self.default_message)}
            }
        else:
            self.detail = {
                'code': self.api_code,
                'message': force_str(self.default_message)
            }

