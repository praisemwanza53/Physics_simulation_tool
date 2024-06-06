import streamlit as st
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Sidebar Navigation
st.sidebar.title("Physics Simulations")
simulation = st.sidebar.selectbox(
    "Choose a simulation",
    [
        "Projectile Motion",
        "Simple Harmonic Motion",
        "Electric Field and Potential",
        "Wave Interference",
        "Circular Motion and Centripetal Force"
    ]
)

# Projectile Motion Simulation
def projectile_motion():
    st.title("Projectile Motion Simulator")

    def calculate_motion(v0, angle, h0):
        g = 9.81  # acceleration due to gravity (m/s^2)
        theta = np.radians(angle)
        
        t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * h0)) / g
        h_max = h0 + (v0**2 * np.sin(theta)**2) / (2 * g)
        x_max = v0 * np.cos(theta) * t_flight
        t = np.linspace(0, t_flight, num=500)
        x = v0 * np.cos(theta) * t
        y = h0 + v0 * np.sin(theta) * t - 0.5 * g * t**2
        
        return x, y, t_flight, h_max, x_max

    v0 = st.slider("Initial Velocity (m/s)", 0, 100, 50)
    angle = st.slider("Launch Angle (degrees)", 0, 90, 45)
    h0 = st.slider("Initial Height (m)", 0, 100, 0)
    x, y, t_flight, h_max, x_max = calculate_motion(v0, angle, h0)
    
    st.write(f"**Time of Flight:** {t_flight:.2f} seconds")
    st.write(f"**Maximum Height:** {h_max:.2f} meters")
    st.write(f"**Range:** {x_max:.2f} meters")

    fig = make_subplots()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Projectile Path'))
    fig.update_layout(
        xaxis_title="Distance (m)",
        yaxis_title="Height (m)",
        title="Projectile Motion",
        showlegend=True
    )
    
    st.plotly_chart(fig)
    
    st.write("""
    Projectile motion refers to the motion of an object projected into the air, subject to only the acceleration of gravity. The key parameters in projectile motion are:
    
    - **Initial Velocity (v_0)**: The speed at which the object is launched.
    - **Launch Angle (θ)**: The angle at which the object is launched with respect to the horizontal.
    - **Initial Height (h_0)**: The height from which the object is launched.
    
    The main characteristics of projectile motion include:
    - **Time of Flight (T)**: The total time the object remains in the air.
    - **Maximum Height (H)**: The highest point the object reaches in its trajectory.
    - **Range (R)**: The horizontal distance the object travels before hitting the ground.
    
    The equations governing projectile motion are:
    - Horizontal distance (x): \\( x = v_0 \\cos(θ) \\cdot t \\)
    - Vertical distance (y): \\( y = h_0 + v_0 \\sin(θ) \\cdot t - \\frac{1}{2} g \\cdot t^2 \\)
    
    Where:
    - \\( g \\) is the acceleration due to gravity (9.81 m/s²).
    """)

# Simple Harmonic Motion Simulation
def simple_harmonic_motion():
    st.title("Simple Harmonic Motion Simulator")
    
    m = st.slider("Mass (kg)", 0.1, 10.0, 1.0)
    k = st.slider("Spring Constant (N/m)", 0.1, 10.0, 1.0)
    A = st.slider("Amplitude (m)", 0.1, 10.0, 1.0)
    omega = np.sqrt(k/m)
    
    t = np.linspace(0, 10, 1000)
    x = A * np.cos(omega * t)
    v = -A * omega * np.sin(omega * t)
    
    fig = make_subplots(rows=2, cols=1)
    
    # Displacement vs Time
    fig.add_trace(go.Scatter(x=t, y=x, mode='lines', name='Displacement'), row=1, col=1)
    fig.update_xaxes(title_text="Time (s)", row=1, col=1)
    fig.update_yaxes(title_text="Displacement (m)", row=1, col=1)
    
    # Phase Space Plot
    fig.add_trace(go.Scatter(x=x, y=v, mode='lines', name='Phase Space'), row=2, col=1)
    fig.update_xaxes(title_text="Displacement (m)", row=2, col=1)
    fig.update_yaxes(title_text="Velocity (m/s)", row=2, col=1)
    
    fig.update_layout(height=600, title_text="Simple Harmonic Motion")
    st.plotly_chart(fig)
    
    st.write("""
    Simple Harmonic Motion (SHM) is a type of oscillatory motion where the restoring force is directly proportional to the displacement. The key parameters in SHM are:
    
    - **Mass (m)**: The mass of the oscillating object.
    - **Spring Constant (k)**: A measure of the stiffness of the spring.
    - **Amplitude (A)**: The maximum displacement from the equilibrium position.
    
    The equations governing SHM are:
    - Displacement (x): \\( x(t) = A \\cos(ωt) \\)
    - Velocity (v): \\( v(t) = -Aω \\sin(ωt) \\)
    
    Where:
    - \\( ω \\) is the angular frequency, given by \\( ω = \\sqrt{\\frac{k}{m}} \\).
    """)

# Electric Field and Potential Simulation
def electric_field_and_potential():
    st.title("Electric Field and Potential Simulator")
    
    q = st.slider("Charge (C)", -10.0, 10.0, 1.0)
    r = st.slider("Distance (m)", 0.1, 10.0, 1.0)
    k = 8.99e9  # Coulomb's constant
    
    E = k * q / r**2
    V = k * q / r
    
    st.write(f"**Electric Field (E):** {E:.2e} N/C")
    st.write(f"**Electric Potential (V):** {V:.2e} V")
    
    st.write("""
    The electric field and electric potential at a distance \\( r \\) from a point charge \\( q \\) are given by:
    
    - **Electric Field (E)**: \\( E = \\frac{kq}{r^2} \\)
    - **Electric Potential (V)**: \\( V = \\frac{kq}{r} \\)
    
    Where:
    - \\( k \\) is Coulomb's constant (\\( 8.99 \\times 10^9 \\) N m²/C²).
    """)

# Wave Interference Simulation
def wave_interference():
    st.title("Wave Interference Simulator")
    
    f = st.slider("Frequency (Hz)", 1, 10, 1)
    A = st.slider("Amplitude (m)", 0.1, 1.0, 0.5)
    phase = st.slider("Phase Difference (radians)", 0.0, np.pi, 0.0)
    
    t = np.linspace(0, 10, 1000)
    y1 = A * np.sin(2 * np.pi * f * t)
    y2 = A * np.sin(2 * np.pi * f * t + phase)
    y = y1 + y2
    
    fig = make_subplots()
    fig.add_trace(go.Scatter(x=t, y=y1, mode='lines', name='Wave 1'))
    fig.add_trace(go.Scatter(x=t, y=y2, mode='lines', name='Wave 2'))
    fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name='Resultant Wave'))
    fig.update_layout(
        xaxis_title="Time (s)",
        yaxis_title="Displacement (m)",
        title="Wave Interference",
        showlegend=True
    )
    
    st.plotly_chart(fig)
    
    st.write("""
    Wave interference is the phenomenon that occurs when two waves meet while traveling along the same medium. The key parameters in wave interference are:
    
    - **Frequency (f)**: The number of cycles per second.
    - **Amplitude (A)**: The maximum displacement from the equilibrium position.
    - **Phase Difference**: The difference in phase between the two waves.
    
    The resultant wave is the sum of the individual waves:
    - Resultant Wave (y): \\( y = y1 + y2 \\)
    """)

# Circular Motion and Centripetal Force Simulation
def circular_motion():
    st.title("Circular Motion and Centripetal Force Simulator")
    
    m = st.slider("Mass (kg)", 0.1, 10.0, 1.0)
    r = st.slider("Radius (m)", 0.1, 10.0, 1.0)
    v = st.slider("Velocity (m/s)", 0.1, 10.0, 1.0)
    
    F_c = m * v**2 / r
    
    t = np.linspace(0, 2*np.pi, 1000)
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    fig = make_subplots()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Circular Path'))
    fig.update_layout(
        xaxis_title="x (m)",
        yaxis_title="y (m)",
        title="Circular Motion",
        showlegend=True
    )
    
    st.plotly_chart(fig)
    
    st.write(f"**Centripetal Force (F_c):** {F_c:.2f} N")
    
    st.write("""
    Circular motion is the motion of an object along the circumference of a circle. The key parameters in circular motion are:
    
    - **Mass (m)**: The mass of the object.
    - **Radius (r)**: The radius of the circular path.
    - **Velocity (v)**: The speed of the object along the circular path.
    
    The centripetal force required to keep an object in circular motion is given by:
    - Centripetal Force (F_c): \\( F_c = \\frac{mv^2}{r} \\)
    """)

# Simulation selection
if simulation == "Projectile Motion":
    projectile_motion()
elif simulation == "Simple Harmonic Motion":
    simple_harmonic_motion()
elif simulation == "Electric Field and Potential":
    electric_field_and_potential()
elif simulation == "Wave Interference":
    wave_interference()
elif simulation == "Circular Motion and Centripetal Force":
    circular_motion()
