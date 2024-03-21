def validate_credit_card(number):
  # Reverse the credit card number and convert to integers
  digits = [int(d) for d in str(number)[::-1]]

  # Multiply every other digit by 2 and sum them with the rest
  checksum = sum(d if i % 2 == 0 else d*2 if d < 5 else d*2 - 9 
                 for i, d in enumerate(digits))

  # Check if the card is valid according to Luhn's algorithm
  is_valid = checksum % 10 == 0

  # Determine the card type
  card_type = "INVALID"
  if is_valid:
      if (number.startswith('34') or number.startswith('37')) and len(number) == 15:
          card_type = "American Express"
      elif any(number.startswith(str(i)) for i in range(51, 56)) and len(number) == 16:
          card_type = "MasterCard"
      elif number.startswith('4') and len(number) in (13, 16):
          card_type = "Visa"

  return is_valid, card_type

# Prompt the user for a credit card number
card_number = input("Enter a credit card number: ").strip()

# Validate the card number and determine its type
valid, card_type = validate_credit_card(card_number)

# Print the result
if valid:
  print(f"{card_number}: {card_type}")
else:
  print(f"{card_number}: INVALID")


