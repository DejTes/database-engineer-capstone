## Introducton to Advanced Data Modeling
 - A data model visually represents data elements and their relationships, helping to understand how data is stored, accessed, and updated within a database.
 - It ensures a consistent structure and high-quality data, particularly in entity relational databases, which are often planned using entity relationship diagrams.

 Levels of Data Models"
- **Conceptual Data Model**: High-level, static business structures and concepts.
    - Provides a high-level overview of the database system, presenting entities (like customers, products, and orders) and their relationships.
- **Logical Data Model**: Entity types, data attributes, and relationships.
    - Builds on the conceptual model by detailing entities, their attributes, primary keys, and foreign keys, creating a more structured representation.
- **Physical Data Model**: Database-specific implementation details.
    - Translates the logical model into a technical schema, including tables, columns, data types, and constraints, tailored to the database management system.

NB:  Data modeling is inherently a top-down process, starting with the conceptual model to establish the overall vision, then proceeding to the logical model, and finally the detailed design contained in the physical model

### Types Of Data Models
- **Entity-Relationship Model (ER Model)**: Represents entities and their relationships.
    - is typically represented using entity relationship diagrams (ERDs), which visually depict entities, attributes, and relationships.
    - Entities are objects or concepts, such as customers or products, while relationships describe interactions between entities, like a customer placing an order.

- **The Hierarchical data Model**: Organizes data in a tree-like structure, with parent-child relationships represented by pointers.
    - Each parent can have multiple children, but each child has only one parent.
    - This model is useful for representing one-to-many relationships, like a department with multiple employees.

- **The Object-oriented data model**: Represents data as objects, similar to object-oriented programming.
    - Objects contain data (attributes) and methods (functions), and can inherit from other objects.
    - This model is useful for complex data structures, like multimedia files or geographic information systems.

## Database modeling in MySQL Workbench

    - Forward Engineering: Translates a data model into a physical database schema.
    - Reverse Engineering: Generates a data model from an existing database schema.


## Data Warehousing
- is a centralized repository that aggregates, stores, and processes large amounts of data from multiple sources, allowing for data analysis and reporting.
- Data warehouses are typically used for business intelligence (BI) and decision-making, providing insights into historical and current data trends.

Key Characteristics of Data Warehouses:
- **Subject-Oriented**: Organized around key business subjects, like sales, customers, or products.
- **Integrated**: Combines data from multiple sources, ensuring consistency and accuracy.
- **Time-Variant**: Stores historical data for analysis and comparison over time.
- **Non-Volatile**: Data is read-only and does not change once stored, ensuring data integrity.

Types of Data Warehouses:
- **structured data**: Data that is organized into a tabular format with rows and columns, like a spreadsheet.
- **unstructured data**: Data that does not have a predefined structure, like text documents, images, or videos.

## Datawarehouse Architecture:
The design of the data warehouse's various components.
- data sources: The systems that provide data to the warehouse, such as transactional databases, CRM systems, or external sources.
- Data Staging: ETL (Extract, Transform, Load): Processes that extract data from source systems, transform it into a consistent format, and load it into the data warehouse.
- Data Warehouse: The central repository that stores and manages data for analysis and reporting.
- Data Marts: Subsets of the data warehouse that focus on specific business areas or departments.
- Data anlytics: Tools and techniques used to analyze data and extract insights, such as OLAP (Online Analytical Processing) or data mining.
- Presentation Layer: The interface that allows users to access and interact with the data warehouse, such as dashboards or reports.

Data warehouse architiecture practices:
- Separate analytical and transactional systems: Keep the data warehouse separate from transactional systems to avoid performance issues and ensure data integrity.
- use scalable solutions to process large volumes of data.
- Build a flexible architecture that can adapt to changing business needs and data sources.

![datawarehouse](/advanced_data_modeling/datawarehous.png)
