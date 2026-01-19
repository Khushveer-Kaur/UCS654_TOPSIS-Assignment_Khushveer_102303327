# UCS654 TOPSIS Assignment

### Name: Khushveer Kaur  
### Roll Number: 102303327  
### Course: UCS654 – Predictive Analysis Using Statistics  
### Institute: Thapar Institute of Engineering and Technology  

---

## Overview

This repository contains the complete implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** algorithm as part of the UCS654 assignment.

The assignment is divided into three independent parts:

1. Command Line Interface (CLI) based implementation  
2. Python Package (PyPI-style) implementation  
3. Web Service implementation using Flask  

Each part follows the same TOPSIS methodology and produces consistent results.

---

## TOPSIS Methodology (Numerical Steps)

Given a decision matrix with alternatives and criteria, TOPSIS is implemented using the following steps:

### Step 1: Construct the Decision Matrix  
A matrix is formed where rows represent alternatives and columns represent criteria.

### Step 2: Normalize the Decision Matrix  
Each value is normalized using vector normalization:

\[
r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{n} x_{ij}^2}}
\]

### Step 3: Construct the Weighted Normalized Matrix  
Each normalized value is multiplied by its corresponding weight:

<img width="376" height="261" alt="image" src="https://github.com/user-attachments/assets/2483bd68-ffbd-462f-9fc7-10a961336723" />


### Step 4: Determine Ideal Best and Ideal Worst  
- **Ideal Best (A⁺)**: Maximum value for benefit criteria, minimum for cost criteria  
- **Ideal Worst (A⁻)**: Minimum value for benefit criteria, maximum for cost criteria  

### Step 5: Calculate Separation Measures  
Distance of each alternative from ideal best and ideal worst:

<img width="841" height="370" alt="image" src="https://github.com/user-attachments/assets/cbec4c37-f8e8-4645-b340-c0f4142c01a4" />


### Step 6: Calculate TOPSIS Score  
<img width="462" height="133" alt="image" src="https://github.com/user-attachments/assets/4b563f60-1d0f-4600-b393-e6d90cc3b64b" />


### Step 7: Rank the Alternatives  
Alternatives are ranked in descending order of TOPSIS score.

---

## Part 1: CLI Based TOPSIS

### Description
- Implements TOPSIS as a command-line tool
- Accepts:
  - Input CSV file
  - Weights (comma-separated)
  - Impacts (`+` or `-`)
- Outputs a CSV file containing TOPSIS score and rank

### Result
- Successfully computes TOPSIS score for all alternatives
- Output CSV includes:
  - Original data
  - TOPSIS Score
  - Rank

### CLI Implementation

<img width="1449" height="468" alt="image" src="https://github.com/user-attachments/assets/0cfaf1ca-4c50-4350-83c5-3ab4b0f80a18" />

### Output (result.csv) appears in the directory

<img width="1555" height="509" alt="image" src="https://github.com/user-attachments/assets/c316d881-461b-4ec1-8842-c65e98616bca" />


Detailed instructions are available in  
`Part-1-CLI-TOPSIS/README.md`

---

## Part 2: Python Package (PyPI Style)

### Description
- TOPSIS implemented as a reusable Python package
- Proper package structure:
  - `setup.py`
  - `LICENSE`
  - Modular logic
- Can be imported and used in other Python projects

### Result
- Package executes correctly when imported
- Produces same TOPSIS scores as CLI version
- Link:  <https://pypi.org/project/Topsis-Khushveer-102303327/0.0.2/> 

<img width="1603" height="906" alt="image" src="https://github.com/user-attachments/assets/0012f225-df72-46d7-9724-90683a262c12" />


Detailed instructions are available in  
`Part-2-PyPI-Package/README.md`

---

## Part 3: Web Service (Flask)

### Description
- Web-based TOPSIS implementation using Flask
- Features:
  - CSV file upload
  - User-defined weights and impacts
  - Email input for result delivery
- Backend uses the same TOPSIS logic for consistency

### Result 
- TOPSIS score calculated correctly
- Result CSV generated on submission
- Email functionality implemented using SMTP (Gmail)

### Web Interface
<img width="1908" height="941" alt="image" src="https://github.com/user-attachments/assets/60a122a9-a397-45da-8b86-006f5df494dc" />

<img width="388" height="127" alt="image" src="https://github.com/user-attachments/assets/40523c8e-994e-47c3-8019-9e5818a13266" />

### data.csv uploaded 
<img width="558" height="279" alt="image" src="https://github.com/user-attachments/assets/84e9a716-c6f2-4840-806f-2dcdbbc59a1e" />

### result.csv received via email
<img width="1105" height="375" alt="image" src="https://github.com/user-attachments/assets/6c51a1fc-4911-4359-ae00-0621c82459f1" />


Detailed instructions are available in  
`Part-3-Web-Service/README.md`

---

## Tech Stack

- Python  
- Flask  
- Pandas, NumPy  
- HTML / CSS  
- SMTP (Gmail)

---

## Conclusion

This project demonstrates a complete and modular implementation of the TOPSIS algorithm across multiple interfaces.  
The same core logic is reused to ensure correctness, consistency, and scalability.

---





