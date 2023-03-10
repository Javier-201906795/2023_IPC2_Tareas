#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
    
    def obtenerDato(self):
        return self.dato
    
    def obtenerSiguiente(self):
        return self.siguiente
    
    def asignarDato(self, nuevodato):
        self.dato = nuevodato
    
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
        




class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None
    
    def getcabeza(self):
        return self.cabeza
    
    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self, item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    
    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
            
        return contador
    
    def buscar(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    
    def remover(self, item):
        actual = self.cabeza
        anterior = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                anterior = actual
                actual = actual.obtenerSiguiente()
        
        if encontrado:
            if anterior == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                anterior.asignarSiguiente(actual.obtenerSiguiente())
                
            print("eliminado")


    

    def anexar(self, item):
        #[A] 1.0 Encontrar ultimo apuntador
        actual = self.cabeza
        anterior = None
        encontrado = False
        while not encontrado:
            #[A] 1.1 Buscar siguiente = None
            if actual.obtenerSiguiente() == None:
                encontrado = True
            else:
                anterior = actual
                actual = actual.obtenerSiguiente()
        #[A] 2.0 Agregar item
        #[A] 2.1 Crear Nodo
        ultimo = Nodo(item)
        #[A] 2.2 Cambiar siguente por nuevo Nodo
        actual.asignarSiguiente(ultimo)

        
        #print(actual.obtenerDato())
        #print(actual.obtenerSiguiente())
        #print("anexado con exito")
        

    def indice(self,item):
        #[B] 1.0 Buscar item
        actual = self.cabeza
        anterior = None
        encontrado = False
        contador = 0
        while not encontrado and actual != None:
            #[B] 1.1 Guardar posicion
            contador += 1
            #[B] 1.2 Buscar item
            if actual.obtenerDato() == item :
                encontrado = True
            else:
                anterior = actual
                actual = actual.obtenerSiguiente()


        #[B] 1.3 Retornar Ubicacion
        # posicion = numeronodostotal - contador + 1
        posicion = self.tamanio() - contador 
        
        return posicion
    

    def insertar(self,pos,item):
        #[C] Inserta un nuevo item en una posicion especificada
        #[C] 1.0 Buscar Item en esa posicion
        #[C] 1.1 Obtener posicion en el listado 
        posicionlistado = int(self.tamanio()) - pos
        #[C] 1.2 Encontrar item a remplazar posicion (-1)
        actual = self.cabeza
        anterior = None
        for i in range(0, posicionlistado - 1):
            anterior = actual
            actual = actual.obtenerSiguiente() 
        #[C] 2.0 Crear Nuevo Nodo
        newNodo = Nodo(item)
        #[C] 3.0 Insertar nuevo nodo
        #[C] 3.1 Cambiar apuntador del Nuevo Nodo
        newNodo.asignarSiguiente(actual.obtenerSiguiente())
        #[C] 3.2 Cambiar apuntador Nodo Actual
        actual.asignarSiguiente(newNodo)

    def extraer(self,pos):
        #[D] Eliminar nodo por posicion
        #[D] 1.0 Encontrar posicion nodo anterior (-2)
        repeticionesfor = int(self.tamanio()) - pos  -2
        
        #[D] 1.1 Encontrar nodo anterior
        actual = self.cabeza
        anterior = None
        if repeticionesfor >=0 :
            for i in range(0, repeticionesfor):
                anterior = actual
                actual = actual.obtenerSiguiente()
        
            #[D] 2.0 Remplazar apuntadores
            #[D] 2.1 Obtener Nodos
            nodoaeliminar = actual.obtenerSiguiente()
            nodosiguiente = nodoaeliminar.obtenerSiguiente()
            #[D] 2.2 Remplazar Nodos
            actual.asignarSiguiente(nodosiguiente)
            print("Nodo Eliminado [ "+nodoaeliminar.obtenerDato() +" ]")
            return nodoaeliminar
        else:
            #CUANDO ES EL UTLIMO NODO
            #[D] 2.2 Remplazar Nodos
            temp = self.cabeza.obtenerSiguiente()
            self.cabeza = temp
            print("Nodo Eliminado [ "+actual.obtenerDato() +" ]")
            return actual

        # return nodoaeliminar

        


miLista = ListaNoOrdenada()



miLista.agregar("Juan")



miLista.agregar("Pedro")


miLista.agregar("Jose")

miLista.tamanio()


# In[29]:


miLista.anexar("Mario")




# In[30]:

miLista.tamanio()


# In[31]:

miLista.indice("Juan")

# In[32]:

miLista.indice("Mario")


# In[]:
miLista.indice("Juan")
# In[]:
miLista.indice("Pedro")
# In[]:
miLista.indice("Jose")
# In[33]:

miLista.insertar(2,"Pancho")

# In[31]:

miLista.indice("Pancho")


# In[34]
miLista.extraer(2)

# %%
