import smtplib
import datetime as dt
import random

# Step 1: Get the current day of the week
now = dt.datetime.now()

# Step 2: Read the quotes from 'quotes.txt'
try:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()  # Get all the quotes as a list of lines
except FileNotFoundError:
    print("The file 'quotes.txt' was not found.")
    quotes = []

# Step 3: Choose a random quote if quotes are available
if quotes:
    quote = random.choice(quotes).strip()  # Choose a random quote and strip any extra whitespace

    # Step 4: Send the quote via email using SMTP
    my_email = "jackson88programming@gmail.com"  # Replace with your email
    password = "hkzq iufv kjyr gonp"  # Use an App Password or your email password

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=password)  # Log in to your email account
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,  # You can change this to the recipient's email address
                msg=f"Subject:Motivational Quote\n\n{quote}"  # Subject and body of the email
            )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send the email: {e}")
else:
    print("No quotes to send.")
