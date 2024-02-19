import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.argument('nombre')
@click.argument('telefono')
@click.argument('correo')
@click.pass_context
def agregar(ctx, nombre, telefono, correo):
    if not nombre or not telefono or not correo:
        ctx.fail('datos requeridos !!!')
    else:
        data = json_manager.read_json()  
        next_id = len(data) + 1
        next_user = {
            'id': next_id,
            'nombre': nombre,
            'telefono': telefono,
            'correo': correo,
            
        }
        data.append(next_user)
        json_manager.write_json(data)
        print(f"Usuario {nombre} {telefono} {correo} creado exitosamente !!! con id {next_id}")


@cli.command()
def listar():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['nombre']} - {user['telefono']} - {user['correo']}")




@cli.command()
@click.argument('nombre', type=str)
def buscar(nombre):
    users = json_manager.read_json()
    user = next((user for user in users if user['nombre'] == nombre), None)
    if user is None:
        print(f"Contacto con {nombre} not found")
    else:    
        print(f"{user['id']} - {user['nombre']} - {user['telefono']} - {user['correo']}")



@cli.command()
@click.argument('nombre', type=str)
def eliminar(nombre):
    users = json_manager.read_json()
    userDelete = next((user for user in users if user['nombre'] == id), None)
    if userDelete is None:
        print(f"User with id {nombre} not found")
    else:    
        users.remove(userDelete)
        json_manager.write_json(users)
        print(f"User with id {id} was deleted")





@cli.command()
@click.argument('id', type=int)
@click.option('--nombre', help='Nombre del usuario')
@click.option('--apellido', help='Apellido del usuario')
def update(id, nombre, apellido):
    users = json_manager.read_json()
    for user in users:
        if user['id'] == id:
            if nombre is not None:
                user['nombre'] = nombre
            if apellido is not None:
                user['apellido'] = apellido
            break    
    json_manager.write_json(users)    
    print(f"User with id {id} updated successfully")






if __name__ == '__main__':
    cli()

