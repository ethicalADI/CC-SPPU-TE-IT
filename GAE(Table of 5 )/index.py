import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Multiplication Table of 5:<br>")
        for i in range(1, 11):
            result = 5 * i
            self.response.write(f"5 x {i} = {result}<br>")

app = webapp2.WSGIApplication([ ('/', MainHandler)], debug=True)
