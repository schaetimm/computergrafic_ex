def li_pt_distance(x, u, p):
    if (type(x) == tuple or type(x) == list) and (len(x) == 3) \
            and (type(u) == tuple or type(u) == list) and (len(u) == 3) \
            and (type(p) == tuple or type(p) == list) and (len(p) == 3):

        pu_1 = (p[0] - x[0])
        pu_2 = (p[1] - x[1])
        pu_3 = (p[2] - x[2])
        pu = (pu_1, pu_2, pu_3)
        # print(pu)

        crossproduct = [
            (u[1] * pu[2]) - (u[2] * pu[1]), (u[2] * pu[0]) - (u[0] * pu[2]),
            (u[0] * pu[1]) - (u[1] * pu[0])]
        # print(crossproduct)
        c_1 = (crossproduct[0]) ** 2
        c_2 = (crossproduct[1]) ** 2
        c_3 = (crossproduct[2]) ** 2

        c_123 = c_1 + c_2 + c_3
        c_123 **= (0.5)
        # print(c_123)

        u_1 = (u[0]) ** 2
        u_2 = (u[1]) ** 2
        u_3 = (u[2]) ** 2

        u_123 = u_1 + u_2 + u_3
        u_123 **= (0.5)
        # print(u_123)

        if u_123 != 0:

            t = (c_123) / (u_123)
            return t
        else:
             return None





    else:
        return None    