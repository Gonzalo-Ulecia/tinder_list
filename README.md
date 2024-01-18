# Tinder List

## Description

Tinder List Checker is an open-source OSINT-based tool that allows checking the existence of users on Tinder using a username dictionary. This tool is designed for educational purposes and should be used ethically and legally. The tool's author assumes no responsibility for its misuse.

**User Responsibility:**
This program is for educational purposes only.
The program author is not responsible for misuse.
Each user is responsible for their own actions when executing this code.

## Installation

Before using the tool, make sure to have the requests library installed. You can install it by running the following command:

```bash
pip install requests
```

##Usage

To use Tinder List Checker, follow these steps:

1. Clone the repository or download the tinder_list.py file to your machine.

2. Open a terminal and navigate to the directory where the tinder_list.py file is located.

3. Execute the following command to initiate the search for users on Tinder:

```bash
python3 tinder_list.py <wordlist>
```

## Important Note

The use of Tinder List Checker is the responsibility of each user. Ensure compliance with local laws and regulations, as well as Tinder's usage policies. Do not use this tool to violate the privacy of others without their consent.

## Example of Usage (Controlled Environment)

### Environment
Imagine we want to gather information about a person named Gonzalo. He is interested in cybersecurity, and we suspect he is involved in scams using social networks like Instagram, Twitter, and Tinder.

### Create a Tinder account for testing
![Create tinder account](/img/imagen1.jpg)

### Use tinder_list to verify accounts
    Create a dictionary file named dictionary.txt with entries like:

     ```bash
     gonzalo
     gonzalo_01
     gonzalo_02
     gonzalo1
     gonzalo2
     gonzalo3
     gonzalo4
     gonzalociberseguridad
     gonzalociber
     gonzalo_ciberseguridad
     ...
     ```
![Wordlist](/img/imagen2.jpg)
Running tinder_list tinder_list:
![Ejecución de tinder_list](/img/imagen3.jpg)

### Obtain public information from the Tinder.com account
![Check information on tinder](/img/imagen4.jpg)