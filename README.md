# PasteQueue

<!-- social-badges:start -->
[![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/jUMuSxGf6q)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/NC1107)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?logo=patreon&logoColor=white)](https://patreon.com/NPC1107)
<!-- social-badges:end -->

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
