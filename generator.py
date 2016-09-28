import numpy as np
import mayavi.mlab as mlab
import  moviepy.editor as mpy
import matplotlib.pyplot as plt
from moviepy.video.io.bindings import mplfig_to_npimage
import random
import os


MIN_CYCLE = 15
MAX_CYCLE = 60
FRAME_LENGTH = 3000





def gradient_chart(duration):



	# MAKE A FIGURE WITH MAYAVI
	bg_B = random.uniform(0,1)
	bg_G = random.uniform(0,1)
	bg_R = random.uniform(0,1)

	fig_myv = mlab.figure(size=(250,250), bgcolor=(bg_B,bg_G,bg_R))
	X, Y = np.linspace(-2,2,200), np.linspace(-2,2,200)
	XX, YY = np.meshgrid(X,Y)

	MAX_PARAMETER = 5
	MIN_PARAMETER = 1


	X_parameter = random.uniform(MIN_PARAMETER, MAX_PARAMETER)
	Y_paeameter = random.uniform(MIN_PARAMETER, MAX_PARAMETER)

	sin_flag = random.randint(0,1)
	if sin_flag:
		ZZ = lambda d: np.sinc(XX**X_parameter +YY**Y_paeameter)+np.sin(XX+d)
	else:
		ZZ = lambda d: np.sinc(XX**X_parameter +YY**Y_paeameter)+np.cos(XX+d)

	# ANIMATE THE FIGURE WITH MOVIEPY, WRITE AN ANIMATED GIF

	def make_frame(t):
	    mlab.clf() # clear the figure (to reset the colors)
	    mlab.mesh(YY,XX, ZZ(2*np.pi*t/duration), figure=fig_myv)
	    return mlab.screenshot(antialiased=True)
	return make_frame

#animation = mpy.VideoClip(make_frame, duration=duration)



def matplot_line_chart(duration):

	MAX_PARAMETER = 1
	MIN_PARAMETER = 0.1

	Y_paeameter = random.uniform(MIN_PARAMETER, MAX_PARAMETER)



	fig_mpl, ax = plt.subplots(1,figsize=(5,3), facecolor='white')
	xx = np.linspace(-2,2,200) # the x vector

	sin_flag = random.randint(0,1)
	if sin_flag:
		zz = lambda d: np.sinc(xx**Y_paeameter)+np.sin(xx+d) # the (changing) z vector
	else:
		zz = lambda d: np.sinc(xx**Y_paeameter)+np.cos(xx+d) # the (changing) z vector

	#ax.set_title("Elevation in y=0")
	#ax.set_ylim(-1.5,2.5)
	line, = ax.plot(xx, zz(0), lw=20)

	# ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.

	def make_frame_mpl(t):
	    line.set_ydata( zz(2*np.pi*t/duration))  # <= Update the curve
	    return mplfig_to_npimage(fig_mpl) # RGB image of the figure


	return make_frame_mpl



iterations = 2
for i in range(iterations):


	cycle = random.randint(MIN_CYCLE, MAX_CYCLE)
	
	print("The cycle is {}".format(cycle))


	render_function = matplot_line_chart(cycle)
	#render_function = gradient_chart(cycle)

	animation =mpy.VideoClip(render_function, duration=cycle)

	output_directory = "./images/{}".format(i)
	if not os.path.exists(output_directory):
	    os.makedirs(output_directory)

	for t in range(1,FRAME_LENGTH):

		animation.save_frame(output_directory + "/i_{}.png".format(t), t=t)



#animation.write_gif("sinc.gif", fps=20)