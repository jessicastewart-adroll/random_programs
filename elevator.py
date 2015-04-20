class Elevator(object):
	def __init__(self, total_floors):
		self.total_floors = total_floors
		self.to_requests = []
		self.from_requests = []
		self.destination = None
		self.current_floor = 1
		self.current_direction = "up"

	def __repr__(self):
		return "Passengers destinations: {}.\n"\
		"Requests on floors: {}.".format(
			self.to_requests,
			self.from_requests,
			)

	def run(self):
		self.destination = self.next_destination()
		while self.current_floor != self.destination:
			self.move(self.current_direction)
		self.remove_requests()

	def add_from_request(self, floor, direction):
		self.from_requests.append((floor, direction))

	def add_to_request(self, floors):
		if type(floors) == int:
			floors = [floors]
		for floor in floors:
			if self.current_direction == "up" and floor > self.current_floor:
				self.to_requests.append(floor)
			elif self.current_direction == "down" and floor < self.current_floor:
				self.to_requests.append(floor)

	def has_requests(self):
		return self.from_requests or self.to_requests

	def move(self, direction):
		if self.current_direction == "up":
			if self.current_floor == self.total_floors:
				raise Exception('Cannot exceed total floors')
			else:
				self.current_floor += 1
		else:
			if self.current_floor == 1:
				raise Exception('Cannot go below floor 1')
			else:
				self.current_floor -= 1

	def next_destination(self):
		if self.to_requests:
			if self.to_requests[0] > self.current_floor:
				self.current_direction = "up"
				return min(self.to_requests)
			else:
				self.current_direction = "down"
				return max(self.to_requests)
		else:
			if self.current_floor < self.from_requests[0][0]:
				self.current_direction = "up"
			else:
				self.current_direction == "down"
			return self.from_requests[0][0]

	def remove_requests(self):
		if self.current_floor in self.to_requests:
			self.to_requests.remove(self.current_floor)
			print "Dropping-off at floor {}".format(self.current_floor)

		if self.from_requests:
			for fr in self.from_requests:
				if self.current_floor == fr[0]:
					print "Picking up at floor {} to go {}.".format(fr[0], fr[1])
					self.current_direction = fr[1]
					self.from_requests.remove(fr)

###Test Case###
e = Elevator(5)

e.add_from_request(3, "up")
e.run()
e.add_from_request(4, "down")
e.run()
e.add_to_request(2)
e.run()
e.add_from_request(5, "down")
e.run()
e.add_to_request([2,3,4])

while e.has_requests():
	e.run()

e.add_from_request(1, "up")
e.run()
e.add_to_request([5,4,2])

while e.has_requests():
	e.run()

###Test Output###
# Picking up at floor 3 to go up.
# Picking up at floor 4 to go down.
# Dropping-off at floor 2
# Picking up at floor 5 to go down.
# Dropping-off at floor 4
# Dropping-off at floor 3
# Dropping-off at floor 2
# Picking up at floor 1 to go up.
# Dropping-off at floor 2
# Dropping-off at floor 4
# Dropping-off at floor 5
