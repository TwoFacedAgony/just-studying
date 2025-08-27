class Server:
    __servers_count = 0

    def __new__(cls, *args, **kwargs):
        cls.__server_id = cls.__servers_count
        cls.__servers_count += 1
        return super().__new__(cls)

    def __init__(self) -> None:
        self.ip = self.__server_id
        self.buffer = []
        self.router = None

    def send_data(self, data) -> None:
        self.router.buffer.append(data) if not self.router is None else None

    def get_data(self) -> list:
        to_show = self.buffer.copy()
        self.buffer.clear()
        return to_show

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server: Server) -> None:
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server: Server) -> None:
        self.servers.pop(server.get_ip())
        server.router = None

    def send_data(self) -> None:
        for package in self.buffer:
            if package.dest_ip in self.servers:
                self.servers[package.dest_ip].buffer.append(package)
        self.buffer.clear()


class Data:
    def __init__(self, data: str, dest_ip: int) -> None:
        self.data = data
        self.dest_ip = dest_ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_from)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data
msg_lst_to = sv_to.get_data
