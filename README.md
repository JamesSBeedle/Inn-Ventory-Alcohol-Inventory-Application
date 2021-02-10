# Inn_Ventory_Individual_Project

User Instructions

First clone the files:

Click on the green Code button, select SSH and copy the link provided.

Once you have the link open terminal, select the directory you wish to clone the files to and type git clone pasting in the link. 

Hit enter and the files will have been cloned to your machine in the directory you selected.



While still in the Inn_Ventory_Individual_Project in terminal run the following commands:

1. psql -d inn_ventory -f db/in_ventory.sql   (this will set up the database for the app to function)

2.  python3 console.py (this will populate the tables with the dummy information used to test the app is working)

3. flask run (this will allow the app to run in your browser)

4. Copy the url you see on your terminal found on line beginning  Running on.....

5. Paste the url into your browser.

6. Check the buttons and links work and that information is displayed correctly.

7. To remove the dummy information from the app first go back to terminal and exit flask by entering ^c (control+c) then follow step 1 followed by step 3. This will leave the database empty of the information console.py placed in there and will now be ready for you to add your own information into the app.






The Brief

The Brief given for this app is shown below: 

Shop Inventory
Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.




MVP
The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
The inventory should track manufacturers, including a name and any other appropriate details.
The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
Show an inventory page, listing all the details for all the products in stock in a single view.
As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Inspired by
eBay, Amazon (back end only), Magento





Technologies Used

HTML

Python3

Jinja

CSS

SQL

Psycopg2

Flask

Git

Github

draw.io

Visual Studio Code
