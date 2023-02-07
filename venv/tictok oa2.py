
import networkx as nx

def match_orders(send_orders, pickup_orders):
    G = nx.Graph()
    # Adding nodes for send orders
    for order in send_orders:
        order_id, car_type, book_time, airport_name = order.split(",")
        G.add_node(order_id, type='send', car_type=car_type, book_time=book_time, airport_name=airport_name)
    # Adding nodes for pickup orders
    for order in pickup_orders:
        order_id, car_type, book_time, airport_name = order.split(",")
        G.add_node(order_id, type='pickup', car_type=car_type, book_time=book_time, airport_name=airport_name)
    # Adding edges between compatible send and pickup ordersn
    for s in G.nodes(data=True):
        for p in G.nodes(data=True):
            if s[1]['type'] == 'send' and p[1]['type'] == 'pickup':
                if s[1]['car_type'] == p[1]['car_type'] and s[1]['airport_name'] == p[1]['airport_name']:
                    if s[1]['book_time'] < p[1]['book_time']:
                        idle_time = (p[1]['book_time'] - s[1]['book_time']).total_seconds()
                        G.add_edge(s[0], p[0], weight=-idle_time)
    # Finding maximum weight matching
    match = nx.max_weight_matching(G, True)
    pair_orders = []
    single_orders = []
    for node in match:
        if match[node] != None:
            pair_orders.append(f"{node}->{match[node]}")
        else:
            single_orders.append(node)
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
print(match_orders(send_orders, pickup_orders))