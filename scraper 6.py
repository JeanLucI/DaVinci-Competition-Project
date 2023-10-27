#
# For this to run properly, we need to go to https://www.retailmenot.com/ca 
# and download it, since making a request through requests.get(url) doesn't 
# seem to work other than sending 403 error.

# The only thing this scraper does is scrape the following in dicctionaries.
# The image url of the company image
# The company name
# The description of the discount
# Ideally if there is a coupon code (TRUE or FALSE) it redirects you directly 
# to the website(Redirect Link) otherwise it takes you to the actual discount 
# coupon.

#


from bs4 import BeautifulSoup
import requests

with open("RetailMeNot Canada_ Save with Coupons & Promo Codes.html", "r") as f:
    soup = BeautifulSoup(f, 'html.parser')
    
# Initialize a list to store dictionaries for each <li> element
results = []

# Find all <li> elements with class 'relative flex h-32 flex-col md:h-auto'
items = soup.find_all('li', class_='relative flex h-32 flex-col md:h-auto')

# Loop through each <li> element and extract the required information
for item in items:
    # Extract the image source URL
    image_src = item.find('img')['src']
    # Modify image_src to use the desired format
    image_src = image_src.replace('./RetailMeNot Canada_ Save with Coupons & Promo Codes_files/', 'https://www.retailmenot.com/imagery/merchants/')
    
    company_name = item.find('h3').text
    description = item.find('p', class_='line-clamp-2').text
    coupon_code_exists = True if item.find('p', text='coupon code') else False
    
    # Get the 'href' attribute value if it exists, otherwise set hyper_code to None
    href_attr = item.find('a')['href']
    hyper_code = href_attr[34:34+26]
    
    redirect_link = href_attr
    discount_code_link = f'https://www.retailmenot.com/ca?u={hyper_code}' if hyper_code else None

    # Create a dictionary for the current item
    item_dict = {
        "image_src": image_src,
        "company_name": company_name,
        "description": description,
        "coupon_code_exists": coupon_code_exists,
        "hyper_code": hyper_code,
        "redirect_link": redirect_link,
        "discount_code_link": discount_code_link
    }

    # Add the dictionary to the results list
    results.append(item_dict)


# Loop through the results list and print out the information for each item
print("-" * 50)
for item in results:
    print("Image Source:", item["image_src"])
    print("Company Name:", item["company_name"])
    print("Description:", item["description"])
    print("Coupon Code Exists:", item["coupon_code_exists"])
    print("Hyper Code:", item["hyper_code"])
    print("Redirect Link:", item["redirect_link"])
    print("Discount Code Link:", item["discount_code_link"])
    print("-" * 50)  # Add a separator for clarity

print(results)