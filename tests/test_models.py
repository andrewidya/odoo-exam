from odoo.tests.common import TransactionCase
from odoo.tests import tagged
from odoo.exceptions import ValidationError


@tagged('post-install')
class KedatechSupplierTestCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(KedatechSupplierTestCase, cls).setUpClass()
        cls.supplier = cls.env['res.partner'].create({'name': 'Test Supplier'})

    def test_supplier_rank_in_creation(self):
        """Test that supplier_rank has 1 when created"""
        self.assertEqual(self.supplier.supplier_rank, 1)

    def test_customer_rank_in_creation(self):
        """Test that customer_rank has 0 when created"""
        self.assertEqual(self.supplier.customer_rank, 0)


@tagged('post-install')
class KedatechMaterialTestCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.supplier = cls.env['res.partner'].create({'name': 'Test Supplier'})

    def test_buy_price_cannot_less_than_100(self):
        """Test than buy price cannot less than 100"""
        with self.assertRaises(ValidationError) as context:
            material = self.env['kedatech.material'].create({
                'name': 'MAT-001',
                'code': 'MAT001',
                'material_type': 'jeans',
                'buy_price': 99,
                'supplier': self.supplier.id
            })

        self.assertTrue(isinstance(context.exception, ValidationError))
        self.assertTrue("Buy price cannot be less than 100" in str(context.exception))
