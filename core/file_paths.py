from django.conf import settings
from server.settings import env


def get_path_partner_upload_file(instance, filename):
    """
    Location of Upload Files for Partner
    Args:
        instance (object): Model object
        filename (str): Name of file
    """
    file_path = env('PATH_PARTNER_IMPORT_FILE')
    x = get_available_name
    filename, ext = filename.split('.')
    filename = f"{filename}_{instance.import_ref_number}.{ext}"
    return f'{file_path}/setup_files/school_setup/{filename}'

    return f'{settings.PATH_SCHOOL_DOCS}/{filename}'
