
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi, degrees, radians
st.title("Mohr's Circle Demonstrator")
st.write("By Ali Chaudhry, University of Waterloo")
st.write("Candidate for BASc. in Civil Engineering")
st.write("")



st.write("This webapp is to graphically illustrate the fundamentals of Mohr's circle "
         "including the determination of the maximum shear stress, the origin of  "
         "(pole), and both major and minor principle stresses.")

st.sidebar.header("Input Parameters: ")
#sigx = st.sidebar.slider("Input horizontal stress:", value=0, min_value=-500, max_value=500, step=1, key="sig_x")
sigx = float(st.sidebar.text_input('Horizontal Stress: ', value=0))
st.sidebar.write("$\sigma_{x}$: ",sigx)
#sigz = st.sidebar.slider("Input vertical stress:", value=0, min_value=-500, max_value=500, key="sig_y")
sigz = float(st.sidebar.text_input("Vertical Stress: ", value=0))
st.sidebar.write("$\sigma_{z}$: ", sigz)



#taoxz = st.sidebar.slider("Input shear stress:", value=0, min_value=-500, max_value=500, key="tao_xz")
taoxz = float(st.sidebar.text_input('Shear Stress: ', value=0))
st.sidebar.write(r'$\tau_{xz}$', taoxz)

#theta = st.sidebar.slider("Input inclination:", value=0, min_value=-90, max_value=90, key="theta")
theta = float(st.sidebar.text_input('Inclination: ', value=0))
st.sidebar.write(r'$\theta$:', theta)

response = st.sidebar.button("Clear Entries")

if response:
    sigx = 0
    sigy = 0
    theta = 0
    taoxz = 0

C = (sigx + sigz) / 2
R = ((((sigx - sigz) / 2) ** 2) + taoxz ** 2) ** 0.5

t = np.linspace(0, 2 * np.pi, 100 + 1)
x1 = R * np.cos(t) + C
x2 = R * np.sin(t)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(1)
sig1 = C+R
sig2 = C-R
sigx_prime = C + ((sigx-sigz)/2)*cos(2*radians(theta)) + taoxz*sin(2*radians(theta))
sigz_prime = C - ((sigx-sigz)/2)*cos(2*radians(theta)) - taoxz*sin(2*radians(theta))
tao_prime = -((sigx-sigz)/2)*sin(2*radians(theta)) + taoxz*cos(2*radians(theta))

ax.plot(x1,x2,color='black')
ax.set_aspect(2)
# Major ticks every 20, minor ticks every 5

if sig1 <= 500:
    major_ticks = np.arange(-R, R, 100)
    minor_ticks = np.arange(-150, 150, 10)
elif sig2 > 100 and sigx <=1000:
    major_ticks = np.arange(-1500, 900, 100)
    minor_ticks = np.arange(-1500, 900, 10)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

ax.grid(which='both',linestyle='-')

X1 = np.array([sigx, sigz])
Y1 = np.array([-taoxz, taoxz])

X2 = np.array([sigx_prime,sigz_prime])
Y2 = np.array([-tao_prime,tao_prime])

X3 = np.array([sig2, sig1])
Y3 = [0, 0]

X4 = [C,C]
Y4 = np.array([-R, R])


ax.plot(X4, Y4, color='black')
ax.plot(X3,Y3, color='black')
ax.plot(X1,Y1, color='red')
ax.plot(X2,Y2, color="cyan")
ax.set_aspect(1)
ax.scatter(sigx,-taoxz, color='c', label=r'$\sigma_{x}$')
ax.scatter(sigz,taoxz, color='k', label=r'$\sigma_{z}$')
ax.scatter(sig1,0, color='b', label=r'$\sigma^\prime_{1}$')
ax.scatter(sig2,0, color='r', label=r'$\sigma^\prime_{2}$')
ax.scatter(C,0, color='m', label="Centre")
ax.scatter(sigx_prime,-tao_prime)
ax.scatter(sigz_prime,tao_prime)
ax.axvline(x=sigx, color="b")
ax.axhline(y=taoxz, color="b")

#ax.axhline(y=0, color='k')
#ax.axvline(x=0, color='k')

ax.legend(loc="upper left", prop={"size":6})


plt.xlabel("Normal Stress ($\sigma_{x}$)")
plt.ylabel("Shear Stress ($\\tau_{xz}$)")
plt.title("Mohr's Circle of Stresses")

st.sidebar.title("Properties of Mohr's Circle")
st.sidebar.write("Radius: ", "{:.2f}".format(R))
st.sidebar.write("Centre: ", "{:.2f}".format(C))

st.sidebar.title("Results of Stress Analysis")
st.sidebar.write("Maximum Shear Stress: ", "{:.2f}".format(R))
st.sidebar.write("Major Principle Stress: ", "{:.2f}".format(sig1))
st.sidebar.write("Minor Principle Stress: ", "{:.2f}".format(sig2))
st.sidebar.write("Transformed Lateral Stress: ", "{:.2f}".format(sigx_prime))
st.sidebar.write("Transformed Longitudinal Stress: ", "{:.2f}".format(sigz_prime))
st.sidebar.write("Transformed Shear Stress: ", "{:.2f}".format(tao_prime))

#if sigx > 0 or sigz > 0 :
 #   plt.annotate("σ3",(sig2,0))
  #  plt.annotate("σ1",(sig1,0))
   # plt.annotate("C", (C,0))
    #plt.annotate("τmax", (C,R))
    #plt.annotate("σx",(sigx,-taoxz))
    #plt.annotate("σz", (sigz,taoxz))
    #plt.annotate("σzθ", (sigz_prime,tao_prime))
    #plt.annotate("σxθ", (sigx_prime,-tao_prime))
    #plt.annotate("Pole", (sigx, taoxz))


st.pyplot(fig)

st.title("Why Mohr's Circle?")
st.write("")
st.write("Mohr's circle is a tool which can be applied within many disciplines including"
         " mechanical, civil, materials, structural and geotechnical engineering.  Mohr's circle enables"
         " us to examine the stresses acting on an element of a material at any inclination."
         " As a result, we can find the maximum normal and shear stresses on an element and the plane"
         " on which it acts.")

st.title("Properties of Mohr's Circle")
st.write("")
st.write("The points at which the circle intersects the x-axis indicate the principle stresses."
         " The maximum normal stress is called the major principle stress, whereas the"
         " minimum normal stress is called the minor principle stress. The centre can be found by taking the average "
         " of the horizontal and vertical stresses. Since these values are typically known, finding the centre is a fairly"
         " straightforward process.  Once the coordinates of the centre are obtained, a triangle can be formed by using"
         " the stress coordinates on the circle. This triangle may be used to compute the radius (we will touch more"
         " on this in the section detailing the procedure. The last major property of Mohr's circle is the origin of planes (also known as the pole)."
         " Properly identifying the pole on Mohr's circle allows for any stress to be calculated at any inclination.)")

st.title("Graphical Procedure")
st.write("")
st.write("1. Determine a sign convention to follow\n"
         "  - Compression (-)\n"
         "  - Tension (+)\n"
         "  - Shear (cw +)\n"
         " \n Please note that the convention is completely arbitrary.  As long as it is consistent throughout the analysis, the results should be the same")
st.write("")
st.write("2. Plot the stress coordinates in the form ($\sigma_{x}$,$\pm\\tau_{xz}$), ($\sigma_{z}$,$\pm\\tau_{zx}$)\n")
st.write("")
st.write("3. Connect the two points with a straight line\n"
         " - The intersection of the line with the x-axis is the centre of the circle")
st.write("")
st.write("4. Draw a circle connecting the two points")
st.write("")
st.write("5. Calculate the radius\n"
         " - Compute the distance between the two coordinates by taking the difference between the larger normal stress and the"
         " smaller normal stress (i.e. if $\sigma_{x}$ > $\sigma_{z}$, $D$ = $\sigma_{x}$ - $\sigma_{z}$\n"
         " - Impose a triangle on the circle of base length $\dfrac{{D}}{2}$ and height $\sigma_{x}$ or $\sigma_{z}$\n"
         " - Employ the Pythagorean Theorem to compute the hypotenuse (i.e. the radius)")
st.write("")
st.write("6. Compute principle stresses\n"
         " - The center coordinates are already known, therefore the principle stresses can"
         " be calculated through the following operation: $\sigma_{p}$ $=$ $C$ $\pm$ $R$ ")

st.write("")
st.write("7. Plot the origin of planes (pole)\n"
         " - Draw two lines parallel to the planes on which σx and σz are acting on\n"
         " - The intersection of these two lines on Mohr's circle is the location of the pole ")
st.write("")
st.write("8. Determine magnitudes of transformed stresses by using the pole\n"
         " - Draw an line crossing the pole at an inclination of the plane of interest\n"
         " - The point where the new line intersects the circle yields the coordinate of a stress transformation\n"
         " - To find the other coordinate, draw a line from the coordinate in the second bullet through the centre of the circle"
         " until it intersects Mohr's circle once again\n"
         " - Be aware that the transformed stresses will always act at a 90$^\circ$ angle from each other.  This is consistent"
         " with the Mohr's circle, since a 90$^\circ$ angle in real life corresponds to a 180$^\circ$ angle in Mohr's circle")