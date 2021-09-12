# source: https://stackoverflow.com/questions/32398160/image-based-visual-servoing-algorithm-in-matlab
# translated into python - since matlab indexing starts from 1 instead of zero incrememnt ALL indexing by 1
# euler angles https://www.coppeliarobotics.com/helpFiles/en/eulerAngles.htm
import numpy as np

ts, vc = VisualServo(??????????????????)

def VisualServo(A3D, B3D, C3D, D3D)

    # global  A3D B3D C3D D3D A B C D Ad Bd Cd Dd

    #coordinates of the 4 points wrt camera frame
    # old coordinate declaration, shows that inputs need to be x,y,z coordinates of each point... ??? how would we know that
    # A3D = [-0.2633;0.27547;0.8956];
    # B3D = [0.2863;-0.2749;0.8937];
    # C3D = [-0.2637;-0.2746;0.8977];
    # D3D = [0.2866;0.2751;0.8916];

    #initial projections (computed here only to show their relation with the desired ones) 
    # A=A3D(1:2)/A3D(3)
    # B=B3D(1:2)/B3D(3)
    # C=C3D(1:2)/C3D(3)
    # D=D3D(1:2)/D3D(3)
    A=A3D(0:1)/A3D(2)
    B=B3D(0:1)/B3D(2)
    C=C3D(0:1)/C3D(2)
    D=D3D(0:1)/D3D(2)

    #initial camera position and orientation
    #orientation is expressed in Euler angles (X-Y-Z around the inertial frame
    #of reference)
    # cam=[0;0;0;0;0;0] vertical array
    cam = [[0],[0],[0],[0],[0],[0]]

    #desired projections
    #Ad=A+[0.1;0]
    Ad=A+[[0.1],[0]]
    Bd=B
    #Cd=C+[0.1;0]
    Cd=C+[[0.1],[0]]
    Dd=D

    t0 = 0
    tf = 50

    s0 = cam

    #time step
    dt=0.01
    t = euler_ode(t0, tf, dt, s0)


def euler_ode(t0,tf,dt,s0)

    # global A3D B3D C3D D3D Ad Bd Cd Dd 

    s = s0
    ts=[]
    #for t=t0:dt:tf
    for x in range(t0, tf, dt)
        #ts(end+1)=t
        ts(-1)=t

        cam = s

        # rotation matrix R_WCS_CCS
        # R = calc_Rotation_matrix(cam(4),cam(5),cam(6))
        R = calc_Rotation_matrix(cam(3),cam(4),cam(5))
        # r = cam(1:3)
        r = cam(0:2)

        # 3D coordinates of the 4 points wrt the NEW camera frame
        # A3D_cam = R'*(A3D-r)
        # B3D_cam = R'*(B3D-r)
        # C3D_cam = R'*(C3D-r)
        # D3D_cam = R'*(D3D-r) minus 1?
        A3D_cam = transpose(R)*(A3D-r)
        B3D_cam = transpose(R)*(B3D-r)
        C3D_cam = transpose(R)*(C3D-r)
        D3D_cam = transpose(R)*(D3D-r)

        # NEW projections
        # A=A3D_cam(1:2)/A3D_cam(3);
        # B=B3D_cam(1:2)/B3D_cam(3);
        # C=C3D_cam(1:2)/C3D_cam(3);
        # D=D3D_cam(1:2)/D3D_cam(3);
        A=A3D_cam(0:1)/A3D_cam(2)
        B=B3D_cam(0:1)/B3D_cam(2)
        C=C3D_cam(0:1)/C3D_cam(2)
        D=D3D_cam(0:1)/D3D_cam(2)

        # computing the L matrices
        # L1 = L_matrix(A(1),A(2),A3D_cam(3));
        # L2 = L_matrix(B(1),B(2),B3D_cam(3));
        # L3 = L_matrix(C(1),C(2),C3D_cam(3));
        # L4 = L_matrix(D(1),D(2),D3D_cam(3));
        # L = [L1;L2;L3;L4];

        L1 = L_matrix(A(0),A(1),A3D_cam(2))
        L2 = L_matrix(B(0),B(1),B3D_cam(2))
        L3 = L_matrix(C(0),C(1),C3D_cam(2))
        L4 = L_matrix(D(0),D(1),D3D_cam(2))

        # stack the image jacobians and invert them https://youtu.be/iPJhjZIoFMM?t=168
        L = [[L1],[L2],[L3],[L4]]


        #updating the projection errors
        # e = [A-Ad;B-Bd;C-Cd;D-Dd]
        e = [[A-Ad],[B-Bd],[C-Cd],[D-Dd]]
        
        #compute camera velocity 'vc' - this is the set of velocities we want to move our coordinates to the desired location on the camera https://youtu.be/iPJhjZIoFMM?t=187

        # https://au.mathworks.com/help/matlab/ref/pinv.html#mw_ffa95973-29a2-48a1-adb0-5a4214e0d9cf ==> https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html
        # vc = -0.5*pinv(L)*e
        vc = -0.5*linalg.pinv(L)*e

        #change of the camera position and orientation (this might be a plotting thing???)
        ds = vc

        #update camera position and orientation (this might be a plotting thing???)
        s = s + ds*dt
   
    # ts(end+1)=tf+dt
    ts(-1) = tf + dt
    return ts, vc


def calc_Rotation_matrix(theta_x, theta_y, theta_z)

    # Rx = [1 0 0; 0 cos(theta_x) -sin(theta_x); 0 sin(theta_x) cos(theta_x)];
    # Ry = [cos(theta_y) 0 sin(theta_y); 0 1 0; -sin(theta_y) 0 cos(theta_y)];
    # Rz = [cos(theta_z) -sin(theta_z) 0; sin(theta_z) cos(theta_z) 0; 0 0 1];
    Rx = [[1, 0, 0], [0, cos(theta_x), -sin(theta_x)], [0, sin(theta_x), cos(theta_x)]]
    Ry = [[cos(theta_y), 0, sin(theta_y)], [0, 1, 0], [-sin(theta_y), 0, cos(theta_y)]]
    Rz = [[cos(theta_z), -sin(theta_z), 0], [sin(theta_z), cos(theta_z), 0], [0, 0, 1]]
    
    return R = Rx*Ry*Rz



def L_matrix(x,y,z)
    # image jacobian https://youtu.be/iPJhjZIoFMM?t=135
    # L = [-1/z,0,x/z,x*y,-(1+x^2),y;
    #   0,-1/z,y/z,1+y^2,-x*y,-x];
    return L = [[-1/z,0,x/z,x*y,-(1+x^2),y], [0,-1/z,y/z,1+y^2,-x*y,-x]]
