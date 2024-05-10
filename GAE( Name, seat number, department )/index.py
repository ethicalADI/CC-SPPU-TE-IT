import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        name = "Your Name"
        seat_number = "Your Seat Number"
        department = "Your Department"

        for _ in range(5):
            self.response.write(f"Name: {name}<br>")
            self.response.write(f"Seat Number: {seat_number}<br>")
            self.response.write(f"Department: {department}<br>")
            self.response.write("<br>")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
