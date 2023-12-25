class StockController:
    def __init__(self) -> None:
        self.RoleList = []

    def create_role(self, role) -> None:
        self.RoleList.append(role)
