import re
import codecs
import csv
from django.db import IntegrityError
from server.taskapp.celery import app
from partners.models import Partner, PartnerUpload


@app.task(name="partners.partner_import.import_partners")
def import_partners(**kwargs):
    """
    Script to import list of partners
    """
    has_error = False
    with codecs.open(kwargs['file_path'], encoding='utf-8', errors='ignore') as source_file:
        partner_file = csv.reader(source_file, quotechar='"', delimiter='|', skipinitialspace=True)
        partner_list = []
        for index, row in enumerate(partner_file):
            if index == 0:
                continue

            created_by_id = kwargs['user_id']
            file_upload_id = kwargs['file_upload_id']
            title = row[0]
            notes = row[1]
            is_client = row[2]
            is_supplier = row[3]
            if is_client == "Y":
                is_client = True
            else:
                is_client = False
            if is_supplier == "Y":
                is_supplier = True
            else:
                is_supplier = False
            partner_list.append(Partner.create_new(
                created_by_id, title, notes, is_client, is_supplier, True
            ))

        if partner_list:
            # Insert all records into Partner Table
            try:
                Partner.objects.bulk_create(partner_list)
                import_msg = "File imported successfully"
            except IntegrityError:
                has_error = True
                import_msg = "Could not import list. Partner Name conflict"
            except:
                has_error = True
                import_msg = "Could not import list. Please try again or contact admin"

        # Get file that was uploaded and set status message
        partner_upload = PartnerUpload.objects.get(id=file_upload_id)
        if has_error:
            # Means there was an error importing the file
            partner_upload.imported_successfully = False
        else:
            partner_upload.imported_successfully = True

        partner_upload.import_summary = import_msg
        partner_upload.save()

        return import_msg
