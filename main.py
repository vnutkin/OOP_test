class Task:
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status
    def done(self):
        self.status = 'done'
    def add_task(self,list):
        list.append(self)
    def in_work(self,list):
        for elem in list:
            if elem.status != 'done':
                print(f'In progress {elem.description}, deadline {elem.deadline}')
tasks = []
t1 = Task(description='To do home work #1',deadline='01.12.24',status='plan')
tasks.append(t1)
tasks.append(Task(description='To do home work #2',deadline='10.12.24',status='plan'))
tasks.append(Task(description='To do home work #3',deadline='20.12.24',status='plan'))
t1.in_work(tasks)
t1.done()
t1.in_work(tasks)
#appendix
class Store:
    def __init__(self,name,adress,items):
        self.name = name
        self.adress = adress
        self.items = items
    def add_item(self,item,price):
        self.items[item] = price
    def del_item(self,item):
        self.items.pop(item)
    def get_price(self,item):
        return self.items.get(item)
    def set_price(self,item,prise):
        self.items[item] = prise
store1 = Store('Fruits','Wallstrit, 10',{})
store1.add_item('apple',5)
store1.add_item('banana',10)
store1.add_item('orange',12)
store2 = Store('Vegetables','Main road,212',{'onion':2,'cabbidge':5,'potato':3})
store3 = Store('Cloth','Riversaid drive, 103',{'t-short':20,'short':25,'pants':30})
store1.add_item('strawberry',20)
print(store1.get_price('banana'))
store1.set_price('banana',15)
print(store1.get_price('banana'))
store1.del_item('banana')
print(store1.get_price('banana'))
print(store2.get_price('onion'))