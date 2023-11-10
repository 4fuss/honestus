from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

PRODUCT_MODEL = 'product.product'


class TestHonestusProduct(TransactionCase):
    """Test Honestus Product extensions."""
    def setUp(self):   # pylint: disable=C0103
        """Create test product with both honestus and default code set."""
        super().setUp()
        self.test_product = self.env[PRODUCT_MODEL].create({
            'name': 'test product',
            'default_code': 'test',
            'honestus_code': 'test'
        })

    def test_create_product_with_default_code_and_no_honestus_code(self):
        """Return ValidationError when Honestus code wasn't set while default
        code was."""
        with self.assertRaises(ValidationError) as context:
            self.env[PRODUCT_MODEL].create({
                'name': 'test product',
                'default_code': 'test'
            })
        self.assertTrue("Honestus code is required" in str(context.exception))

    def test_write_product_with_default_code_and_honestus_code(self):
        """Check if exception is raised when honestus code set to None while
        default code is set."""
        with self.assertRaises(ValidationError) as context:
            self.test_product.write({
                'honestus_code': False
            })
        self.assertTrue("Honestus code is required" in str(context.exception))
