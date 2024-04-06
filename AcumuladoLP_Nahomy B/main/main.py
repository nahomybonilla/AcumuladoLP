import os
import sys
sys.path.append(r"c:\Users\User\Downloads\AcumuladoLPo")
from dao import daoConnection
from models import clases as c

os.system('cls')

conex = daoConnection.Connection("localhost", "root", "", "bdregisters")
conex.connect()

#Insertar ciudad
def insertarciudad():
    os.system("cls")
    name = input("Inserte el Nombre de la Ciudad")
    ciudad = c.City(name, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    #insertar 
    daoCity.insert(ciudad)

#Mostrar ciudad
def MostrarCiudad():
    os.system("cls")
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_all()
    for City in cities :
        print(City)

#Eliminar ciudad
def EliminarCiudad():
    os.system("cls")
    NameEliminar = input("Escriba el ID de la Ciudad que quiera eliminar")
    daoCity = daoConnection.DaoCity(conex)
    daoCity.delete(NameEliminar)

#Buscar ciudad
def buscarCiudad():
    os.system("cls")
    idBuscarCiudad = input("Escriba el ID de la Ciudad que quiera buscar ")
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_by_id(idBuscarCiudad)
    print(cities)

#Editar ciudad
def editarCiudad():
    os.system("cls")
    MostrarCiudad()
    id_sec = int(input("id que quieres actualizar"))
    name_new = input("Nuevo nombre : ")
    status_new = input("Nuevo status : ")
    daoCity = daoConnection.DaoCity(conex)
    ciudad = c.City(name_new,status_new, id_sec)
    daoCity.update(ciudad)

#MENU 
def menuCiudad():
    print("1. Ingresa la Ciudad")
    print("2. Mostrar Ciudad")
    print("3. Eliminar Ciudad")
    print("4. Editar Ciudad")
    print("5. Buscar Ciudad")
    print("6. Salir")

def main_ciudad():
    opcion_ciudad = 0
    while(opcion_ciudad != 6):
        menuCiudad()
        opcion_ciudad = int(input("Ingresa la opcion que deseas"))
        if(opcion_ciudad == 1):
            insertarciudad()
            os.system("pause")
        elif(opcion_ciudad == 2):
            MostrarCiudad()
            os.system("pause")
        elif(opcion_ciudad == 3):
            EliminarCiudad()
            os.system("pause")
        elif(opcion_ciudad == 4):
            editarCiudad()
            os.system("pause")
        elif(opcion_ciudad == 5):
            buscarCiudad()
            os.system("pause")

# CONSULTAS DE JOB 
def InsertarJob():
    name_job = input("Ingresa el Nombre del Trabajo")
    trabajo = c.Job(name_job,1,any)
    daoJob = daoConnection.DaoJob(conex)
    daoJob.insert(trabajo)

#mostar JOBS
def MostrarJob():
    daoJob = daoConnection.DaoJob(conex)
    Jobs = daoJob.get_all()
    for jobsj in Jobs:
        print(jobsj)

#eliminar JOB
def EliminarJob():
    NameJobEliminar = input("Ingresa el ID del Trabajo que quieras eliminar :  ")
    daoJob = daoConnection.DaoJob(conex)
    daoJob.delete(NameJobEliminar)

#buscar JOB
def buscarJob():
    idBuscarJob = input("Escribe el id del trabajo que quieras buscar : ")
    daoJob = daoConnection.DaoJob(conex)
    jobs = daoJob.get_by_id(idBuscarJob)
    print(jobs)

#editar JOB
def editarJob():
    os.system("cls")
    MostrarJob()
    id_job_sec = int(input("Que id quieres que sea actualizado : "))
    name_new_job = input("Nuevo trabajo :  ")
    status_new = input("Nuevo status : ")
    daoJob = daoConnection.DaoJob(conex)
    trabajo = c.Job(name_new_job,status_new,id_job_sec)
    daoJob.update(trabajo)

#MENU JOB
def menujobs():
    print("1. Ingresar Trabajo")
    print("2. Mostrar Trabajo")
    print("3. Eliminar Trabajo")
    print("4. Editar Trabajo")
    print("5. Buscar")
    print("6. Salir")

def main_Jobs():
    opcion_Job = 0
    while(opcion_Job !=6):
        menujobs()
        opcion_Job = int(input("Ingresa tu Opcion"))
        if(opcion_Job == 1):
            InsertarJob()
            os.system("pause")
        if(opcion_Job == 2):
            MostrarJob()
            os.system("pause")
        if(opcion_Job == 3):
            EliminarJob()
            os.system("pause")
        if(opcion_Job == 4):
            editarJob()
            os.system("pause")
        if(opcion_Job == 5):
            buscarJob()
            os.system("pause")

#INSERTAR EMPLOYEES
def insertarEmployees():
    os.system("cls")
    name_employee = input("Ingresr el Nombre del Empleado : ")
    os.system("cls")
    idciudad= MostrarCiudad()
    idciudad = int(input("Escribe un id de Ciudad para el empleado : "))
    os.system("cls")
    idJob= MostrarJob()
    idJob = int(input("Escribe un id de trabajo para el Empleado : "))
    salario = int(input("Ingrese Salario del empleado : "))
    
    empleado = c.Employee(name_employee,idciudad,idJob,salario,1,any)
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.insert(empleado)

#Mostrar EMPLOYEES
def mostrarEmpleado():
    daoEmployee = daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_all()
    for employees in Employee:
        print(employees)

#Eliminar EMPLOYEE
def EliminarEmployee():
    os.system("cls")
    ned = input("Ingrese el id del Empleado que quieres eliminar : ")
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.delete(ned)

#Buscar EMPLOYEE
def buscarEmployee():
    os.system("cls")
    id_employee_search = input("ingrese el id que quieras buscar : ")
    daoEmployee = daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_by_id(id_employee_search)
    print(Employee)

#ediatar EMPLOYEES
def editarEmployee():
    os.system("cls")
    mostrarEmpleado()
    ieo = int(input("id que quieras actualizar : "))
    n_new_employee = input("Ingrese nuevo empleado : ")
    os.system("cls")
    n_new_idCiudad = MostrarCiudad()
    n_new_idCiudad = input("ingrese el nuevo id de ciudad para el empleado : ")
    os.system("cls")
    n_new_idJob = MostrarJob()
    n_new_idJob = input("ingrese nuevo id de trabajo para el Empleado : ")
    os.system("cls")
    status_new = input("nuevo status : ")
    new_salario = int(input("Nuevo salario : "))
    daoEmployee = daoConnection.DaoEmployee(conex)
    employee = c.Employee(n_new_employee,n_new_idCiudad,n_new_idJob,status_new,new_salario,ieo)
    daoEmployee.update(employee)

#MENU EMPLOYEE
def menuEmpleado():
    print("1. Ingresar Empleados")
    print("2. Mostrar Empleados")
    print("3. Eliminar Empleado")
    print("4. Editar Empleado")
    print("5. Buscar")
    print("6. Salir")

def main_Employees():
    opcion_Employees = 0
    while(opcion_Employees != 6):
        menuEmpleado()
        opcion_Employees = int(input("Ingresa tu Opcion"))
        if(opcion_Employees ==1):
            insertarEmployees()
            os.system("pause")
        if(opcion_Employees ==2):
            mostrarEmpleado()
            os.system("pause")
        if(opcion_Employees == 3):
            EliminarEmployee()
            os.system("pause")
        if(opcion_Employees == 4):
            editarEmployee()
            os.system("pause")
        if(opcion_Employees == 5):
            buscarEmployee()
            os.system("pause")

def main():
    opcion_menu = 0
    while(opcion_menu != 3):
        print("1. MENU CIUDAD")
        print("2. MENU JOBS")
        print("3. MENU EMPLOYEES")
        opcion_menu = int(input("ELIGE UN MENU : "))
        if(opcion_menu == 1):
            main_ciudad()
            os.system("pause")
        if(opcion_menu == 2):
            main_Jobs()
            os.system("pause")
        if(opcion_menu == 3):
            main_Employees()
            os.system("pause")
        else:
            print("opcion incorrecta")

main()