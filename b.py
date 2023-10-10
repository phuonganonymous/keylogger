
from pybotnet import BotNet

def _connect(self, connect:tuple[str,int]) -> None:
	self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.conn.connect(connect)
	self.star()

def send(self, req:Request) -> None:
	for payload in req:
		self.conn.send(payload)

def recv(self) -> Respone:
	data = self.conn.recv(MAX_CHUNK_SIZE)
	if not data:
		return None

	res = Respone(data)

	return res 