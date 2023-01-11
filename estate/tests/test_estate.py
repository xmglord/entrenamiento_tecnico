from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.tests.common import Form


@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(EstateTestCase, cls).setUpClass()

        cls.buyer = cls.env['res.partner'].create([{
            'name': 'test_buyer',
            }])
        cls.properties = cls.env['estate.property'].create([{
            'name': 'test_prop1',
            'expected_price': 100,
            }])
        cls.offers = cls.env['estate.property.offer'].create([{
            'partner_id': cls.buyer.id,
            'property_id': cls.properties[0].id,
            'price': 95,
            }])

    def test_action_sell(self):
        with self.assertRaises(UserError):
            self.properties.action_sold()

        self.offers.action_accept()

        self.properties.action_sold()
        self.assertRecordValues(self.properties, [
            {'state': 'sold'},
            ])

        with self.assertRaises(UserError):
            self.env['estate.property.offer'].create([{
                'partner_id': self.buyer.id,
                'property_id': self.properties[0].id,
                'price': 100,
                }])

    def test_property_form(self):
        with Form(self.properties[0]) as prop:
            self.assertEqual(prop.garden_area, 0)
            self.assertIs(prop.garden_orientation, False)
            prop.garden = True
            self.assertEqual(prop.garden_area, 10)
            self.assertEqual(prop.garden_orientation, "north")
            prop.garden = False
            self.assertEqual(prop.garden_area, 0)
            self.assertIs(prop.garden_orientation, False)
