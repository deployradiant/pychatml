# chatml

The `chatml` package allows you to convert chat interfaces from and to the ChatML format.

## Installation

You can install the `chatml` package using pip:

```shell
pip install chatml
```

## Usage

To use the `chatml` package, you need to import the `ChatMLConverter` and `ChatMLParser` classes from the `chatml` module:

```python
from chatml.converter import ChatMLConverter
from chatml.parser import ChatMLParser
```

### Converting to ChatML

To convert a chat interface to the ChatML format, you can use the `to_chatml` method of the `ChatMLConverter` class:

```python
converter = ChatMLConverter()
chatml = converter.to_chatml(chat_interface)
```

### Converting from ChatML

To convert a chat interface from the ChatML format, you can use the `from_chatml` method of the `ChatMLConverter` class:

```python
converter = ChatMLConverter()
chat_interface = converter.from_chatml(chatml)
```

### Parsing ChatML

To parse a chat interface in the ChatML format, you can use the `parse_chatml` method of the `ChatMLParser` class:

```python
parser = ChatMLParser()
parsed_chatml = parser.parse_chatml(chatml)
```

### Validating ChatML

To validate a chat interface in the ChatML format, you can use the `validate_chatml` method of the `ChatMLParser` class:

```python
parser = ChatMLParser()
is_valid = parser.validate_chatml(chatml)
```

## Contributing

Contributions to the `chatml` package are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
```

Please note that this is just a template, and you should customize it to provide accurate and relevant information about your `chatml` package.