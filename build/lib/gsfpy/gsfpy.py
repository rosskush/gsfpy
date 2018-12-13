__author__ = 'rosskush'

import geopandas as gpd
import numpy as np
import flopy




class read_gsf():

	def __init__(self,filename):
			# this reads gsf files used in GMS

		with open(filename,'r') as f:
			self.read_data = f.readlines()

		self.nnode, self.nlay, self.iz, self.ic = self.read_data[1].split()
		self.nnode, self.nlay, self.iz, self.ic = [int(n) for n in self.read_data[1].split()]

		self.nvertex = int(self.read_data[2])



	def get_vertex_coords(self):

		vdata = self.read_data[3:self.nvertex+3]
		vertex_coords = {}
		for vert in range(self.nvertex):
			x,y,z = self.read_data[3+vert].split()
			# remember python is zero indexed but these are vertex IDs so they remain one indexed
			vertex_coords[vert+1] = [float(x),float(y),float(z)]
		return vertex_coords

	def get_node_coords(self):
		node_data = self.read_data[self.nvertex+3:]

		node_coords = {}
		for node in range(self.nnode):
			nid, x, y, z, lay, numverts = self.read_data[self.nvertex+3 + node].split()[:6]
			
			# vertidx = {'ivertex': [int(n) for n in self.read_data[self.nvertex+3 + node].split()[6:]]}
			vertidx = [int(n) for n in self.read_data[self.nvertex+3 + node].split()[6:]]


			node_coords[int(nid)] = [float(x), float(y), float(z), int(lay), int(numverts),vertidx]
		return node_coords