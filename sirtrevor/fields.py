# vim:fileencoding=utf-8
from django.db import models
from django.utils.six import text_type
from django.utils.translation import ugettext_lazy as _
from . import SirTrevorContent
from .forms import SirTrevorFormField


class SirTrevorField(models.Field):
    description = _("TODO")

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, **kwargs):
        defaults = {
            'form_class': SirTrevorFormField
        }
        defaults.update(kwargs)
        return super(SirTrevorField, self).formfield(**defaults)

    def from_db_value(self, value, expression, connection, context):
        return value

    def to_python(self, value):
        return SirTrevorContent(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        return text_type(value)
