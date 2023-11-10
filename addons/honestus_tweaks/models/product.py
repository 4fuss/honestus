from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HonsestusProductTemplate(models.Model):
    """Honestus Product Template extensions."""
    _inherit = 'product.template'

    honestus_code = fields.Char(string='Honestus code')
    honestus_price = fields.Float(string='Honestus price')


class HonestusProductProduct(models.Model):
    """Honestus Product extensions."""
    _inherit = 'product.product'

    @api.constrains('default_code', 'honestus_code')
    def _validate_honestus_code(self):
        """Honestus code is required when default code is set."""
        for record in self:
            if (
                record.honestus_code is False
                and record.default_code is not False
            ):
                raise ValidationError(
                    _("Honestus code is required when default code is set.")
                )
