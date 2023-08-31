# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestDevelopersManagement(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Developer = self.env['developers.management.developer']
        self.Company = self.env['developers.management.company']

    def test_01_create_developer(self):
        developer_data = {
            'name': 'John Doe',
            'type': 'fullstack',
            'phone': '123456789',
            'email': 'john@example.com',
        }
        developer = self.Developer.create(developer_data)
        self.assertTrue(developer)
        self.assertEqual(developer.global_identification, 'John Doe-fullstack')

    def test_02_create_company(self):
        company_data = {
            'name': 'TechCo',
            'address': '123 Main St',
        }
        company = self.Company.create(company_data)
        self.assertTrue(company)

    def test_03_link_developer_to_company(self):
        developer_data = {
            'name': 'Jane Smith',
            'type': 'backend',
            'phone': '987654321',
            'email': 'jane@example.com',
        }
        developer = self.Developer.create(developer_data)

        company_data = {
            'name': 'DevCo',
            'address': '456 Elm St',
        }
        company = self.Company.create(company_data)

        developer.write({'dev_company_id': company.id})
        self.assertEqual(developer.dev_company_id, company)
        self.assertEqual(len(company.developer_ids), 1)
        self.assertIn(developer, company.developer_ids)
