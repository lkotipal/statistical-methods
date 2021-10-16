from enum import IntEnum
from math import floor
import numpy as np
from random import shuffle, seed
from collections import deque

class Seat(IntEnum):
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	SEATS = 6

class Passenger:
	aisle_time = 10
	luggage_time = 25

	def __init__(self, id):
		self.id = id
		if id < 3:
			self.row = 0
			self.seat = Seat(id)
		else:
			self.row = int(floor((id+3) / 6))
			self.seat = Seat((id + 3) % 6)
		self.waiting_aisle = -1
		self.waiting_luggage = -1
	
	def wait_luggage(self):
		if self.waiting_luggage == -1:
			self.waiting_luggage = self.luggage_time
		if self.waiting_luggage > 0:
			self.waiting_luggage -= 1
			return False
		else:
			return True
	
	def wait_aisle(self, obstructing):
		if self.waiting_aisle == -1:
			self.wait_aisle = obstructing * self.aisle_time - 1
		if self.waiting_aisle > 0:
			self.wait_aisle -= 1
			return False
		else:
			return True
	
	def wait(self, obstructing):
		if self.wait_luggage():
			return self.wait_aisle(obstructing)
		else:
			return False
	
	def __repr__(self):
		return f'{self.row+1}' + chr(ord('A') + self.seat)

class Plane:
	PASSENGER_GAP = 0.5
	GATE_DISTANCE = 25
	SEAT_ROWS = 28

	def __init__(self):
		self.seats = [[0 for i in range(Seat.SEATS)] for j in range(Plane.SEAT_ROWS)]
		self.queue = [None for i in range(int((Plane.SEAT_ROWS + Plane.GATE_DISTANCE) / Plane.PASSENGER_GAP) - 1)]

		#passengers = [Passenger(i) for i in range(Plane.SEAT_ROWS*Seat.SEATS - 3)]
		#shuffle(passengers)
		#self.passengers = deque(passengers)
		self.passengers = deque([Passenger(0)])

		self.time = 0
	
	def on_row(i):
		if i * Plane.PASSENGER_GAP >= Plane.GATE_DISTANCE and i % 2 == 0:
			return int((i - Plane.GATE_DISTANCE / Plane.PASSENGER_GAP) / 2)
		else:
			return None
	
	def simulate(self):
		# Iterate from back to front so the queue moves smoothly
		for i in range(len(self.queue) - 1, -1, -1):
			passenger = self.queue[i]
			# If there's a passenger
			if passenger:
				# Who is on the correct row
				row = Plane.on_row(i)
				if row == passenger.row:
					# Who is done waiting
					if passenger.wait(self.obstructing(row, passenger.seat)):
						# Move him into the seat and delet from queue
						self.seats[row][passenger.seat] = passenger
						self.queue[i] = None
				else:
					# If there's space ahead
					if not self.queue[i+1]:
						# Move the passenger forward
						self.queue[i+1] = passenger
						self.queue[i] = None

		if not self.queue[0] and self.passengers:
			self.queue[0] = self.passengers.pop()

		# False unless the queue is empty
		if any(self.queue):
			self.time += 1
			return False
		else:
			return True



	def obstructing(self, row, seat):
		if seat == Seat.A:
			return (1 if self.seats[row][Seat.B] else 0) + (1 if self.seats[row][Seat.C] else 0)
		elif seat == Seat.B:
			return 1 if self.seats[row][Seat.C] else 0
		elif seat == Seat.E:
			return 1 if self.seats[row][Seat.D] else 0
		elif seat == Seat.F:
			return (1 if self.seats[row][Seat.D] else 0) + (1 if self.seats[row][Seat.E] else 0)
		else:
			return 0

	def __str__(self):
		s = ''
		for i in range(len(self.queue)):
			row = Plane.on_row(i)
			if row is not None:
				s += f'{self.seats[row][:3]}|{row + 1}|{self.seats[row][3:]}\n'
		return s

seed(14819973)
times = np.zeros(100)
for i in range(100):
	plane = Plane()
	while not plane.simulate():
		pass
	times[i] = plane.time

print(f'Average time {np.average(times)}')
print(f'Standard deviation {np.std(times)}')