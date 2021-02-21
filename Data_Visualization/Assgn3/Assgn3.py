import matplotlib.pyplot as plt
def create_circle():
    circle= plt.Circle((0,0), radius= 5)
    return circle
def show_shape(patch):
    ax=plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()
c= create_circle()
show_shape(c)