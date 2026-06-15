import streamlit as st
import time
def triangle_perimeter(a,b,c):
    return a+b+c

def triangle_area(a,b,c):
    s=(a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return area

def square_perimeter(side):
    return 4*side

def square_area(side):
    return side**2

def rectangle_perimeter(l,b):
    return 2*(l+b)

def rectangle_area(l,b):
    return l*b

def circle_perimeter(r):
    return 2*(22/7)*r

def circle_area(r):
    return (22/7)*(r**2)
#3D objects
def cone_tsa(r,l):
    return ((22/7)*r*(r+l))

def cone_vol(r,l):
    return (1/3)*(22/7)*((r**2)*(l**2)-(r**2))**(1/2)

def cube_tsa(s):
    return 6*(s**2)

def cube_vol(s):
    return s**3

def cuboid_tsa(l,b,h):
    return 2*(1*b+b*h+h*l)

def cuboid_vol(l,b,h):
    return l*b*h

def sphere_tsa(r):
    return 4*(22/7)*(r**2)

def sphere_vol(r):
    return (4/3)*(22/7)*(r**2)

def cylinder_tsa(r,h):
    return 2*(22/7)*r*(h+r)

def cylinder_vol(r,h):
    return(22/7)*(r**2)*h

st.title('geometry calculator')
st.header('2D shapes')
#######################triangle
st.subheader('triangle')
col1,col2=st.columns([1,3])

with col1:
    a=st.number_input('side1: ',key='tri_a')
    b=st.number_input('side2: ',key='tri_b')
    c=st.number_input('side3: ',key='tri_c')

cola,colb = st.columns(2)
with cola:
    st.metric('perimeter',triangle_perimeter(a,b,c))
with colb:
    st.metric('area',round(triangle_area(a,b,c),2))
####################square###############################
st.divider()
st.subheader('square')
col1s,col2s = st.columns([1,3])
with col1s:
    s = st.number_input('side: ',key='sq_s')
colas,colbs = st.columns(2)

with colas:
    st.metric('perimeter',round(square_perimeter(s),2))
with colbs:
    st.metric('area',square_area(s))
############################################rec
st.divider()
st.subheader('rectangle')
col1r,col2r = st.columns([1,3])
with col1r:
    l= st.number_input('length: ',key='rect_l')
    b= st.number_input('breadth: ',key='rect_b')
colar,colbr = st.columns(2)

with colar:
    st.metric('perimeter',rectangle_perimeter(l,b))
with colbr:
    st.metric('area',rectangle_area(l,b))
####################################circle
st.divider()
st.subheader('circle')
col1c,col2c = st.columns([1,3])
with col1c:
    r = st.number_input('Radius: ',key='cir_r')
colac,colbc = st.columns(2)

with colac:
    st.metric('perimeter',circle_perimeter(r))
with colbc:
    st.metric('area',circle_area(r))
################################################
st.divider()
st.divider()
st.header('3D objects')
st.subheader('cone')
col1co,col2co = st.columns([1,3])
with col1co:
    r_cone= st.number_input('Radius: ',key='r_cone')
    l_cone= st.number_input('lateral side length: ',key='l_cone')
colaco,colbco = st.columns(2)

with colaco:
    st.metric('total surface area',cone_tsa(r_cone,l_cone))

with colbco:
    st.metric('volume',cone_vol(r_cone,l_cone))

###############################################cube
st.divider()
st.subheader('cube')
col1cu,col2cu = st.columns([1,3])
with col1cu:
    s_cube = st.number_input('side: ',key='cube_s')
colacu,colbcu = st.columns(2)

with colacu:
    st.metric('total surface area',cube_tsa(s_cube))
with colbcu:
    st.metric('volume',cube_vol(s_cube))
##########################################cuboid
st.divider()
st.subheader('cuboid')
col1boid,col2boid = st.columns([1,3])
with col1boid:
    l = st.number_input('length: ',key='cuboid_l')
    b = st.number_input('breadth: ',key='cuboid_b')
    h = st.number_input('height: ',key='cuboid_h')
cola_boid,colb_boid = st.columns(2)
with cola_boid:
    st.metric('total surface area',cuboid_tsa(l,b,h))
with colb_boid:
    st.metric('volume',cuboid_vol(l,b,h))


#################################################sphere
st.divider()
st.subheader('sphere')
col1sp,col2sp = st.columns([1,3])
with col1sp:
    r_sphere = st.number_input('Radius: ',key='sphere_r')
       
colasp,colbsp = st.columns(2)

with colasp:
    st.metric('total surface area',round(sphere_tsa(r_sphere)),2)
with colbsp:
    st.metric('volume',round(sphere_vol(r_sphere),2))
##########################################cylinder
st.divider()
st.divider()
st.header('3D objects')
st.subheader('cylinder')
col1co,col2co = st.columns([1,3])
with col1co:
    r_cyl= st.number_input('Radius: ',key='r_cyl')
    h_cyl= st.number_input('heigth: ',key='h_cyl')
cola_cyl,colb_cyl = st.columns(2)

with cola_cyl:
    st.metric('total surface area',cylinder_tsa(r_cyl,h_cyl))

with colb_cyl:
    st.metric('volume',cylinder_vol(r_cyl,h_cyl))