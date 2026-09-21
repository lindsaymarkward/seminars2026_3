"""..."""
GST_RATE = 0.1

item_price = float(input("Price: "))
gst_response = input("GST: ")
if gst_response == "yes":
    item_price *= (1 + GST_RATE)
print(f"${item_price:.2f}")
