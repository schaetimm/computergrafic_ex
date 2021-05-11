def ray_tri_intersect(o, d, v0, v1, v2):
    if (type(o) == tuple or type(o) == list) and (len(o) == 3) \
            and (type(d) == tuple or type(d) == list) and (len(d) == 3) \
            and (type(v0) == tuple or type(v0) == list) and (len(v0) == 3) \
            and (type(v1) == tuple or type(v1) == list) and (len(v1) == 3) \
            and (type(v2) == tuple or type(v2) == list) and (len(v2) == 3):

        ab_1 = (v1[0] - v0[0])
        ab_2 = (v1[1] - v0[1])
        ab_3 = (v1[2] - v0[2])
        e1 = (ab_1, ab_2, ab_3)
        # print("E1 ist",e1)
        bc_1 = (v2[0] - v0[0])
        bc_2 = (v2[1] - v0[1])
        bc_3 = (v2[2] - v0[2])
        e2 = (bc_1, bc_2, bc_3)
        # print("E2 ist", e2)
        t_1 = (o[0] - v0[0])
        t_2 = (o[1] - v0[1])
        t_3 = (o[2] - v0[2])
        t = (t_1, t_2, t_3)
        # print(" T ist", t)
        p = [
             d[1] * e2[2] - d[2] * e2[1], d[2] * e2[0] - d[0] * e2[2],
             d[0] * e2[1] - d[1] * e2[0]
             ]
        # print("kreuzprodukt P ist", p)
        q = [
            t[1] * e1[2] - t[2] * e1[1], t[2] * e1[0] - t[0] * e1[2],
            t[0] * e1[1] - t[1] * e1[0]
        ]
        # print(q)

        skalar_p_e1 = (
            (p[0] * e1[0]) + (p[1] * e1[1]) + (p[2] * e1[2])
        )
        skalar_q_e2 = (
            (q[0] * e2[0]) + (q[1] * e2[1]) + (q[2] * e2[2])

        )
        skalar_p_t = (
                (p[0] * t[0]) + (p[1] * t[1]) + (p[2] * t[2])

        )
        skalar_q_d = (
                (q[0] * d[0]) + (q[1] * d[1]) + (q[2] * d[2])

        )
        if skalar_p_e1 < 0.0000001:
            return None
        # print(skalar_p_e1)
        # print(skalar_q_e2)
        if (skalar_p_e1) or (skalar_q_e2) or (skalar_p_t) or (skalar_q_d) != 0:
            small_t = (1 / skalar_p_e1) * (skalar_q_e2)
            # print(small_t)
            small_u = (1 / skalar_p_e1) * (skalar_p_t)
            # print(small_u)
            small_v = (1 / skalar_p_e1) * (skalar_q_d)
            # print(small_v)
            small_z_1 = o[0] + (small_t * d[0])
            small_z_2 = o[1] + (small_t * d[1])
            small_z_3 = o[2] + (small_t * d[2])
            small_z = (small_z_1, small_z_2, small_z_3)

            return small_z
        else:
            return None






























    else:
        return None
