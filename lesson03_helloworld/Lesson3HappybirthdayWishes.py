print("*****Welcome to Birthday Card Generator***** ")

recipientName = input("--Recipient's name:")
date_of_birth = int(input("--Year of birth:"))
message = input("--Personalized message:")
senderName = input("--Sender's name:")
"""
[Recipient's Name], let's celebrate your [Age] years of awesomeness!
Wishing you a day filled with joy and laughter as you turn [Age]!

[Short Personalized Message]

With love and best wishes,
[Sender's Name]
"""
print(f"{recipientName}, let's celebrate your {(2024 - date_of_birth)} years of awesomeness!\n"
      f"Wishing you a day filled with joy and laughter as you turn {(2024 - date_of_birth)}!\n"
      f"{message}/n"
      f"With love and best wishes,\n"
      f"{senderName}")