from datetime import datetime
import time
from collections import defaultdict
import heapq


def convert(send_orders,pickup_orders):
    m, n = len(send_orders), len(pickup_orders)
    distances = []
    for i, s_order in enumerate(send_orders):
        distances.append([])
        s_order_id, s_car_type, s_book_time, s_airport_name = s_order.split(",")
        for j, p_order in enumerate(pickup_orders):
            p_order_id, p_car_type, p_book_time, p_airport_name = p_order.split(",")
            start_time= datetime.strptime(p_book_time, '%Y-%m-%d %H:%M:%S')

            end_time = datetime.strptime(s_book_time, '%Y-%m-%d %H:%M:%S') #2022-02-11 12:00:00
            idle = (start_time - end_time).total_seconds()
            if s_car_type == p_car_type and s_airport_name == p_airport_name and idle > 0:
                distances[-1].append((idle, i, j))
            else:
                distances[-1].append((float('inf'), i, j))
        distances[-1].sort(reverse=True)


    res = [None] * m
    used_bikes = set()
    dist = [distances[i].pop() for i in range(m)]  # smallest distance for each worker
    heapq.heapify(dist)

    while len(used_bikes) < m:
        d, worker, bike = heapq.heappop(dist)
        if bike not in used_bikes:
            if d != float('inf'):
                res[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(dist, distances[worker].pop())  # bike used, add next closest bike

    return res


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