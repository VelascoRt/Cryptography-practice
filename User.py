import Password

# Clase de Usuario
class User:
    name : str
    middle_name : str
    email : str
    pw : bytes
    key : bytes
    address : str
    purchase_history = []
    def __init__(self, name, middle_name, email, pw, key, address, purchase_history,) -> None:
        self.name = name
        self.middle_name = middle_name
        self.email = email
        self.pw = pw
        self.key = key
        self.address = address
        self.purchase_history = purchase_history

    # Función para mostrar los Usuarios.
    def __str__(self):
        return f"Nombre: {self.name} \nApellido: {self.middle_name}\nCorreo electrónico: {self.email} \nDirección: {self.address} \nHistorial de compras:"
    
    # Función para mostrar el historial de compras.
    def showPurchase_history(self):
        if (self.purchase_history is None):
            return "No hay historial de compras."
        for purchases in self.purchase_history:
            print(f"{str(purchases)}.")
    
    # Función para Actualizar el usuario.
    def updateUser(self, newName, newMiddleName, newPw, newAddress):
        self.key, self.pw = Password.Password.encryptPasword(newPw) if newPw is not None else self.pw
        self.name = newName if newName is not None else self.name
        self.middle_name = newMiddleName if newMiddleName is not None else self.middle_name
        self.address = newAddress if newAddress is not None else self.address
        print("El usuario se actualizado.")
    
    # Función para registrar el usuario.
    def registerUser():
        print("\n --Registro de Usuarios--")
        name = input("Ingresa tu nombre: ")
        middle_name = input("Ingresa tus apellido: ")
        address = input("Ingresa tu Dirección: ")
        email = input("Ingresa tu Correo eléctronico: ")
        pw = bytes(input("Ingresa tu contraseña: "), encoding='utf8')
        key, epw = Password.Password.encryptPasword(pw)
        user = User(name,middle_name, email, epw, key, address,[] )
        return user



        
    
