# Machine_Learning
This repository consists of all the subjects that are needed to start machine learning. I will keep update it from time to time. If you would like to learn machine learning by yourself, it is advisable to follow the steps bellow in order to have a better understanding about machine learning.

If you would like to have the comments in different colors, you can install Better Comments in Extension. You can follow the settings I have been made or follow you own.

```
"better-comments.multilineComments": true,
    "better-comments.highlightPlainText": false,
    "better-comments.tags": [
    
        {
          "tag": "?",
          "color": "#7533FF",
          "strikethrough": false,
          "underline": false,
          "backgroundColor": "transparent",
          "bold": false,
          "italic": false
        },
        {
          "tag": "*",
          "color": "#33BDFF",
          "strikethrough": false,
          "underline": false,
          "backgroundColor": "transparent",
          "bold": false,
          "italic": false
        },
        {
          "tag": "!",
          "color": "#FF3357",
          "strikethrough": true,
          "underline": false,
          "backgroundColor": "transparent",
          "bold": false,
          "italic": false
        },
        {
          "tag": "todo",
          "color": "#FF8C00",
          "strikethrough": false,
          "underline": false,
          "backgroundColor": "transparent",
          "bold": false,
          "italic": false
        }
    ],
```

To read content from webpage, you need to import requests and BeautifulSoup4 into Python file (needed for Practice_Python/Q17.py & Q19.py):

Step 1:
- In your text editor, open Terminal > New Terminal and run the following command in order to create a new virtual environment
```
python3 -m venv venv
```
To activate it, if you are on windows, type the following:
```
venv\Scripts\activate.bat
```
If you are on Linux/Mac, then type this instead:
```
source venv/bin/activate
```
-Now, you can see (venv) in front of your file directory in the terminal

Step 2:
- Type the following command in the terminal and install the requests module:
```
pip install requests
```
- Type the following command in the terminal and install the BeautifulSoup4 module
```
pip install beautifulsoup4
```