# OntarioVaccineFormAutomaker

- Spins up browser windows for X people, autofills health card fields.
- Useful if you're booking for more than one person.

# Requirements

- Installation:
    - Get the chrome driver that is the same as your chrome version: https://chromedriver.chromium.org/downloads
    - To know your chrome verison go to: chrome://version
    - Unzip the chrome driver file
- Must have python3 installed in the system
- Install pip
    - Do ```pip install selenium```

# Steps to use

- Copy the path of the chrome driver and paste it into the last column in the CSV
- Enter your information for each corresponding column in the single row below
- Run script by executing ```python script.py sample.csv```

# Optional
- Add one .csv file per person with their info in them.
- Run multiple windows with one command 
	- This joins the provincial booking site queue (if there is one) with 3 seperate windows for 3 individuals, waits until it's your turn, autofills health card info and logs in.
	- Example - ```python script.py me.csv & python script.py gf.csv & python script.py dad.csv &```


# Other tips
- They say booking opens at 8AM, but the queue is usually open at 730/740AM.