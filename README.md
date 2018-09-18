# alg-geneticos-python
	ciudades=[]
    ciudades.extend([ciudad("Buenos Aires",-34.599722, -58.381944]))
    ciudades.extend([ciudad("Córdoba",-31.416667, -64.183333))
    ciudades.extend([ciudad("S. F. del valle de Catamarca",-28.468611, -65.779167))
    ciudades.extend([ciudad("Resistencia",-27.451389, -58.986667))
    ciudades.extend([ciudad("Rawson",-43.3, -65.1))
    ciudades.extend([ciudad("Corrientes",-27.483333, -58.816667))
    ciudades.extend([ciudad("Paraná",-31.744444, -60.5175))
    ciudades.extend([ciudad("Formosa",-26.184722, -58.175833))
    ciudades.extend([ciudad("San S. de Jujuy",-24.185556, -65.299444))
    ciudades.extend([ciudad("Santa Rosa",-36.620278, -64.290556))
    ciudades.extend([ciudad("La Rioja",-29.413056, -66.855833))
    ciudades.extend([ciudad("Mendoza",-32.883333, -68.833333))
    ciudades.extend([ciudad("Posadas",-27.366667, -55.896944))
    ciudades.extend([ciudad("Neuquén",-38.95735, -68.045533))
    ciudades.extend([ciudad("Viedma",-40.8, -63))
    ciudades.extend([ciudad("Salta",-24.788333, -65.410556))
    ciudades.extend([ciudad("San Juan",-31.5375, -68.536389))
    ciudades.extend([ciudad("San Luis",-33.277222, -66.3525))
    ciudades.extend([ciudad("Rio Gallegos",-51.633333, -69.233333))
    ciudades.extend([ciudad("Santa Fe",-31.633333, -60.7))
    ciudades.extend([ciudad("Santiago del Estero",-27.784444, -64.266944))
    ciudades.extend([ciudad("Ushuaia",-54.807222, -68.304444))
    ciudades.extend([ciudad("S. M. de Tucumán",-26.816667, -65.216667))
class ciudad:
	def __init__(self,nombre,lat,lon):
        self.nombre=nombre
		self.lat=lat
		self.lon=lon
		self.estado=0
		def setEstado(self,estado):
			self.estado=estado
		def getEstado(self):
			return self.estdao

		
def ciudadesPendientes (thisCity, ciudades):
	closerCity=0
	for x in range (0,23):		
		if (ciudades[x].getEstado() == 1):
			continue
		if (calc_distance(thisCity,ciudades[x])<closerCity):
			closerCity=ciudades[x]
		
			

		
def calc_distance(_lat1, _lon1, _lat2, _lon2):
    """ Use of Haversine Algorithm"""
    
    R = 6373.0
    lat1 = radians(_lat1)
    lon1 = radians(_lon1)
    lat2 = radians(_lat2)
    lon2 = radians(_lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return int(R * c)
	
	
	print ("Ingrese ciudad inicial")
	x=int(readline()
	lastCity=ciudades[x]
	ciudades[x].estado=1
	
	
	
	for 
	
