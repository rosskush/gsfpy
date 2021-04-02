__author__ = 'rosskush'

import pandas as pd

class GsfReader():
	'''
	a helper class to read a standard gsf file
	'''

	def __init__(self,gsffilename):
		# this reads gsf files used in GMS

		with open(gsffilename,'r') as f:
			self.read_data = f.readlines()

		self.nnode, self.nlay, self.iz, self.ic = [int(n) for n in self.read_data[1].split()]

		self.nvertex = int(self.read_data[2])



	def get_vertex_coordinates(self):
		'''

		:return:
			Dictionary containing list of x, y and z coordinates for each vertex
		'''
		# vdata = self.read_data[3:self.nvertex+3]
		vertex_coords = {}
		for vert in range(self.nvertex):
			x,y,z = self.read_data[3+vert].split()
			vertex_coords[vert+1] = [float(x),float(y),float(z)]
		return vertex_coords

	def get_node_data(self):
		'''

		:return:
			DataFrame containing Node information; Node, X, Y, Z, layer, numverts, vertidx

		'''

		node_data = []
		for node in range(self.nnode):
			nid, x, y, z, lay, numverts = self.read_data[self.nvertex+3 + node].split()[:6]
			
			# vertidx = {'ivertex': [int(n) for n in self.read_data[self.nvertex+3 + node].split()[6:]]}
			vertidx = [int(n) for n in self.read_data[self.nvertex+3 + node].split()[6:]]


			node_data.append([int(nid),float(x), float(y), float(z), int(lay), int(numverts),vertidx])

		nodedf = pd.DataFrame(node_data,columns=['Node','X','Y','Z','layer','numverts','vertidx'])
		return nodedf

	def get_node_coordinates(self):
		'''

		:return:
			Dictionary containing x and y coordinates for each node
		'''
		node_coords = {}
		for node in range(self.nnode):
			nid, x, y, z, lay, numverts = self.read_data[self.nvertex + 3 + node].split()[:6]

			node_coords[nid] = [float(x), float(y)]

		return node_coords

if __name__ == '__main__':
	import os
	gsffilename = os.path.join('..','example','freyberg.usg.gsf')

	gsf = GsfReader(gsffilename)


	print('eh')

