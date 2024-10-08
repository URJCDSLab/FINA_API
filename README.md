# **Automated Results Collection from FINA**

This Python script automates the process of collecting swimming results from the [FINA website](https://www.worldaquatics.com) by calling the [API](#api-endpoint). The results are saved as CSVs based on user-defined parameters specified in `config.py`, with the final Excel file named using the format: **GENDER DISTANCE STROKE.xlsx** (e.g., `F 200 FREESTYLE.xlsx`).

---

## **Installation**

To install the required packages, navigate to the directory and run:

```bash
pip install -r requirements.txt
```
## **Running the Script**

Use the following command to run the script

<pre><code>python ./script.py</code></pre>
<hr>

## **API Endpoint**

API Endpoint is:

<pre><code>https://api.worldaquatics.com/fina/rankings/swimming/report/csv</code></pre>

## **Parameters**
Edit the parameters in the following code block in [config.py](config.py).
<pre>
    <code>
        params={
                "distance": distance, Distance in metres [e.g. (50, 100, 200, 400, 800, 1500). Note for relays (e.g. 4x100, 4x200), leave as 100 or 200]
                "gender": gender,  M is Men, F is Women [e.g. (M or F)]
                "stroke": stroke, Stroke or Style <u>in CAPS</u> [e.g. (FREESTYLE, FREESTYLE_RELAY, BACKSTROKE, BUTTERFLY, MEDLEY)]
                "poolConfiguration": poolConfiguration, Pool configuration/length [e.g. LCM or SCM (LCM is 50m, SCM is 25m)]
                "year": year, Year filter (leave blank if filtering by date range)
                "startDate": startDate, Filter by Start Date (<u>in URL encoded format</u>) [e.g. 01/01/2019 will be "01%2F01%2F2019", whereby %2F denotes a "/"]
                "endDate": endDate, Filter by End Date (<u>in URL encoded format</u>) [e.g. 31/12/2022 will be "31%2F12%2F2022", whereby %2F denotes a "/"]
                "timesMode": timesMode, Get all timings or only best timings [e.g. (ALL_TIMES, BEST_TIMES)]
                "pageSize": pageSize,
                "countryId": countryId, ID of country (this is referenced from [countries.json](countries.json) file, id is provided by FINA website and can be found using network tab of developer console)
            },
    </code>
</pre>


<br/>

### **Changing Countries**

Edit the countries that you would like to get results for in the following code block in [config.py](config.py). Ensure that country name is the same as that defined in fina website.

<pre>
    <code>
        # Define Countries to get results from
        countries_list = [
            "Philippines",
            "Singapore",
            "Malaysia",
            "Vietnam",
            "Indonesia",
            "Thailand",
            "Brunei Darussalam",
            "Myanmar",
            "Lao People's Democratic Republic",
            "Cambodia",
            "Democratic Republic of Timor - Leste",
        ]
    </code>
</pre>

<br/>

## About us
DSLAB URJC. Contact info:

* [DSLAB](https://www.datasciencelab.es)

* [alvaro.novillo@urjc.es](https://www.linkedin.com/in/%C3%A1lvaro-novillo-correas-1b4452226)
