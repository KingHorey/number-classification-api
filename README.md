# Number Classification API

This project is a Flask-based API that provides various information about a given number. The API can classify numbers, check if they are prime, perfect, or Armstrong numbers, and provide fun facts about them.

## Project Structure

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/number-classification.git
cd number-classification
```

## Running the API

To run the API, execute the following command:

```bash
python app.py
```

The API will be available at http://127.0.0.1:5000.

## API Endpoints

### Classify Number

```http
GET /classify?number={number}
```

**Parameters:**

- `number` (required): The number to classify.

**Response:**

```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even", "perfect"],
  "digit_sum": 10,
  "fun_fact": "28 is a perfect number!"
}
```

## Utility Functions

The project includes several utility functions located in the `utils` directory:

- `sum_digits.py`: Contains the `sum_digits` function to calculate the sum of digits
- `armstrong.py`: Contains the `check_armstrong` function for Armstrong numbers
- `fetch_fun_fact.py`: Contains the `get_fun_fact` function for number facts

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
