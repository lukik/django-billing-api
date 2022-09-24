from django.utils.translation import gettext_lazy as _
from model_utils import Choices

API_CODE = Choices(

    # 10000 - 10199 | Base Codes | 200
    (5000, 'Success', _("Successful response")),
    (5001, 'UnknownError', _("Unknown Error")),

    # 6200 - 6399 | General Errors | 200
    (6201, 'FieldIsRequired', _('Field is required')),
    (6202, 'FieldCannotBeNull', _('FieldCannotBeNull')),
    (6203, 'DateOneMustBeEarlierThanDateTwo', _('Date One Must Be Earlier Than Date Two')),
    (6204, 'DateRangeNotAllowedToOverlap', _('Date Range Not Allowed To Overlap')),
    (6205, 'DateMustBeWithinGivenRange', _('Date Must Be Within Given Range')),
    (6206, 'InvalidDataValue', _('Invalid data type provided')),
    (6207, 'FileNotFound', _('Invalid data type provided')),
    (6208, 'FileAlreadyProcessed', _('File already processed')),
    (6209, 'DuplicateRecord', _('Duplicate record found')),
    (6210, 'RecordNotFound', _('Record not found')),
    (6211, 'MissingKeyError', _('Missing Key')),
    (6212, 'BlankKeyError', _('Blank Key')),
    (6213, 'InvalidKeyError', _('Invalid Key')),
    (6214, 'RelatedObjectRequired', _('Related Object Required')),
    (6215, 'EditingNotAllowed', _('Editing not allowed')),
    (6216, 'InvalidParameterValue', _('Invalid Parameter Value')),
    (6217, 'PermissionDenied', _('Permission Denied')),
    (6218, 'RequiredParameter', _('Required Parameter')),
    (6219, 'DeleteError', _('Delete Error')),

    # 6400 - 6499 | Requests Errors | 100
    (6401, 'EndPointHTTPError', _("HTTPError occurred")),
    (6402, 'EndPointConnectionError', _("Connection Error. End Point Cannot Be Reached")),
    (6403, 'EndPointTimeout', _("Connection timed out")),
    (6404, 'EndPointRequestsException', _("Requests Exception")),

    # 6500 - 6699 | User Account related
    (6501, 'UserNotFound', _('User Not Found')),
    (6502, 'UserAccountAlreadyExists', _('User Account Already Exists')),
    (6503, 'InvalidLoginCredentials', _('Invalid Login Credentials')),
    (6504, 'MobileNumberDoesNotMatch', _('Mobile Number Does Not Match')),
    (6505, 'AccountDetailsNotVerified', _('Account Details Not Verified')),
    (6506, 'UserAccountNotActive', _('User Account Not Active')),
    (6507, 'InvalidUserToken', _('Invalid User Token')),

    # 7400 - 7499 | Finance | 100
    (7401, 'AccountNumberNotFound', _('Invalid Account Number')),
    (7402, 'UndefinedPresetAccount', _('Undefined Preset Account')),
    (7403, 'ChartOfAccountNotFound', _('Chart of Account not found')),

    # 7500 - 7599 | Billing | 100
    (7501, 'InvoiceNotFound', _('Invoice Not Found')),
    (7502, 'BillNotFound', _('Bill Not Found')),
    (7503, 'InvoiceAlreadyCancelled', _('Invoice Already Cancelled')),
    (7504, 'InvoiceAlreadyPaid', _('Invoice already paid in full or part')),
    (7505, 'NoUnbilledItems', _('Partner does not have any un-billed items')),

)
