import streamlit as st
import numpy as np
import plotly.graph_objects as go
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

sig1 = C + R
sig2 = C - R
sigx_prime = C + ((sigx-sigz)/2)*cos(2*radians(theta)) + taoxz*sin(2*radians(theta))
sigz_prime = C - ((sigx-sigz)/2)*cos(2*radians(theta)) - taoxz*sin(2*radians(theta))
tao_prime = -((sigx-sigz)/2)*sin(2*radians(theta)) + taoxz*cos(2*radians(theta))

t = np.linspace(0, 2 * np.pi, 100 + 1)
x1 = R * np.cos(t) + C
x2 = R * np.sin(t)

# Define arrays for lines
X1 = np.array([sigx, sigz])
Y1 = np.array([-taoxz, taoxz])
X2 = np.array([sigx_prime, sigz_prime])
Y2 = np.array([-tao_prime, tao_prime])
X3 = np.array([sig2, sig1])
Y3 = np.array([0, 0])
X4 = np.array([C, C])
Y4 = np.array([-R, R])

# Create the Plotly figure
fig = go.Figure()

# Add the Mohr's circle
fig.add_trace(go.Scatter(
    x=x1, y=x2,
    mode='lines',
    name="Mohr's Circle",
    line=dict(color='black')
))

# Add the vertical and horizontal lines through center
fig.add_trace(go.Scatter(
    x=X4, y=Y4,
    mode='lines',
    name='Center Lines',
    line=dict(color='black')
))

# Add principle stress line
fig.add_trace(go.Scatter(
    x=X3, y=Y3,
    mode='lines',
    name='Principle Stresses',
    line=dict(color='black')
))

# Add stress points line
fig.add_trace(go.Scatter(
    x=X1, y=Y1,
    mode='lines',
    name='Stress Points',
    line=dict(color='red')
))

# Add transformed stress line
fig.add_trace(go.Scatter(
    x=X2, y=Y2,
    mode='lines',
    name='Transformed Stress',
    line=dict(color='cyan')
))

# Add scatter points
fig.add_trace(go.Scatter(
    x=[sigx], y=[-taoxz],
    mode='markers',
    name='σx',
    marker=dict(color='cyan', size=10)
))

fig.add_trace(go.Scatter(
    x=[sigz], y=[taoxz],
    mode='markers',
    name='σz',
    marker=dict(color='black', size=10)
))

fig.add_trace(go.Scatter(
    x=[sig1], y=[0],
    mode='markers',
    name="σ'1",
    marker=dict(color='blue', size=10)
))

fig.add_trace(go.Scatter(
    x=[sig2], y=[0],
    mode='markers',
    name="σ'2",
    marker=dict(color='red', size=10)
))

fig.add_trace(go.Scatter(
    x=[C], y=[0],
    mode='markers',
    name='Centre',
    marker=dict(color='magenta', size=10)
))

fig.add_trace(go.Scatter(
    x=[sigx_prime], y=[-tao_prime],
    mode='markers',
    name='Transformed Point 1',
    marker=dict(color='cyan', size=10)
))

fig.add_trace(go.Scatter(
    x=[sigz_prime], y=[tao_prime],
    mode='markers',
    name='Transformed Point 2',
    marker=dict(color='cyan', size=10)
))

# Add vertical and horizontal lines at stress points
fig.add_vline(x=sigx, line_width=1, line_color="blue")
fig.add_hline(y=taoxz, line_width=1, line_color="blue")

# Update layout
fig.update_layout(
    title="Mohr's Circle of Stresses",
    xaxis_title="Normal Stress (σx)",
    yaxis_title="Shear Stress (τxz)",
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        font=dict(size=10)
    ),
    # Make the plot square and add grid
    yaxis=dict(
        scaleanchor="x",
        scaleratio=1,
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
    ),
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
    ),
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

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