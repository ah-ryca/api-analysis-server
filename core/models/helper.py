from django.db import models

from django.utils.translation import gettext_lazy as _


class DEVICE_TYPE(models.IntegerChoices):
    IS_MOBILE = 1, _('موبایل')
    IS_TABLET = 2, _('تبلت')
    IS_PC = 3, _('کامپیوتر')
    IS_TOUCH_CAPABLE = 4, _('لمسی')
    IS_BOT = 5, _('بات')
    OTHER = 6, _('نامشخص')
