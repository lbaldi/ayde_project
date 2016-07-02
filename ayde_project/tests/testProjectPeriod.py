from openerp.tests.common import TransactionCase

class testProjectPeriod(TransactionCase):
	record = self.env['model.project_period'].create[{'name':'ayde'}]
	self.assertEqual(record.name,'ayde')
