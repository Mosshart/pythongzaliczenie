from locust import HttpUser, task
import random

class LocustTests(HttpUser):

    @task
    def NumberTests(self):
       # a = random.randrange(9223372036854775807)
        self.client.get(url='number/9223372036854775807')

    @task(1)
    def post_img(self):
         in_file = open('Zolta.jpg', 'rb')
         data = in_file.read()
         self.client.post(url="ImageColorInvert", files={'img': data})

    @task(2)
    def AuthTest(self):
        #https://pythongzaliczenie.herokuapp.com/auth/{creditnails}?login=test&password=test'
        self.client.get(url='auth/{creditnails}?login=test&password=test')


