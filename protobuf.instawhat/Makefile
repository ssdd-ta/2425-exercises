HOST = localhost
PORT = 1234

all: compile

compile:
	protoc --python_out=. instawhat.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__

run_server:
	python3 server.py $(PORT)

post_photo:
	python3 client.py $(HOST) $(PORT) post_photo "http://example.com/photo.jpg"

comment_photo:
	python3 client.py $(HOST) $(PORT) comment_photo Jane.Doe "http://example.com/photo.jpg" "Great photo!"

rate_photo:
	python3 client.py $(HOST) $(PORT) rate_photo Jane.Doe "http://example.com/photo.jpg" 5

like_photo:
	python3 client.py $(HOST) $(PORT) like_photo "http://example.com/photo.jpg" Jane.Doe

delete_photo:
	python3 client.py $(HOST) $(PORT) delete_photo "http://example.com/photo.jpg"

get_last_photos:
	python3 client.py $(HOST) $(PORT) get_last_photos Jane.Doe
