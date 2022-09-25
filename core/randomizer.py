__author__ = 'Muchai Noah'

import random
from model_utils import Choices
from django.utils.translation import gettext_lazy as _

RANDOM = Choices(
    (1, 'PartnerAccountNumber', _('Partner Account Number')),
)

CHAR_SET_NUMBERS = "1234567890"
CHAR_SET_STRINGS = "123456789ABCDEFGHJKMNPQRSTUVWXYZ"  # Have skipped I and O for readability


def generate_random(random_type, length):
    """
    Create a random number of characters
    Args:
        random_type(int): Type of reference required
        length (int): Length of the generated code
    Returns:
         random_value(str): on success or False on failure
    """
    try:
        if random_type in [RANDOM.PartnerAccountNumber]:

            return generate_random_code(CHAR_SET_NUMBERS, length)

        elif random_type in [RANDOM.UserInputCode, RANDOM.MessageCode, RANDOM.AssignmentCode]:

            # Generate a human-readable code avoiding numbers 0, letters O, I & L
            return generate_random_code(CHAR_SET_STRINGS, length)

        else:

            print("random_type: ", random_type)
            raise ValueError("Could not find {0} in {1} Enum".format(random_type,"RANDOM_TYPE"))

    except ValueError:
        ValueError(f"Could not find {random_type} in RANDOM Choices")


def generate_random_code(char_set, length):
    """
    Generate a random code
    Args:
        char_set (str):
        max_length (int): Maximum length of the code to be generated
    Returns:
        code (str)
    """
    while True:
        chosen = ''
        chosen1 = ''
        code_length = 0
        while code_length < length / 2:
            chosen = f'{chosen}{str(random.choice(char_set))}'
            chosen1 = f'{chosen1}{str(random.choice(char_set))}'
            code_length += 1
            if str(chosen)[:1] == "0":  # Cannot start with a zero
                code_length = 0
                chosen = ''
                chosen1 = ''
        # print("RANDOM CODE: ", f"{chosen}{chosen1}")
        return f"{chosen}{chosen1}"
        # return code




