from payment_behavior import PaymentBehavior

class PaymentCard(PaymentBehavior):
	def pay():
		print("Paying with card")

		sale = input("enter total in sale")
		cardNumber = input("enter card number")

		print("purchase successful")

		return True