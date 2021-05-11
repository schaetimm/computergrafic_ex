
# from 3dvectors.arecontent import*
# from 3dvectors.intersection import*
from blabla.ray_tri_intersect import*
def main():
    #print(intersection((6, 8, 4), (6, 7, 0), (6, 8, 2), (6, 7, 4)))
    #print(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,0,0), (-1,2,0), (2,0,1)))
    """print('(', "{:.3f}".format(ray_tri_intersect((0, 0, -1), (0, 0, 1), (-0.5, 0, 0), (-1, 2, 0), (2, 0, 1))[0]), ', ',
          "{:.3f}".format(ray_tri_intersect((0, 0, -1), (0, 0, 1), (-0.5, 0, 0), (-1, 2, 0), (2, 0, 1))[1]), ', ',
          "{:.3f}".format(ray_tri_intersect((0, 0, -1), (0, 0, 1), (-0.5, 0, 0), (-1, 2, 0), (2, 0, 1))[2]), ')', sep='')
    print(ray_tri_intersect((0, 0, -1), (0, 0, 1), (-3, 0, 0), (-1, 0, 0), (-2, 0, 0)))"""
    # print(ray_tri_intersect((0, 0, -1), (0, 0, 1), (-3, 1, 0), (-1, 2, 0), (-2, 2, 0)))
    print('(', "{:.3f}".format(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,0,0), (-1,2,0), (2,0,1))[0]), ', ', \
    "{:.3f}".format(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,0,0), (-1,2,0), (2,0,1))[1]), ', ', \
    "{:.3f}".format(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,0,0), (-1,2,0), (2,0,1))[2]), ')', sep='')

    print(ray_tri_intersect((0,0,-1),(0,0,1),(-3,0,0),(-1,0,0),(-2,0,0)))

    print(ray_tri_intersect((0,0,-1),(0,0,1),(-3,1,0),(-1,2,0),(-2,2,0)))

    print('(', "{:.3f}".format(ray_tri_intersect((1,1,1), (-1,-1,-1), (1,0,0), (0,1,0), (0,0,1))[0]), ', ', \
    "{:.3f}".format(ray_tri_intersect((1,1,1), (-1,-1,-1), (1,0,0), (0,1,0), (0,0,1))[1]), ', ', \
    "{:.3f}".format(ray_tri_intersect((1,1,1), (-1,-1,-1), (1,0,0), (0,1,0), (0,0,1))[2]), ')', sep='')

    print(ray_tri_intersect((0,0,-1),(0,0,1),(-3,0,0),(-1,0,0),(-2,0,0)))

    print(ray_tri_intersect((0,0,-1),(0,0,1),(-3,0,0),(1,0,0),(-2,0,-3)))

    print('(', "{:.3f}".format(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,1,0.5), (1,2,1), (2,-4,1))[0]), ', ', \
    "{:.3f}".format(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,1,0.5), (1,2,1), (2,-4,1))[1]), ', ', \
    "{:.3f}".format(ray_tri_intersect((0,0,-1), (0,0,1), (-0.5,1,0.5), (1,2,1), (2,-4,1))[2]), ')', sep='')

    print(ray_tri_intersect((0,0,-1),(0,0,1),(-3,2-1),(-1,2,1),(-2,4,1)))

    print(ray_tri_intersect((0,-1),(0,0,1),(-3,2,0),(-1,2,1),(0,0,0)))

    print(ray_tri_intersect((0,0,-1),(0,0,0),(-3,2,0),(-1,2,1),(0,0,0)))

    try:
        ray_tri_intersect((0, 0, -1), (0, 0, 1), (-3, 2, 1), (-1, 2, 1))
    except TypeError:
        print(None)


if __name__ == "__main__":
    main()
