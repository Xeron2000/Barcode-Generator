# Barcode Generator CLI

This is a simple command-line tool for generating barcodes in bulk, based on a specified text pattern. It uses the `python-barcode` library to generate barcodes in the `code128` format and saves the output images as `.png` files in a specified directory.

## Features

- Generates barcodes using the `code128` format.
- Saves the barcodes as `.png` images.
- Allows batch generation of barcodes with similar text (e.g., `S1`, `S2`, ..., `S10`).
- Automatically creates a folder for organizing the generated barcode images.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Xeron2000/Barcode-Generator.git
   cd Barcode-Generator
   ```

2. **Install the dependencies**:

   ```bash
   pip install python-barcode Pillow
   ```

## Usage

To generate barcodes from the command line, use the following syntax:

```bash
python code.py BASE_TEXT START_NUMBER END_NUMBER
```

### Parameters:

- `BASE_TEXT`: The base text for the barcode. For example, if you want barcodes like `S1`, `S2`, ..., `S10`, the base text would be `S`.
- `START_NUMBER`: The starting number for the barcode sequence.
- `END_NUMBER`: The ending number for the barcode sequence.

### Example:

To generate barcodes from `S1` to `S10` and save them in a folder named `S`, run:

```bash
python code.py S 1 10
```

This will generate the following barcodes and save them as images in the `S` folder:

```
S/S1.png
S/S2.png
S/S3.png
...
S/S10.png
```

### Output:

Each barcode will be saved as a `.png` image with the filename format `<BASE_TEXT><NUMBER>.png` (e.g., `S1.png`, `S2.png`, etc.).

## Folder Structure

The output barcodes will be stored in a folder named after the `BASE_TEXT` parameter. For example, if `BASE_TEXT` is `S`, the structure will look like this:

```
Barcode-Generator/
├── S/
│   ├── S1.png
│   ├── S2.png
│   ├── ...
│   └── S10.png
├── code.py
```

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`:
  - `python-barcode`
  - `Pillow`

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.
