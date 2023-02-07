'''

5. Airport send and pickup service orders make pairs
Description

One online ride hailing company can fulfil many airport transfer orders every day.
in order to reduce the time and cost without orders, the company pairs pickup and
send orders, if they have the same car type and same airport.
Besides the arrival time of airport send order must be earlier than the send time of
airport pickup order.
Then they will assign the pair orders to one driver.
Question:
How to match the airport send and pickup orders, with the sum of car idle time
minimized?

Tips:
1. This is a maximum weight matching problem.
2. weigh(i,j)=idle duration=the book pickup timestamp of pickup service order - the
book arrival time of send service order

'''
'''
# list item: order_id,car_type,book_time,airport_name
Input:
send_orders=[
"_order1,1,2022-02-11 12:00:00, airporti", 
"S_order2,1,2022-02-11 12:30:00, airporti", 
"_order3,1,2022-02-11 12:10:00,airport1", 
"_order4,2,2022-02-12 12:30:00,airport2", 
"S_order5,2,2022-02-12 18:27:00,airport2",
"_order6,1,2022-02-12 19:30:00, airport2", 
"_order7,2,2022-02-12 20:15:00, airport2",
]
pickup_orders =[
"p_order1,1,2022-02-11 12:20:00, airport1",
"p_order2,2,2022-02-11 14:30:00,airporti",
"p_order3,2,2022-02-12 12:45:00, airport2",
"p_order4,2,2022-02-12 12:15:00, airport2",
"p_order5,2,2022-02-12 19:20:00,airport2",
"p_order6,2,2022-02-12 20:30:00,airport2",
"p_order7,2,2022-02-12 20:00:00, airport2"
]


Output:
pair_orders=[
"s_order3->p_order1',
"s_order4->p_order3',
"s_order5->p_order5",
"s_order6->p_order7",
"s_order7->p_order6",
]

single_orders=[
's_orderl',
's_order2',
'p_order2',
'p_order4'
]
'''
from datetime import datetime
import time
from collections import defaultdict

from munkres import Munkres

def convert(send_orders,pickup_orders):
    m, n = len(send_orders), len(pickup_orders)
    weight = [[-1]* n for _ in range(m)]
    for i, s_order in enumerate(send_orders):
        s_order_id, s_car_type, s_book_time, s_airport_name = s_order.split(",")
        for j, p_order in enumerate(pickup_orders):
            p_order_id, p_car_type, p_book_time, p_airport_name = p_order.split(",")
            start_time= datetime.strptime(p_book_time, '%Y-%m-%d %H:%M:%S')

            end_time = datetime.strptime(s_book_time, '%Y-%m-%d %H:%M:%S') #2022-02-11 12:00:00
            idle = (start_time - end_time).total_seconds()
            if s_car_type == p_car_type and s_airport_name == p_airport_name and idle > 0:
                weight[i][j] = idle

    munkres = Munkres()
    indexes = munkres.compute(weight)
    pair_orders = []
    single_orders = send_orders.copy()
    for i, j in indexes:
        pair_orders.append("s_order" + str(i+1) + "->p_order" + str(j+1))
        single_orders.remove("s_order" + str(i+1))
    single_orders.extend(["p_order" + str(i+1) for i in range(len(pickup_orders)) if i not in [j for i, j in indexes]])
    return pair_orders, single_orders




send_orders=[
"_order1,1,2022-02-11 12:00:00, airporti",
"S_order2,1,2022-02-11 12:30:00, airporti",
"_order3,1,2022-02-11 12:10:00,airport1",
"_order4,2,2022-02-12 12:30:00,airport2",
"S_order5,2,2022-02-12 18:27:00,airport2",
"_order6,1,2022-02-12 19:30:00, airport2",
"_order7,2,2022-02-12 20:15:00, airport2",
]
pickup_orders =[
"p_order1,1,2022-02-11 12:20:00, airport1",
"p_order2,2,2022-02-11 14:30:00,airporti",
"p_order3,2,2022-02-12 12:45:00, airport2",
"p_order4,2,2022-02-12 12:15:00, airport2",
"p_order5,2,2022-02-12 19:20:00,airport2",
"p_order6,2,2022-02-12 20:30:00,airport2",
"p_order7,2,2022-02-12 20:00:00, airport2"
]
print(convert(send_orders, pickup_orders))