# Supercomp - Supermarket Management System

## Overview
Supercomp is a supermarket management system that allows clients to order products. The system includes:
- **Stock Management**: Manage available products.
- **Order System**: Clients can place orders.
- **CLI Interface**: A command-line interface for easy interaction.

## Project Structure
- `models.py`: Defines the database schema and models using SQLAlchemy.
- `cli.py`: Provides a command-line interface to interact with the system.
- `README.md`: Documentation for using the system.

## Setup Instructions

### Prerequisites
- Python 3.x installed
- Virtual environment (optional but recommended)
- Install dependencies using:

  ```sh
  pip install -r requirements.txt
  ```

### Database Initialization
1. Create the database and tables:

   ```sh
   python models.py
   ```

2. The database file (`supercomp.db`) will be generated.

## Usage
Run the command-line interface using:
```sh
python cli.py
```

### Available Commands
- **Create a client**: Register a new client.
- **Add a product**: Add a new product to stock.
- **Place an order**: Clients can place orders for products.
- **List all clients**: View registered clients.
- **List all products**: View available products.
- **List all orders**: View all placed orders.

## Enhancements & Features
- **Input Validation**: Ensures valid IDs and values are entered.
- **Error Handling**: Prevents crashes from invalid database operations.
- **Improved User Experience**: Clear prompts and messages.

## Testing
- Ensure database operations work correctly.
- Test edge cases (invalid inputs, missing records, etc.).

## Future Improvements
- Implement a web-based UI.
- Add role-based access control for staff and clients.

## License
MIT License

## Contact
For support or contributions, please contact the project maintainers.

