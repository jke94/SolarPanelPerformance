[![Netlify Status](https://api.netlify.com/api/v1/badges/8793a9fd-9cca-4efe-bf2f-49de24777914/deploy-status)](https://app.netlify.com/sites/jke94-solar-panel-performance/deploys)

# Solar Panel Performance 
1. Repository with python scripts to extract data plots and data, based on database generated by solar panels.

2. Repository with Angular application to show the solar panel web performance.

![imagen](https://user-images.githubusercontent.com/53972851/162615624-acfe72c9-f2c8-4e8e-a902-99aaff0286a8.png)

## A. Angular, NodeJS and NPM

- Angular CLI: 14.1.0
- Node: 16.14.0
- Package Manager: npm 8.15.1 

## B. Python version
- Python 3.9.6

### B.1. Python script library dependencies
- matplotlib==3.5.1
- numpy==1.22.2
- pandas==1.4.0

## C. How to run

### 1. Data preprocessing.

#### 1.1 Parsing xls files to generate CSV, JSON and Sqlite files.

- Command:

```
python .\01.Backend\src\data-preprocessing\solarpanel_db.py
```
#### 1.2 Extract custom data from raw data file.

- Command:

```
python .\01.Backend\src\data-preprocessing\stadistic-work.py
```

### 2. Data ploting.

#### 2.1 To generate a plot with daily production.

- Command:

```
python .\01.Backend\src\data-plotting\DailyProduction.py
```
#### 2.2 To generate a plot max power time between two dates plot.

- Command:

```
python .\01.Backend\src\data-plotting\MaxPoderTime.py
```
1. Download data (.xls) and put into 'data' folder.
2. Edit 'MaximumDailyProduction.py' file with the correct .xls file name.
3. Run: 'MaximumDailyProduction.py' file.

## Example image:
![DailyProduction](https://user-images.githubusercontent.com/53972851/215266110-67abee3a-37d4-49e5-a823-c47c755aa091.jpg)

