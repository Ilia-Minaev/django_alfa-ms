from constants.models import Constants
#import re
from re import sub


class ConstantsMixin:
    def get_constants(self, **kwargs):
        def _get_phone(phone_str):
            if phone_str:
                phone_int = sub(r'(\D)', '', phone_str)
            else:
                return False
            
            try:
                phone_int = int(phone_int)
            except:
                return False
            
            return {'phone_str': phone_str, 'phone_int': phone_int}
        
        context = kwargs
        constants = Constants.objects.get(pk=1)
        context['site_name'] = constants.site_name or False
        context['address'] = constants.address or False
        context['logo'] = constants.logo or False
        context['email'] = constants.email or False
        context['phone1'] = _get_phone(constants.phone1)
        context['phone2'] = _get_phone(constants.phone2)
        context['facebook'] = constants.facebook or False
        context['twitter'] = constants.twitter or False
        context['instagram'] = constants.instagram or False
        context['linkedin'] = constants.linkedin or False
        context['youtube'] = constants.youtube or False
        context['vk'] = constants.vk or False

        return context