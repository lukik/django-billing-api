from django.db.models.signals import post_save
from django.dispatch import receiver
from server.settings import env
from server.settings.components.common import MEDIA_ROOT
from partners.models import PartnerUpload
from partners.partner_import import import_partners


@receiver(post_save, sender=PartnerUpload)
def import_partner_list(sender, instance, created, **kwargs):
    if created:
        file_path = f'{MEDIA_ROOT}/{instance.document.name}'
        params = {
            'user_id': instance.created_by_id,
            'file_upload_id': instance.id,
            'file_path': file_path
        }
        # import_partners(**params)
        import_partners.apply_async(kwargs=params)