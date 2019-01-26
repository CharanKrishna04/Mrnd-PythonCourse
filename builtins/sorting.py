"""
You are required to write a program to sort the (name, age, height) tuples.
Sort them by ascending order where name is string, age and height are numbers. 

The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.


Input - [('Tom','19','80'),('John','20','90'),('Jony','17','91'),('Jony','17','93'),('Json','21','85') ]

Output - [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""

def sorting(data):

    data=sorted(data,key=lambda a:int(a[2]))
    data = sorted(data, key=lambda a: int(a[1]))
    data = sorted(data, key=lambda a: a[0])
    return data

def test_sorting():
    assert [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')] == sorting([('Tom','19','80'),('John','20','90'),('Jony','17','91'),('Jony','17','93'),('Json','21','85') ])
