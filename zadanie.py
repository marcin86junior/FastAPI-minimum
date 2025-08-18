Technical Workshop: Product Catalog API

The goal of this workshop is to design and build a simple API for managing a product catalog. The system should support basic product management, tagging, and search functionality with two distinct access levels: Admin and Public.
## Core Features & Requirements
1. Product Management (Admin Only)

Implement full CRUD (Create, Read, Update, Delete) functionality for products. All of these operations should be restricted to authenticated administrators.
2. Public Product Search

Create a publicly accessible endpoint that allows users to search for products based on the following criteria:

    Name: Search by product name.
    Price: Search by product price.
    Tags: Search by one or more tags.
        Important: When multiple tags are provided in a single search query, the API must return only the products that are associated with all of the specified tags (AND logic).

## Database Schema Design

A key part of this task is to design a database schema that effectively supports the application's features. Your design should account for the following:

    A Product entity with attributes for name (cannot contain numbers), a unique sku, price, and a description (max 300 characters).
    A Tag entity to store tag information.
    A many-to-many relationship between products and tags, allowing a single product to have multiple tags and a single tag to be applied to many products.

You should be prepared to explain the tables, columns, and relationships in your proposed schema.
## Technical Stack & Constraints

    Language & Framework: The application must be built using Python and the FastAPI framework.
    Database: You can use either PostgreSQL or SQLite for data persistence.
    Authentication: For this workshop, a simple mechanism is enough.
