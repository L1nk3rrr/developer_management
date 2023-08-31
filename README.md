# Odoo Developer Management Module

## Description

This Odoo module, named "developers_management," is designed to simplify the management of developers within the Odoo 16 Community platform. It offers a user-friendly interface for handling developer-related information, including personal details and associations with companies. The module introduces the concept of Developers and their relationships with Companies, enhancing the overall developer management process.

## Features

### Developer Model

- **Name:** Each developer has a unique name.
- **Type:** Developers are categorized into types: "front-end," "backend," "fullstack," or "out-stuff."
- **Global Identification:** A computed field combining the developer's name and type.
- **Phone:** Contact phone number for the developer (displayed if not "out-stuff").
- **Email:** Developer's email address.
- **Address:** Address details for the developer.
- **Birthdate:** Birthdate of the developer.
- **Company:** Association of developers with companies.

### Company Model

- **Name:** Each company has a unique name.
- **Address:** Address details of the company.
- **Developers:** One2many relationship linking developers with the company.

## Module Functionality

### Developer List View

- A tree view displaying developers with filters for name, phone number, and type.
- Grouping by developer type for better organization.

### Developer Form View

- Form view for adding and editing developer records.
- Easy management of developer details and associations.

### Company List View

- A dedicated view displaying a list of companies along with their associated developers.

### Menu Navigation

- "Developers" menu offering two main actions:
  - "View Developers" to navigate to the list of developers.
  - "Add Developer" to add a new developer.
  - "View Company" to navigate to the list of Companies.
  - "Add Company" to add a new Company.

### Access Rights

- Secure access to functionality, allowing only registered users to view and add developers and companies.
- Restricted access to editing and deletion rights, ensuring data integrity.