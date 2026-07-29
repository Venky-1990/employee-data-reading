import json
import requests
import os
import logging
url="https://jsonplaceholder.typicode.com/users"
cache="users.json"

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
    )
logging.info(f"fetching data from URL",{"https://jsonplaceholder.typicode.com/users"})
logging.info(f"User searched: {user_id}")
logging.info("Address displayed")
logging.info("Program Closed")
def fetch_user():
    if os.path.exists(cache):
        with open (cache,"r") as file:
            return json.load (file)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        users = response.json()

        with open(cache, "w") as file:
            json.dump(users, file, indent=4)

        return users

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def get_user(users,user_id):
    for user in users:
        if user["id"]==user_id:
            print("User details")
            print("username:",user["username"])
            print("email:",user["email"])        
            address_check=input("want to view address details? (yes/no): ")
            if address_check == "yes":
                address = user["address"]
                print("Address Details")
                print("Street :", address["street"])
                print("Suite  :", address["suite"])
                print("City   :", address["city"])
                print("Zipcode:", address["zipcode"])
            logging.info(f"User ID {user_id} viewed.")
            return
                
    return
users=fetch_user()
print("users:", users)
user_id=int(input("Enter user ID:"))
get_user(users, user_id)
continue_search = "yes"

while continue_search == "yes":
    try:
        user_id = int(input("\nEnter User ID: "))
        get_user(users, user_id)

        continue_search = input("\nDo you want to search another user? (yes/no): ").lower()

    except ValueError:
        print("Please enter a valid numeric User ID.")

print("Thank you! Exiting program.")
