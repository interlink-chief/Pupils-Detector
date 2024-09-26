import matplotlib.pyplot as plt


class FigureModule:
    def __init__(self, marker='o', color='blue'):
        self.marker = marker
        self.color = color

        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Time')

    def plot_point(self, x, y, z):
        self.ax.scatter(x, y, z, marker=self.marker, color=self.color)

    def show_figure(self):
        # plt.draw()
        # plt.pause(0.001)
        plt.show()

