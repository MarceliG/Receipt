# Receipt

# Usage

1. (Recommended but not necessary) Create a virtual environment:
    
    `python3.10 -m venv .venv`

    - Activate them: 
    
    `source .venv/bin/activate`

2. Ensure you have the required libraries installed using pip:
    
    `pip install -r requirements.txt`

3. Prepare functions package:

    `python3 -m pip install --upgrade pip`

    `pip install -e functions/`

    Next Reload window


# Program flow 
1. upload receipt
2. remove shadow from image
3. rotate image to correct position
4. recognition text from image
5. extract text to csv file


```
mypy project/ --ignore-missing-imports
```