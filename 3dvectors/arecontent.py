def area (a,  b,  c):
    if (type(a) == tuple or type(a) == list) and (len(a) == 3) \
            and (type(b) == tuple or type(b) == list) and (len(b) == 3)\
            and (type(c) == tuple or type(c) == list) and (len(c) == 3):


        ab_1 = (b[0] - a[0])
        ab_2 = (b[1] - a[1])
        ab_3 = (b[2] - a[2])
        bc_1 = (c[0] - b[0])
        bc_2 = (c[1] - b[1])
        bc_3 = (c[2] - b[2])
        ab = (ab_1, ab_2, ab_3)
        bc = (bc_1, bc_2, bc_3)
        kreuzprodukt = [


        ab [1] * bc[2] - ab[2] * bc[1], ab[2] * bc[0] - ab[0] * bc[2],
        ab [0] * bc[1] - ab[1] * bc[0]
        ]
        kreuzprodukt_1 = (kreuzprodukt[0]) ** 2
        kreuzprodukt_2 = (kreuzprodukt[1]) ** 2
        kreuzprodukt_3 = (kreuzprodukt[2]) ** 2

        area = kreuzprodukt_1 + kreuzprodukt_2 + kreuzprodukt_3
        area **= (0.5)
        area = area *(1/2)
        return area
    else:
        return None





