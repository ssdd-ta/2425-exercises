HOST = localhost
PORT = 1234

all: compile

compile:
	protoc --python_out=. door.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__

run_server:
	python3 door.py $(PORT)

open_door:
	python3 controller.py $(HOST) $(PORT) open -t 30 -m pedestrian

close_door:
	python3 controller.py $(HOST) $(PORT) close

get_door_status:
	python3 controller.py $(HOST) $(PORT) status
