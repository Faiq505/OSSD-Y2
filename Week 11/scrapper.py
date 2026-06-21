import requests
from bs4 import BeautifulSoup
import csv

def get_cars_data(car):
    
    url=f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response=requests.get(url, headers=headers)

    cars=[]
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        tables=soup.find_all('table')
        if not tables:
            print("No tables found on the webpage.")
        for table in tables:
            rows=table.find_all('tr')
            for row in rows:
                cols=row.find_all('td')
                if len(cols)>= 2:
                    name=cols[0].get_text()
                    price=cols[1].get_text()
                    cars.append({'name': name, 'price': price})
                  
            
    else:
        print("Failed to retrieve the webpage.")    
        
    return cars


#create a function to scrape data from the webpage, the above code can be used inside the function
def scrapper():
    print("--- PakWheels Price Scraper ---")
    
    # 1. User se car brand ka naam input liya (e.g., suzuki, toyota, honda)
    car_brand = input("Kisi car brand ka naam likhein: ")
    
    # .lower() ka use kiya taake URL ka format kharab na ho (Suzuki -> suzuki)
    car_brand_clean = car_brand.strip().lower()
    
    print(f"\n{car_brand_clean} ka data nikala ja raha hai, thora intezar karein...")
    
    # 2. get_cars_data function ko call kiya jo website se data layega
    scraped_data = get_cars_data(car_brand_clean)
    
    # 3. Agar data mil gaya, toh save_to_file function ko call karein ge
    if scraped_data:
        print(f"Success! Total {len(scraped_data)} cars data reterived.")
        
        filename = f"{car_brand_clean}_prices.csv"
        save_to_file(scraped_data, filename)
    else:
        print("Failed to retrieve car data.")


# create a function to save data to a csv file
def save_to_file(data, filename):
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data saved to {filename}")