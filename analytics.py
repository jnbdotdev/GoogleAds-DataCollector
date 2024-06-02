import pandas as pd
import matplotlib.pyplot as plt

PATH = 'data/info.csv'

def read_data():
    # Load the CSV file with the correct delimiter
    data = pd.read_csv(PATH, on_bad_lines='warn', delimiter=';')
    data = data.dropna()

    # Filter the data for rows where 'Region' is 'North America'
    north_america_data = data[data['Region'] == 'North America']
    north_america_data = north_america_data.sort_values(by='Value', ascending=True)

    south_america_data = data[data['Region'] == 'South America']
    south_america_data = south_america_data.sort_values(by='Value', ascending=True)

    middle_east_data = data[data['Region'] == 'Europe, Middle East and Africa']
    middle_east_data = middle_east_data.sort_values(by='Value', ascending=True)

    asia_pacific_data = data[data['Region'] == 'Asia and Pacific countries']
    asia_pacific_data = asia_pacific_data.sort_values(by='Value', ascending=True)

    return north_america_data, south_america_data, middle_east_data, asia_pacific_data

def north_america_graphic(north_america_data):
    # Plot the data
    plt.figure(figsize=(10, 6))
    bars = plt.barh(north_america_data['Category'], north_america_data['Value'], color="purple")
    plt.xlabel('Values')
    plt.ylabel('Category')
    plt.title('Region: North America')
    plt.xticks(rotation=90)

    # Add the values inside the bars with white text
    for bar in bars:
        width = bar.get_width()
        plt.text(width,  # Position the text slightly inside the edge
                 bar.get_y() + bar.get_height() / 2,  # Vertical position of the text
                 f'{width}',  # Value text
                 va='center',  # Vertical alignment
                 ha='right',  # Horizontal alignment to the right
                 color='white')  # Text color

    plt.tight_layout()

    # Save the plot as an image
    plot_path = "img/relatory/north_america_relation.png"
    plt.savefig(plot_path)

    # Display the plot
    plt.show()
    
def south_america_graphic(south_america_data):
    # Plot the data
    plt.figure(figsize=(10, 6))
    bars = plt.barh(south_america_data['Category'], south_america_data['Value'], color="purple")
    plt.xlabel('Values')
    plt.ylabel('Category')
    plt.title('Region: South America')
    plt.xticks(rotation=90)

    # Add the values inside the bars with white text
    for bar in bars:
        width = bar.get_width()
        plt.text(width,  # Position the text slightly inside the edge
                 bar.get_y() + bar.get_height() / 2,  # Vertical position of the text
                 f'{width}',  # Value text
                 va='center',  # Vertical alignment
                 ha='right',  # Horizontal alignment to the right
                 color='white')  # Text color

    plt.tight_layout()

    # Save the plot as an image
    plot_path = "img/relatory/south_america_relation.png"
    plt.savefig(plot_path)

    # Display the plot
    plt.show()
    
def middle_east_graphic(middle_east_data):
    # Plot the data
    plt.figure(figsize=(10, 6))
    bars = plt.barh(middle_east_data['Category'], middle_east_data['Value'], color="purple")
    plt.xlabel('Values')
    plt.ylabel('Category')
    plt.title('Region: Europe, Middle East and Africa')
    plt.xticks(rotation=90)

    # Add the values inside the bars with white text
    for bar in bars:
        width = bar.get_width()
        plt.text(width,  # Position the text slightly inside the edge
                 bar.get_y() + bar.get_height() / 2,  # Vertical position of the text
                 f'{width}',  # Value text
                 va='center',  # Vertical alignment
                 ha='right',  # Horizontal alignment to the right
                 color='white')  # Text color

    plt.tight_layout()

    # Save the plot as an image
    plot_path = "img/relatory/middle_east_relation.png"
    plt.savefig(plot_path)

    # Display the plot
    plt.show()

def asia_pacific_graphic(asia_pacific_data):
    # Plot the data
    plt.figure(figsize=(10, 6))
    bars = plt.barh(asia_pacific_data['Category'], asia_pacific_data['Value'], color="purple")
    plt.xlabel('Values')
    plt.ylabel('Category')
    plt.title('Region: Asia and Pacific countries')
    plt.xticks(rotation=90)

    # Add the values inside the bars with white text
    for bar in bars:
        width = bar.get_width()
        plt.text(width,  # Position the text slightly inside the edge
                 bar.get_y() + bar.get_height() / 2,  # Vertical position of the text
                 f'{width}',  # Value text
                 va='center',  # Vertical alignment
                 ha='right',  # Horizontal alignment to the right
                 color='white')  # Text color

    plt.tight_layout()

    # Save the plot as an image
    plot_path = "img/relatory/asia_pacific_relation.png"
    plt.savefig(plot_path)

    # Display the plot
    plt.show()

def run_analytics():
    north_america_data, south_america_data, middle_east_data, asia_pacific_data = read_data()
        
    if not north_america_data.empty:
        north_america_graphic(north_america_data)
    if not south_america_data.empty:
        south_america_graphic(south_america_data)
    if not middle_east_data.empty:
        middle_east_graphic(middle_east_data)
    if not asia_pacific_data.empty:
        asia_pacific_graphic(asia_pacific_data)
    if north_america_data.empty and south_america_data.empty and middle_east_data.empty and asia_pacific_data.empty:
        print('There are no data to analyse')
