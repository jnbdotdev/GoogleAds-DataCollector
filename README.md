<h1 width="100%">
  <img src="img/Logo.png" align="center"/>
</h1>
<div class="badges" align="center">
  <img src="https://img.shields.io/static/v1?label=Language&labelColor=D18CE0&message=Python&color=F6F5F2&style=for-the-badge"/>
  <img src="https://img.shields.io/static/v1?label=Status&labelColor=D18CE0&message=Finished&color=F6F5F2&style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/static/v1?label=Version&labelColor=D18CE0&message=1.1.0&color=F6F5F2&style=for-the-badge&logo=vonage"/>
  <img src="https://img.shields.io/static/v1?label=License&labelColor=D18CE0&message=MIT&color=F6F5F2&style=for-the-badge&logo=perforce"/>
</div>
<br>
<h2 id="about">1. About</h2>
<p>
  This software is designed to collect data from Google's AdSense calculator using Selenium for web automation. It uses customtkinter for the graphical user interface (GUI), OpenCV and Tesseract for image processing and optical character recognition (OCR), and Matplotlib and pandas for data analysis and visualization.
</p>
<br>

<h2 id="summary">2. Summary</h2>
<details open>
  <summary>Summary</summary><br>
  The application automates the process of selecting categories and regions from the Google AdSense calculator, captures the displayed results using screenshots, extracts text from the images using OCR, and stores the data in a CSV file. It then generates visual charts for further analysis of the collected data.<br/>
  
  * [About](#about)
    
  * [Summary](#summary)
    <details open>
    <summary target="#howtouse">How to use</summary>

    * [Pre-requisites](#prerequisites)
    * [Tesseract installation](#tesseract_instalation)
    * [Interface tutorial](#interface_tutorial)
    * [Data interpretation](#data_interpretation)
      <details closed>
      <summary target="#extra">Extra</summary>
      
        * [Excel integration](#excel_integration)
      </details>
    </details>
    
    <details open>
    <summary target="#howitworks">How it works?</summary>

    * [Interface interaction](#interface_interaction)
    
    * [Automation process](#automation_process)
      
    * [Image capture](#image_capture)
      
    * [Text extraction](#text_extraction)
      
    * [Data storage](#data_storage)
   
    * [Data collection](#data_collection)
      
    * [Chart creation](#chart_creation)
  </details>

  * [Tests](#tests)
    
  * [Technologies](#technologies)
</details>

<br/>
<h2 id="howtouse">3. How to use</h2>
  <h3 id="prerequisites">3.1 Pre-requisites</h3>
  <ul>
        <li>Python 3.x</li>
        <li>Selenium</li>
        <li>OpenCV</li>
        <li>Pytesseract</li>
        <li>Matplotlib</li>
        <li>Pandas</li>
        <li>CustomTkinter</li>
    </ul>
  <h3 id="tesseract_instalation">3.2 Tesseract installation</h3>
  <ol>
        <li>Download the Tesseract installer from <a href="https://github.com/tesseract-ocr/tesseract">Tesseract GitHub</a>.</li>
        <li>Run the installer and follow the instructions.</li>
        <li>Add the Tesseract installation path to your system's PATH environment variable.</li>
    </ol>
  <h3 id="interface_tutorial">3.3 Interface tutorial</h3>
    <p>This section provides a detailed guide on how to navigate and use the graphical user interface (GUI) of the software for collecting data from Google's AdSense calculator.</p>
    <h4>Step-by-Step Guide to Using the Interface</h4>
    <h5>1. Launching the Interface</h5>
    <p>
        Ensure all dependencies are installed and correctly configured, including Tesseract and the web driver.<br>
        Run the <code>interface.py</code> script using Python:
    </p>
    <pre><code>python interface.py</code></pre>
    <p>
        This will open the main GUI window titled "Google AdSense - Data Collector".
    </p>
    <h5>2. Understanding the Main Window Layout</h5>
    <p>
        The window is divided into two scrollable frames:
    </p>
    <ul>
        <li><strong>Left Frame (Regions)</strong>: Contains checkboxes for selecting regions.</li>
        <li><strong>Right Frame (Categories)</strong>: Contains checkboxes for selecting categories.</li>
    </ul>
    <h5>3. Selecting Regions</h5>
    <p>
        The regions are displayed in the left scrollable frame.<br>
        The available regions are:
    </p>
    <ul>
        <li>North America</li>
        <li>South America</li>
        <li>Europe, Middle East, and Africa</li>
        <li>Asia and Pacific countries</li>
    </ul>
    <p>
        Click the checkbox next to each region you want to include in the data collection.
    </p>
    <h5>4. Selecting Categories</h5>
    <p>
        The categories are displayed in the right scrollable frame.<br>
        The available categories include:
    </p>
    <ul>
        <li>Arts and entertainment</li>
        <li>Automobiles and vehicles</li>
        <li>House and garden</li>
        <li>Science</li>
        <li>Food and drinks</li>
        <li>Shopping</li>
        <li>And many more (as listed in the initial script)</li>
    </ul>
    <p>
        You can individually select the categories by clicking the checkboxes next to each one.
    </p>
    <h5>5. Using the "Select All" Feature</h5>
    <p>
        At the top of the right scrollable frame, there is a "Select All" checkbox.<br>
        Clicking this checkbox will select or deselect all category checkboxes:
    </p>
    <ul>
        <li>If you want to select all categories, check this box.</li>
        <li>If you want to deselect all categories, uncheck this box.</li>
    </ul>
    <h5>6. Confirming Selections</h5>
    <p>
        After selecting the desired regions and categories, click the "Confirm" button at the bottom center of the window.<br>
        The confirm button triggers the data collection process:
    </p>
    <ul>
        <li>If any region or category is unselected, a message will be printed indicating that there are unselected options.</li>
        <li>Ensure that at least one region and one category are selected before clicking "Confirm".</li>
    </ul><br>
  <h3 id="data_collection">3.4 Data collection</h3><br/>
  <p>The process of collecting information involves several steps:</p>
    <ol>
        <li><strong>Initialization:</strong> The software initializes Selenium and opens the Google AdSense website. The user-provided login credentials are used to authenticate and access the required data pages.</li>
        <li><strong>Navigation:</strong> Selenium automates the navigation through the Google AdSense website. It selects the specified regions and categories based on user input.</li>
        <li><strong>Screenshot Capture:</strong> Once the relevant data is displayed, the software captures screenshots of the web pages using the pyscreenshot library.</li>
        <li><strong>Image Processing:</strong> The captured screenshots are processed using OpenCV to enhance the quality of the images. This includes noise reduction, thresholding, and edge detection to prepare the images for OCR.</li>
        <li><strong>Text Extraction:</strong> Pytesseract is used to extract text from the processed images. The extracted text is parsed to identify the required numeric values and associated categories.</li>
        <li><strong>Data Storage:</strong> The extracted data is organized and saved into a CSV file located at <code>data/info.csv</code>. This file contains columns for the category, value, region, and status (indicating whether the data was collected on the first attempt or reviewed).</li>
    </ol><br>
  <h3 id="data_interpretation">3.5 Data interpretation</h3><br/>
  <p>After the data is collected, it is saved in a CSV file located at <code>data/info.csv</code>. The data includes the following columns:</p>
    <ul>
        <li><strong>Category:</strong> The ad category.</li>
        <li><strong>Value:</strong> The collected value for the category.</li>
        <li><strong>Region:</strong> The region associated with the data.</li>
        <li><strong>Status:</strong> Indicates whether the data was collected on the first attempt or reviewed.</li>
    </ul>
  <h3 id="extra">3.6 Extra</h3>
    <h3 id="excel_integration">Excel integration</h4>
    <ol>
      <li>
        <h4>Open Excel and Import the CSV Data:</h4>
        <ul>
          <li>Open Excel and create a new spreadsheet.</li>
          <li>Go to the "Data" tab and click on "From Text/CSV".</li>
          <li>Select the CSV file generated by your program that contains the data you want to use for the chart and click "Import".</li>
        </ul>
      </li>
      <li>
        <h4>Set Up the Import:</h4>
        <ul>
          <li>In the import window, ensure that the delimiter and data type are correct. Excel usually auto-detects the delimiter and data type.</li>
          <li>Click "Load" to import the data into Excel.</li>
        </ul>
      </li>
      <li>
        <h4>Create a Pivot Table:</h4>
        <ul>
          <li>With the data imported into the spreadsheet, select any cell within the data range.</li>
          <li>Go to the "Insert" tab and click on "Pivot Table". Choose "Pivot Table" from the dropdown menu.</li>
          <li>In the "Create PivotTable" window, confirm that the data range is correct and choose where you want to place the Pivot Table on the worksheet. Click "OK".</li>
        </ul>
      </li>
      <li>
        <h4>Configure the Pivot Table:</h4>
        <ul>
          <li>In the new right-hand side pane, you'll see fields like "Row Labels", "Column Labels", "Values", etc.</li>
          <li>Drag the relevant fields into the desired areas. For example, you can place the "Category" field in "Row Labels" and the "Value" field in "Values".</li>
          <li>This will create a Pivot Table summarizing the data based on your configuration.</li>
        </ul>
      </li>
      <li>
        <h4>Create the Pivot Chart:</h4>
        <ul>
          <li>With the Pivot Table configured, select any cell within it.</li>
          <li>Go to the "Insert" tab and click on "PivotChart". Choose the type of chart you want to create (e.g., column chart, line chart, pie chart, etc.).</li>
          <li>Once the chart is created, you can adjust details like titles, legends, colors, etc., by right-clicking on the chart and selecting the desired options.</li>
        </ul>
      </li>
      <li>
        <h4>Update the Pivot Chart:</h4>
        <ul>
          <li>Whenever your data in the CSV is updated or new data is added, you can update the Pivot Chart by right-clicking on the Pivot Table and selecting "Refresh".</li>
        </ul>
      </li>
    </ol>
<br/>
<h2 id="howitworks">4. How it works?</h2>
  <h3 id="interface_interaction">4.1 Interface interaction</h3>
    <p>The interface is built using CustomTkinter, providing a simple GUI for selecting regions and categories for data collection.</p>
    <h3 id="automation_process">4.2 Automation process</h3>
    <p>The automation process uses Selenium to navigate the Google AdSense website, selecting regions and categories based on user input.</p>
    <h3 id="image_capture">4.3 Image capture</h3>
    <p>The software captures screenshots of the results displayed on the website using the pyscreenshot library.</p>
    <h3 id="text_extraction">4.4 Text extraction</h3>
    <p>Extracted text from screenshots using Tesseract OCR is processed to remove non-numeric characters and obtain the desired values.</p>
    <h3 id="data_storage">4.5 Data storage</h3>
    <p>The collected data is stored in a CSV file for further analysis and visualization.</p>
    <h3 id="chart_creation">4.6 Chart creation</h3>
    <p>The stored data is used to create visual charts using Matplotlib, providing a graphical representation of ad values across different regions and categories.</p><br>

<h2 id="tests">5. Tests</h2>
<p>To ensure the software functions correctly, tests can be run to verify the following:</p>
    <ul>
        <li>Proper installation of dependencies.</li>
        <li>Correct functionality of Selenium web automation.</li>
        <li>Accuracy of Tesseract OCR text extraction.</li>
        <li>Data integrity in the CSV file.</li>
        <li>Proper generation of visual charts.</li>
    </ul>
<br>
<h2 id="technologies">6. Technologies</h2>
<p>This project utilizes the following technologies:</p>
    <ul>
        <li><strong>Python:</strong> The main programming language used for development.</li>
        <li><strong>Selenium:</strong> Used for web automation and interaction.</li>
        <li><strong>OpenCV:</strong> Used for image processing tasks.</li>
        <li><strong>Pytesseract:</strong> Utilized for Optical Character Recognition (OCR).</li>
        <li><strong>pyscreenshot:</strong> Used for capturing screenshots.</li>
        <li><strong>CustomTkinter:</strong> Used for creating the graphical user interface.</li>
        <li><strong>Pandas:</strong> Used for data manipulation and analysis.</li>
        <li><strong>Matplotlib:</strong> Used for creating visual charts.</li>
    </ul>
