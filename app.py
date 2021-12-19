from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse

app=Flask(__name__)
# app.debug=True
api = Api(app)

class Total_Cost(Resource):
	def get(self):
		return "The API will take as input items ordered, delivery distance, and offer applied. The response is the total order value. Use POST method to send data."
	
	def computeTotalCost(self, items):
		res = 0
		for item in items:
			res += (item["quantity"]*item["price"])
		return res

	def computeDeliverFee(self, distance):
		"""
		The delivery cost slab is(the upper limits are inclusive):
		0 to 10km: 50 INR
		10 to 30km: 100 INR
		30 to 100km: 500 INR
		100 to 500km: 2000 INR
		"""
		deliverSlab = {10: 50, 30: 100, 100: 500, 500: 2000}
		for u,val in deliverSlab.items():
			# check if distance less than or equal to upper limit in meters
			if distance <= (u*1000):
				# return applicable rate in paisa
				return val*100

	def post(self):
		parser = reqparse.RequestParser()

		parser.add_argument("order_items", required=True, type=dict, action="append", help="order_items parameter is required")
		parser.add_argument("distance", type = int, help="Delivery distance(integer in meters) is required", required=True)
		parser.add_argument("offer", type = dict, action="append")

		args = parser.parse_args()
		# args is a dictionary

		# compute order total
		ot = args["order_items"]
		# check if multiple items exist or just single item
		if(type(ot) == list):
			total = self.computeTotalCost(ot)
		else:
			total = self.computeTotalCost([ot])

		# compute delivery fee (if any)
		dfee = self.computeDeliverFee(args["distance"])

		# compute offers if any
		if type(args["offer"]) == list:
			offers = args["offer"]
		elif type(args["offer"]) == dict:
			offers = [args["offer"]]
		else:
			# in case no offers available, early return
			return jsonify({"order_total": total+dfee})
		
		offer_price = 0
		for offer in offers:
			# print(offer)
			if offer["offer_type"] == "DELIVERY":
				dfee = 0
			if offer["offer_type"] == "FLAT":
				offer_price = offer["offer_val"]

		# compute net price
		total += dfee
		total -= min(offer_price,total)
		return jsonify({"order_total": total})

api.add_resource(Total_Cost,"/")

if __name__=="__main__":
    app.run()