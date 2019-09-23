# Mongo_Project

You recently created a new company in the `GAMING industry`. The company will have the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President

As a data engineer you have asked all the employees to show their preferences on where to place the new office.
Your goal is to place the **new company offices** in the best place for the company to grow.
You have to found a place that more or less covers all the following requirements.
Note that **it's impossible to cover all requirements**, so you have to prioritize at your glance.

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan

# SRC

MAIN_Project:
    
        1 - Coenctamos con Pymongo
        2 - Asociamos el dataset companies a un dataframe
        3 - Echamos un primer vistazo al dataframe
        4 - Creamos query para filtrar las empresas que nos interesan
        5 - Se crean las funciones para conseguir la latitud y longitud de las oficinas seleccionadas
        6 - Creamos la funcion GEO para añadir las columna 'position' para poder crear el indice en mongo
        7 - Exportamos el dataframe a un archivo .json
        
MAIN_Project2:

        1 - Conectamos nuevamente con Pymongo despues de crear el indice en Mongo
        2 - Creamos la columna cities para conocer cual es la cidad en la que mas oficinas hay con query seleccionada
        3 - Creamos la funcion GEONEAR para poder sacar las posiciones de la ciudad elegida
        4 - Exportamos los resultados a un archivo .json
        
API_STB:

        1 - Debido a que los ejecutivos les gusta mucho tomar cafe en Starbucks, la oficina la situamos cercana a un a de ellos
        2 - Starbucks mas cercano lo tienen a 374m
        
API_McDonals:

        1 - Aunque el CEO se pronuncie como un una persona con gustos veganos, hablando mas detenidamente con él nos confiesa que almuerza             de 2 a 3 veces por semana en un McDonals
        2 - Otra de las caracteristicas que introducimos a la hora de la ubicacion de la oficina es haber podido posicionarla a tan sólo               270m de una franquicia de McDonals
        
API_Airport:
    
        1 - Debido a la alta frecuendad con la que los Account managers viajan en avión, la ubicación de la oficina esta a tan sólo 14,1               millas del Aeropuerto de San Francisco
        

       
# OUTPUT_INPUT

        1 - Aqui podremos encontrar los 3 mapas, en formato HTML, con las ubicaciones de los Starbucks, McDonals y Aeropuerto
        2 - Encontraremos tambien todos los archivos json con los que hemos ido trabajando en las distintas partes del proyecto



