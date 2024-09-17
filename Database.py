import Password
import User

class Database:
    users : User = []
    # Función para añadir usuario
    def Add_User(self,newUser):
        self.users.append(newUser)
        print("El usuario ha sido agregado.")
    
    # Mostrar todos los usuarios.
    def show_users(self):
        print("\n--Lista de usuarios--\n")
        if len(self.users) == 0:
            print("No hay usuarios.")
        for user in self.users:
            print(f"{user}\n")
            print(f"{user.showPurchase_history()}\n")
    
    def update_users(self,email,userUpdated):
        for i in range(0,len(self.users)):
            if self.users[i].email == email:
                self.users[i] = userUpdated
                print(f"Se ha actualizado el usuario con el correo: {email}")
                return
        print("No se ha encontrado el usuario.")
    
    # Eliminar usuarios.
    def delete_user(self,email):
        for i in range(0,len(self.users)):
            if self.users[i].email == email:
                self.users.pop(i)
                print(f"Se ha eliminado el usuario con el correo: {email}")
                return self
        print("No se ha encontrado el usuario.")

    # Función para iniciar sesión.    
    def loggin(self,email,pw):
        if (email is None or pw is None):
            print("\nCorreo o contraseña vacios\n")
            return None
        for user in self.users:
            dpw = Password.Password.decrypt(user.key,user.pw)
            if user.email == email and pw == dpw:
                print("\nHa iniciado sesión correctamente.\n")
                return user
        print("\nCorreo o contraseña incorrectos\n")
        return None

# Usuarios de prueba
sk, pw = Password.Password.encryptPasword(b"contra")
user_test = User.User(name="Vicor", middle_name="Ortíz", email="victor@hotmail.com", pw=pw, key=sk, address="San Judas 401 37150", purchase_history=["Mouse - $ 102","Monitor - $ 1250"])
Database.Add_User(Database,user_test)

sk, pw = Password.Password.encryptPasword(b"pass")
user_test1 = User.User(name="Samuel", middle_name="Alejandro", email="samuel@hotmail.com", pw=pw, key=sk, address="Tlaxcala", purchase_history=["Pencil - $ 2","Pizza - $ 31","Macbook Pro - $ 30000"])
Database.Add_User(Database,user_test1)