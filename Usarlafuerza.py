mochi = ['campera', 'soga', 'linterna', 'sable de luz', 'botella de agua']


def fuerza(moch, objsacados=0):

  if len(mochi) == 0:
    print('Mochi vacia')
    return objsacados

  objeto = mochi.pop(0)
  objsacados += 1

  if objeto == 'sable de luz':
    print(
      f'Despues de sacar {objsacados-1} items, encontró el sable.'
    )
  else:
    objsacados = fuerza(mochi, objsacados)

  return objsacados


objsacados = fuerza(mochi)
print(objsacados)
