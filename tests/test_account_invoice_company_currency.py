# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import doctest
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_teardown
from trytond.tests.test_tryton import doctest_checker

class AccountInvoiceCompanyCurrencyTestCase(ModuleTestCase):
    'Test Account Invoice Company Currency module'
    module = 'account_invoice_company_currency'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountInvoiceCompanyCurrencyTestCase))
    suite.addTests(doctest.DocFileSuite(
            'scenario_invoice_company_currency.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
