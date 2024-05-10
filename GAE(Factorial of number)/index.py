import webapp2

class FactorialHandler(webapp2.RequestHandler):
    def get(self):
        number = self.request.get('number')
        factorial = self.calculate_factorial(int(number))
        self.response.write(f"The factorial of {number} is {factorial}")

    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

app = webapp2.WSGIApplication([('/', FactorialHandler)], debug=True)
