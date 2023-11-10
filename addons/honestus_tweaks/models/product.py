import re
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

    def _honestus_product_name(self, name_get):
        """Map default code to honestus code."""
        p_id = name_get[0]
        p_name = name_get[1]
        product = self.browse(p_id)
        if self._context.get('display_default_code', True):
            default_code = product.default_code
            honestus_code = product.honestus_code
            if default_code and honestus_code:
                regex = r"^\[.*?\]"
                p_name = re.sub(regex, f"[{honestus_code}]", p_name)
            if not default_code and honestus_code:
                p_name = f"[{honestus_code}] {p_name}"
        return (p_id, p_name)

    def name_get(self):
        """Replace default code in product name with honestus code."""
        product_names = super().name_get()
        return map(self._honestus_product_name, product_names)
