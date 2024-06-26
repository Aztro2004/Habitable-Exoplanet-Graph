# Habitable Exoplanet Graph
## Members and Contact
* José Ángel López Gutiérrez | jalg030129@gmail.com
* Erika Monserrat Correa Hernández | erikacorreahdezenes@gmail.com
* Diego Maldonado Castro  | thebrogrrs@gmail.com
## License
GNU General Public License v3.0
## Affilation
Final project for the 2024-2 Distributed Computing (Cloud Computing) class, designed and developed at the Universidad Nacional Autonoma de México(UNAM), at the Escuela Nacional de Estudios Superiores (ENES Morelia). This project is carried out by students of the Bachelor's Degree in Technologies for Information in the Sciences.
## Introduction
Exploration of the planets has advanced significantly with modern technology, including advanced telescopes and space missions, profoundly expanding our knowledge of the solar system and the universe. 

A habtiable zone is the distance from a star at which liquid water has the possibility of existing on orbiting planets’ surfaces. Habitable zones can also be known as Goldilocks’ zones, where conditions might be  neither too hot nor too cold for life. 


Thid is were the Habitable Graph Simulator Project comes in. This project emerges from building on the foundation laid by the information already given about exoplanets. This project seeks to leverage  simulation technology to create a comprehensive and interactive model of potentially habitable planets within these Goldilocks zones. By synthesizing data from sources, including the NASA exoplanet archive, this Habitable Exoplanet Graphing Project aims to provide a tool for the visualization and study of these distant worlds.

## Justification

This proyect aims to ease the visualization of planets in a habitable zone. By retrieving the numeric data given in the NASA Exoplanet Archive and processing it to display a 3D simulation graph we pretend to ease the visualization of the information that can sometimes be hardly interpreted by someone that doesn't have sufficient knowldedge to understand rough data of an exoplanet.
  
## Hypothesis
Population ingeneral needs to be able to get information about the universe, not just because it helps make us understand better tyhe world but because it satisfies the need of being curious... Education works because there's an easy and sometimes free way of accessing it, so we need to go beyond the barriers and help everyone to reach that goal. 
## General Objetive 
Our overall goal is that anyone who loves astronomy and planets, from the amateur enthusiast, the person curious about habitable planets and even the experienced scientist, can travel through our website and can observe and perform an intuitive search for exoplanets located in habitable zones in an advanced system of data analysis and visualization that we will develop taking advantage of the information that NASA gives us about the planets.

## Particular Objectives
* Implement a mechanism to retrieve planet data from the NASA Exoplanet Archive or a similar database.
* Ease the visualization of planets in a habitable zone.
* Graph planets if they are in a habitable zone.
* Implement a search algorithm that finds exo-planets in the habitable zone.
## Tools
* Database Expo Planet Archive | https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS
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
    *  mpl_toolkits.mplot3d
    * HTML
    * CSS
    * Java Script
    * Docker

* For Databases:
   * Datasets of Pandas

* Others:
   * Bash
   * Docker
   * AWS
   * GIT
     
## General System Architecture

![Diagram_Architecture](https://github.com/Aztro2004/Habitable-Exoplanet-Graph/blob/main/Architecture.jpg)

## Results


As the end of the project arrived, we saw what we can achieve with it, which was the creation and renderization of some exoplanets that, based on the filters we state before, are habitable, and rendered on a 3D image. Also,  even when the csv had some missing data, based on different criterias the orbits and size of the planets are an approximation only.
The result that we got is that filtering that kind of data can be tricky(Not unusual as you may expect for people who aren't familiar with exoplanets), so the file filter.ipynb can be improved with help of professionals that know the topic well. In the end we have a small piece of software that is useful for so many reasons, the first one is that this tool, if upgraded, can help us visualize where all the exoplanets are, in terms of the earth position.



## Conclusion

The making of a system like this involves different kind of knowledges and abilities, some of them we do not possess as a matter of being experts on the topic, beyond that, we feel pleased with the results that we achieve, so if someone comes and uses our software we be sure about they getting some new knowledge, information or at least an idea about how this works on transforming a big csv to a small one, then visualize it and in the end making it a website about it 

