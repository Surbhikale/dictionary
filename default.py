# spy_name = 'Bond'
# spy_salutation = 'Mr.'
# spy_age = 21
# spy_rating = 4.5

# from test import Name ,Class
# print (Name,Class)

# spy = {'name' : 'Bond',
#         'salutation' : 'Mr.',
#        'age' : 23,
#        'rating' : 4.5,
#        'Online Status' : True
#       }


class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online_status = True
        self.current_status_msg = None

spy = Spy("Bond" , "Mr." , 25, 4.3)

friend_1 = Spy("surbhi" , "Ms." , 21, 3.0)
friend_2 = Spy("neha" , "Ms." , 19, 4.4)
friend_3 = Spy("Roy" , "Mr." , 45, 4.1)

friend = [friend_1,friend_2,friend_3]
