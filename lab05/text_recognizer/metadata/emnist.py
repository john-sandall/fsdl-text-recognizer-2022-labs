from __future__ import annotations

from pathlib import Path

from text_recognizer.metadata import shared

RAW_DATA_DIRNAME = shared.DATA_DIRNAME / "raw" / "emnist"
METADATA_FILENAME = RAW_DATA_DIRNAME / "metadata.toml"
DL_DATA_DIRNAME = shared.DATA_DIRNAME / "downloaded" / "emnist"
PROCESSED_DATA_DIRNAME = shared.DATA_DIRNAME / "processed" / "emnist"
PROCESSED_DATA_FILENAME = PROCESSED_DATA_DIRNAME / "byclass.h5"
ESSENTIALS_FILENAME = Path(__file__).parents[1].resolve() / "data" / "emnist_essentials.json"

NUM_SPECIAL_TOKENS = 4
INPUT_SHAPE = (28, 28)
DIMS = (1, *INPUT_SHAPE)  # Extra dimension added by ToTensor()
OUTPUT_DIMS = (1,)

MAPPING = [
    "<B>",
    "<S>",
    "<E>",
    "<P>",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
    "!",
    '"',
    "#",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "?",
]
