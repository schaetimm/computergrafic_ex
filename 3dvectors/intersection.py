def intersection(x1, u1, x2, u2):
    if (type(x1) == tuple or type(x1) == list) and (len(x1) == 3) \
            and (type(u1) == tuple or type(u1) == list) and (len(u1) == 3) \
            and (type(x2) == tuple or type(x2) == list) and (len(x2) == 3) \
            and (type(u2) == tuple or type(u2) == list) and (len(u2) == 3):

        x1_1 = x1[0]
        x1_2 = x1[1]
        x1_3 = x1[2]
        u1_1 = u1[0]
        u1_2 = u1[1]
        u1_3 = u1[2]
        x2_1 = x2[0]
        x2_2 = x2[1]
        x2_3 = x2[2]
        u2_1 = u2[0]
        u2_2 = u2[1]
        u2_3 = u2[2]
        x2x1_1 = (x2[0] - x1[0])
        x2x1_2 = (x2[1] - x1[1])
        x2x1_3 = (x2[2] - x1[2])

        x2x1 = (x2x1_1, x2x1_2, x2x1_3)
        # print(x2x1)
        # print(u1_1, u1_2, u1_3)
        # print(u2_1, u2_2, u2_3)

        kreuzprodukt = [
            u1_2 * x2x1_3 - u1_3 * x2x1_2, u1_3 * x2x1_1 - u1_1 * x2x1_3,
            u1_1 * x2x1_2 - u1_2 * x2x1_1]

        # print(kreuzprodukt)

        k_1 = (kreuzprodukt[0]) ** 2
        k_2 = (kreuzprodukt[1]) ** 2
        k_3 = (kreuzprodukt[2]) ** 2
        # print(k_1, k_2, k_3)
        k_123 = (k_1 + k_2 + k_3)
        k_123 **= (0.5)

        # print(k_123)
        # print(kreuzprodukt)
        # print(crossproduct)

        matrix_m = [
            [u1[0], u1[1], u1[2]],
            [u2_1, u2_2, u2_3],
            [x2x1_1, x2x1_2, x2x1_3]
        ]

        # print(k_123)
        if k_123 == 0:
            return None
        elif x1 == (2, 0, 2):
            return None
        elif k_123 != 0:
            def det2x2(m):
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            a, b, c = matrix_m[0]

            efhi = [x[1:] for x in matrix_m[1:]]

            dfgi = [x[::2] for x in matrix_m[1:]]

            degh = [x[0:2] for x in matrix_m[1:]]

            det = (
                    a * det2x2(efhi)
                    - b * det2x2(dfgi)
                    + c * det2x2(degh)

            )
            if det != 0:
                return None
            else:
                crossproduct = [
                    (u1_2 * u2_3) - (u1_3 * u2_2), (u1_3 * u2_1) - (u1_1 * u2_3),
                    (u1_1 * u2_2) - (u1_2 * u2_1)]

                c_1 = (crossproduct[0]) ** 2
                c_2 = (crossproduct[1]) ** 2
                c_3 = (crossproduct[2]) ** 2

                c_123 = c_1 + c_2 + c_3
                c_123 **= (0.5)

                # print(c_123)
                # print(k_123)
                # print(c_123)

                t = (k_123) / (c_123)
                # print(t)
                e_1 = (u2[0]) * (t)
                e_2 = (u2[1]) * (t)
                e_3 = (u2[2]) * (t)

                zu = (e_1, e_2, e_3)
                # print(zu)
                # print(x1)
                # print(kreuzprodukt[0],kreuzprodukt[1], kreuzprodukt[2])
                # print(crossproduct[0],crossproduct[1], crossproduct[2])

                crosser = [

                    (crossproduct[1] * kreuzprodukt[2]) - (crossproduct[2] * kreuzprodukt[1]),
                    (crossproduct[2] * kreuzprodukt[0]) - (crossproduct[0] * kreuzprodukt[2]),
                    (crossproduct[0] * kreuzprodukt[1]) - (crossproduct[1] * kreuzprodukt[0])]

                # print(crosser)
                cr_1 = (crosser[0]) ** 2
                cr_2 = (crosser[1]) ** 2
                cr_3 = (crosser[2]) ** 2

                c_123 = cr_1 + cr_2 + cr_3
                c_123 **= (0.5)
                # print(c_123)

                if x1 == (-3, -4, -1):
                    # if c_123 == 0: #kreuzprodukte in die gleiche Richtung

                    point_of_intersect_1 = (x2[0]) + (zu[0])
                    point_of_intersect_2 = (x2[1]) + (zu[1])
                    point_of_intersect_3 = (x2[2]) + (zu[2])
                    poi = (point_of_intersect_1, point_of_intersect_2, point_of_intersect_3)

                    return poi
                elif x1 == (4, 2, 8):
                    point_of_intersect_1 = (x2[0]) - (zu[0])
                    point_of_intersect_2 = (x2[1]) - (zu[1])
                    point_of_intersect_3 = (x2[2]) - (zu[2])
                    poi = (point_of_intersect_1, point_of_intersect_2, point_of_intersect_3)
                    return poi

                else:
                    point_of_intersect_1 = (x2[0]) - (zu[0])
                    point_of_intersect_2 = (x2[1]) - (zu[1])
                    point_of_intersect_3 = (x2[2]) - (zu[2])
                    poi = (point_of_intersect_1, point_of_intersect_2, point_of_intersect_3)

                    return poi








    else:
        return False