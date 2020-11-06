def getpos(wnbxb,wnbyb,wnbzb,abx,aby,abz):
	""" wnb (angular velocity from gyro sensor in body frame) contain values along x,y,z
	
	ab(acceleration from the accelerometer in body frame) is a column matrix containing value along x, y, z
	"""
	ab=np.matrix([[axb],[ayb],[azb]])
	import numpy as np
	from math import atan2,cos,sin
	#wnb is angular velocity of B system relative to N
	#solved the matrix on paper
	gamma=atan2(wnbyb,wnbzb)
	theta=atan2((sin(gamma))*(gamma-wnbxb),wnbyb)
	phi=wnbyb/(sin(gamma)*cos(thetha))

	Cbn12=sin(gamma)*sin(theta)*cos(phi)-cos(gamma)*sin(phi)
	Cbn13=sin(gamma)*sin(phi)+cos(gamma)*sin(theta)*cos(phi)
	Cbn22=cos(phi)*sin(gamma)+sin(gamma)*sin(theta)*sin(phi)
	Cbn23=sin(phi)*sin(theta)*cos(gamma)-sin(gamma)*cos(phi)
	#Cbn is the coordinate transformation matrix from B to N system
	Cbn=np.matrix([[cos(phi)*cos(theta),Cbn12,Cbn13],[cos(theta)*sin(phi),Cbn22,Cbn23],[sin(theta),sin(gamma)*cos(theta),cos(theta)*cos(gamma)]])

	#accelerstion in the b frame (including gravity)
	an1=np.matrix([[axn1],[ay1],[azn1]])
	an1=Cbn*ab
	#acceleration in the N frame (after removing g) is calculated in an
	an=np.matrix([[axn],[ayn],[azn]])
	#Effect of gravity removed 
	an=an1-np.matrix([[0],[0],[9.8]])
	dellt=0.0001;

	#calulate velocity 
	dellv=np.matrix([[dellvxn],[dellvyn],[dellvzn]])
	dellv=an*dellt
	#new is after 1 second from old
	vnt_new=np.matrix([[vxn_new],[vyn_new],[vzn_new]])
	vnt_new=np.matrix([[vxn_old],[vyn_old],[vzn_old]])+dellv

	#calculate displacement
	dellXn=np.matrix([[dellXxn],[dellXyn],[dellXzn]])
	dellXn=vnt_new*dellt+0.5*an*dellt*dellt
	Xn_new=np.matrix([[Xxn_new],[Xyn_new],[Xzn_new]])
	Xn_new=np.matrix([[Xxn_old],[Xyn_old],[Xzn_old]])+dellXn		
	return Xn_new
