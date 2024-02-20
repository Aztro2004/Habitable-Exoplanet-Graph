# Exoplanet-similarity-filter
# Description
Exoplanet similarity filter
## Members and Contact
* José Ángel López Gutiérrez | jalg030129@gmail.com
* Erika Monserrat Correa Hernández | erikacorreahdezene@gmail.com
* Diego Maldonado Castro  | thebrogrrs@gmail.com
# License
GNU General Public License v3.0
# Affilation
Final project for the 2024-2 Distributed Computing (Cloud Computing) class, designed and developed at the Universidad Nacional Autonoma de México(UNAM), at the Escuela Nacional de Estudios Superiores (ENES Morelia). This project is carried out by students of the Bachelor's Degree in Technologies for Information in the Sciences.
# Introduction
Exploration of the planets has advanced significantly with modern technology, including advanced telescopes and space missions, profoundly expanding our knowledge of the solar system and the universe.

This study is key to understanding the formation of the solar system, contributes to the protection of the Earth against cosmic threats, maintains the orbital stability of the solar system through its masses and gravities avoiding collisions, helps regulate temperature by absorbing and reflecting solar radiation influencing the Earth's climate, also allows us to understand its development, its orbital movements and therefore its climatic conditions, is essential for space exploration, facilitating the planning of missions, offers us perspectives on the formation and evolution of the solar system and therefore promotes technological advances with terrestrial applications. 


For these reasons it seems to us of great importance to contribute and help the study of the planets, their characteristics, the similarities they have with each other can be visualized in a more friendly way, so we will develop a filter with the help of information provided by an API and NASA that gives us real and reliable data of the different planets some of its characteristics such as the year they were discovered, the method they used for discovery, the place where it was discovered and other parameters with specific data that can help experts in the field to determine the changes that may have the planets in a given time, or even to know data that did not know the specific planet, facilitating the recognition of patterns in certain time.

# Justification

The making of this project has an objective of giving the user an easy to use solution to a problem that we can see on the NASA platform of exoplanets. What is that problem? The internet connection that is obligatory to access to the filters and also the flexibility of the platform in terms of customization and visualization of some other data. 

So, we want to offer a solution to users who use this platform on how they access to the information that they want based on characteristics of the exoplanet, and give them tools to visualize the data, even helping to see patterns on it. It may then offer an easy to use tool when no internet is available or, if the user itself wants to go deeper on observations of the data thanks to the flexibility of this program. 
  
# Hypothesis
The problem issues several objectives that we want to put this way: Can this task be done on a fast and easy way for the user even if its not a computer science person? The way we see it, we state that is possible; having defined the variables that are attached to exoplanets by the NASA,  we can program a tool to read, filter and show the info that a CSV from the web page. 

## Objectives
* Implement a mechanism to retrieve planet data from the NASA Exoplanet Archive or a similar database.
* Ease the recognition of characteristics between planets.
* Identify key features of planets that determine similarity.
* Filter planets given a planet of reference and its metrics.
* Implement a search algorithm that uses the similarity metric to find planets similar to the given planet.
# Tools
* API Expo Planet Archive | https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS
* Python 3
* Library of the Python:
    * Pandas
    * Numpy
    * Request
    * Mathplotlib
    * scikit-learn
    * scipy.spatial.distance
    * seaborn
    * astroquery
    * mysql
* For Databases:
   * Datasets of Pandas
   * MySQL
* Others:
   * Bash
   * Docker
   * AWS
   * 
# General System Architecture
