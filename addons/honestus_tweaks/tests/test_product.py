from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

PRODUCT_MODEL = "product.product"
DEFAULT_CODE = "default_code"
HONESTUS_CODE = "honestus_code"
TEST_PRODUCT_NAME = "test product"


class TestHonestusProduct(TransactionCase):
    """Test Honestus Product extensions."""
    def setUp(self):   # pylint: disable=C0103
        """Create test product with both honestus and default code set."""
        super().setUp()
        self.test_product = self.env[PRODUCT_MODEL].create({
            'name': TEST_PRODUCT_NAME,
            'default_code': DEFAULT_CODE,
            'honestus_code': HONESTUS_CODE
        })

    def test_create_product_with_default_code_and_no_honestus_code(self):
        """Return ValidationError when Honestus code wasn't set while default
        code was."""
        with self.assertRaises(ValidationError) as context:
            self.env[PRODUCT_MODEL].create({
                'name': TEST_PRODUCT_NAME,
                'default_code': DEFAULT_CODE
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

    def test_honestus_code_in_product_name(self):
        """Honestus code is in product name."""
        product_name = self.test_product.display_name
        self.assertEqual(
            product_name,
            f"[{HONESTUS_CODE}] {TEST_PRODUCT_NAME}"
        )

    def test_honestus_code_in_product_name_while_no_default_code(self):
        """Honestus cods is in product name even if there is no default
        code."""
        self.test_product.write({
            'default_code': False
        })
        product_name = self.test_product.display_name
        self.assertEqual(
            product_name,
            f"[{HONESTUS_CODE}] {TEST_PRODUCT_NAME}"
        )

    def test_product_name_with_extra_bracket(self):
        """Honestus code replaces only default code brackets."""
        product_name_extra_bracket = f"{TEST_PRODUCT_NAME} [extra bracket]"
        self.test_product.write({
            'name': product_name_extra_bracket
        })
        product_name = self.test_product.display_name
        self.assertEqual(
            product_name,
            f"[{HONESTUS_CODE}] {product_name_extra_bracket}"
        )
