# -*- coding: utf-8 -*-
""" combispans.py
Created on Sun Jun 18 19:46:22 2023

@author: arolm

Generación de spans a partir de combinaciones.
"""

def combispan(*combis):
  """
  Genera un span a partir de listas de elementos a combinar.
  combispan(combi1, combi2, ..., combiN)
  combispan("lsf", combi1, combi2, ..., combiN)
  combispan("msf", combi1, combi2, ..., combiN)
  """
  
  # Gestión de argumentos de entrada: -----------------------------------------
  ssort = "lsf"
  if isinstance(combis[0], str): ssort, combis = combis[0], combis[1:]

  if ssort=="msf":
    combis = combis[-1::-1]
  elif ssort!="lsf":
    raise Exception("ssort argument must be 'msf' or 'lsf'")
  
  # Inicialización: -----------------------------------------------------------
  ncombis = len(combis) # Número de listas de combinación.
  lcombis = [] # Longitud de cada lista de combinación.
  ccombis = [0]*ncombis # Cursores de cada lista de combinación.
  ncases = 1 # Número total de casos.
  for combi in combis:
    lcombi = len(combi)
    ncases = ncases*lcombi
    lcombis.append(lcombi)
  #end for
  # end Inicialización --------------------------------------------------------
  
  # Barrido -------------------------------------------------------------------
  _combispan = [[] for icombi in range(0, ncombis)]
  for icase in range(0, ncases):
    overflow = 1
    # Para cada lista de combinación:
      # Se descarga el valor apuntado por el cursor.
      # Se actualiza el cursor.
    for icombi in range(0, ncombis):
      # Descarga del valor apuntado por los cursores.
      combi, ccombi, lcombi = combis[icombi], ccombis[icombi], lcombis[icombi]
      vcombi = combi[ccombi]
      _combispan[icombi].append(vcombi)
      # Actualización de los cursores.
      ccombi = ccombi + overflow
      if ccombi==lcombi:
        ccombi = 0
        overflow = 1
      else:
        overflow = 0
      #end if-else
      ccombis[icombi] = ccombi
    #end for
    
  #end Barrido ----------------------------------------------------------------
  
  # Return:
  if ssort=="lsf":
    return _combispan
  else:
    return _combispan[-1::-1]
  
#end def _combideroll ---------------------------------------------------------

# main: for test purpose ------------------------------------------------------
if __name__ == "__main__":
  ndspan1 = combispan([1,2,3], [1,2])
  ndspan2 = combispan('msf', [1,2,3],[1,2])
  ndspan3 = combispan('lsf', [1,2,3],[1,2])