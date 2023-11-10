from odoo import models, fields


class HonestusReport(models.Model):
    """Honestus Sales Report."""
    _name = "honestus.report"
    _description = "Honestus Report"
    _auto = False
    _order = 'name'

    name = fields.Char("Order Reference")
    product_code = fields.Char()
    honestus_code = fields.Char()
    customer = fields.Char()
    customer_id = fields.Integer()
    margin = fields.Float(compute='_compute_margin')
    unit_price = fields.Float()
    honestus_price = fields.Float()
    standard_price = fields.Float("Cost")

    @property
    def _table_query(self):
        return """
SELECT
    min(sol.id) as id,
    partner.id as customer_id,
    partner.name as customer,
    so.name as name,
    pt.default_code as product_code,
    pt.honestus_code as honestus_code,
    pt.list_price as unit_price,
    pt.honestus_price as honestus_price,
    prop.value_float as standard_price
FROM
    sale_order_line sol
    LEFT JOIN sale_order so ON so.id = sol.order_id
    JOIN res_partner partner ON so.partner_id = partner.id
    LEFT JOIN product_product product ON sol.product_id = product.id
    LEFT JOIN product_template pt ON product.product_tmpl_id = pt.id
    LEFT JOIN ir_property prop
        ON prop.res_id = 'product.product,' || product.id
GROUP BY
    partner.id,
    partner.name,
    so.name,
    pt.default_code,
    pt.honestus_code,
    pt.list_price,
    pt.honestus_price,
    prop.value_float
"""

    def _compute_margin(self):
        price = self.honestus_price if self.honestus_price else self.unit_price
        return ((price - self.standard_price) * 100) / price
