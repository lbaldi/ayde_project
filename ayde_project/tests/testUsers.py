from openerp.tests.common import TransactionCase

class testUsers(TransactionCase):
        def test_salario(self):
                record = self.env['model.ResUsers'].create({'salary':'200'})
                self.assertEqual(record.salary,200)

