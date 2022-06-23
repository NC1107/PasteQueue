# PasteQueue

mass queue to clipboard from text file with the option of a delimiter, now with either python CLI or as a desktop application.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install keyboard, the other required packages are built into python.

For the desktop application version, download the PasteQueue zip from the main branch, unzip, run the exe.

```bash
pip install keyboard os sys time
```

## Usage

```bash
python .\main.py <filename>.txt <optional_delimiter>
```
Example file with **no dilimiter**
```
apples
pears
cucumber
```
this will automatically accept it as a newline delimeter and seperate the list as such, also works with single-line spaced elements, otherwise feed it the delimeter of your choice and it will seperate it as you requested.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
