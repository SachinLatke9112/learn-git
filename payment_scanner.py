import qrcode

# upi id from user 
upi_id = input("Enter the Upi_ID :") # Upi id as input

# upi://pay?pa=upi_id&pn=Name&am=Amount&cu=Currency&tn=Message

# payment url based on upi id 
phonepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
Paytem_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
Goggle_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#  creating QR codes
phonepay_qr = qrcode.make(phonepay_url)
paytem_qr = qrcode.make(Paytem_url)
googlePay_qr = qrcode.make(Goggle_pay_url)

# saves the QR code
phonepay_qr.save("phonepay_qr.png")
paytem_qr.save("paytem_qr.png")
googlePay_qr.save("Goggle_pay_url.png")

# Display the qr code 
phonepay_qr.show()
paytem_qr.show()
googlePay_qr.show