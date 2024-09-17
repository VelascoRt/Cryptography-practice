import User
import Database
def menu(database : Database.Database, logged_user : User.User):
    print("-Bienvenido-")
    print("\n1. Registrar Usuario\n2. Iniciar sesión\n3. Actualizar los datos\n4. Ver datos de usuarios\n5. Mostrar datos de todos los usuario o usuarios\n6. Eliminar Usuario\n7. Salir")
    o = input("Inserte la opción: ")
    if((o == "3" or o == "4") and logged_user is None):
         print("\nNo ha ingresado sesión\n")
         menu(database, logged_user)
    if(o=="1"):
        new_user = User.User.registerUser()
        Database.Database.Add_User(database,new_user)
        menu(database, logged_user)
    elif(o=="2"):
        email = input("Inserta tu correo: ")
        password= bytes(input("Inserta tu contraseña: "), encoding='utf8')
        logged_user = Database.Database.loggin(database,email,password)
        menu(database,logged_user)
    elif(o=="3"):
        newName = input("Ingresa tu nombre: ")
        newMiddleName = input("Ingresa tu apellido: ")
        newPw = bytes(input("Ingresa tu contraseña: "), encoding='utf8')
        newAddress = input("Ingresa tu dirección: ")
        User.User.updateUser(logged_user,newName,newMiddleName,newPw,newAddress)
        database.update_users(database,logged_user.email,logged_user)
        menu(database,logged_user)
    elif(o=="4"):
        print(f"\n{logged_user}", end="")
        print(logged_user.showPurchase_history())
        menu(database,logged_user)
    elif(o=="5"):
        database.show_users(database)
        menu(database,logged_user)
    elif(o=="6"):
        email = input("Ingrese el correo a eliminar: ")
        database = database.delete_user(database,email)
        if (logged_user.email == email):
            logged_user = None
        menu(database,logged_user)
    elif(o=="7"):
        print("\n -- Saliendo del programa --\n")
    else:
        print("Inserte una opción de los rangos aceptados.")
        menu(database,logged_user)

    

        
     