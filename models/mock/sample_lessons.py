#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:54:16 2018

@author: praveen
"""

from models.common import *
from models.courses import Lesson

lessons = [
  Lesson(**{
    "id": "8SoStdsL1",
    "name": "Our Solar System",
    "courseId": "8SoStds", 
    "description": "8th Grade Social Studies",
    "materials": [
        Video(**{
          "title":'Planets of our Solar System',
          "url":'https://www.youtube.com/watch?v=libKVRa01L8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/8/8c/Systeme_solaire_fr.jpg'
        }),
        Text(**{
            "title":'Our Sun',
            "text":'''The Sun is a star like many others in our Milky Way galaxy. 
              It has existed for a little over 4.5 billion years, and is going to continue 
              for at least as long. The Sun is about a hundred times as wide as the Earth. 
              It is 333,000 times the mass of the Earth. 
              The Earth can also fit inside the Sun 1.3 million times.'''
        }),
        Text(**{
            "title":'Our Sun',
            "text":'''The Sun is a star like many others in our Milky Way galaxy. 
              It has existed for a little over 4.5 billion years, and is going to continue 
              for at least as long. The Sun is about a hundred times as wide as the Earth. 
              It is 333,000 times the mass of the Earth. 
              The Earth can also fit inside the Sun 1.3 million times.'''
        }),
        Link(**{
            "title":'NASA Science - Solar System Exploration',
            "url":'https://solarsystem.nasa.gov/planets/sun/indepth'
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/8/8c/Systeme_solaire_fr.jpg',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  }),
  Lesson(**{
    "id": "8SoStdsL2",
    "name": "Our Earth",
    "courseId": "8SoStds", 
    "description": "8th Grade Social Studies",
    "materials": [
        Video(**{
          "title":'Layers of Earth',
          "url":'https://www.youtube.com/watch?v=3xLiOFjemWQ',
          "imageUri":'https://3.bp.blogspot.com/-MCsbIihWzMI/V8zLCDW1VAI/AAAAAAAAGyQ/iCEhWGNn5cQx7Q6zz2CsEn0oHxs80NiMwCLcB/s1600/layers-of-earth.gif'
        }),
        Text(**{
          "title":'Structure of the Earth',
          "text":'''The structure of the Earth is divided into layers. 
            These layers are both physically and chemically different. 
            The Earth has an outer solid crust, a highly viscous mantle, a liquid outer core, 
            and a solid inner core.The shape of the earth is an oblate spheroid, 
            because it is slightly flattened at the poles and bulging at the equator.
            The crust is the outermost layer of the Earth. It is made of solid rocks.
            The mantle is the layer of the Earth right below the crust. 
            The Earth's core is made of solid iron and nickel, and is about 5000–6000 centigrade.''',
          "imageUri":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Earth-crust-cutaway-english.svg/995px-Earth-crust-cutaway-english.svg.png"
        })
    ],
    "imageUri":'https://3.bp.blogspot.com/-MCsbIihWzMI/V8zLCDW1VAI/AAAAAAAAGyQ/iCEhWGNn5cQx7Q6zz2CsEn0oHxs80NiMwCLcB/s1600/layers-of-earth.gif',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  }),
  Lesson(**{
    "id": "8ScnceL1",
    "name": "The Cell",
    "courseId": "8Scnce", 
    "description": "8th Grade Science",
    "materials": [
        Video(**{
          "title":'Cell structure and function',
          "url":'https://www.youtube.com/watch?v=URUJD5NEXC8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png'
        }),
        Text(**{
          "title":'The Cell',
          "text":'''The cell is the basic structural, functional, and biological unit of all known living organisms. 
            A cell is the smallest unit of life. Cells consist of cytoplasm enclosed within a membrane.
            Cells are of two types: eukaryotic, which contain a nucleus, and prokaryotic, which do not. 
            Prokaryotes are single-celled organisms, while eukaryotes can be either single-celled or multicellular.''',
          "imageUri":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Celltypes.svg/450px-Celltypes.svg.png"
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  }),
  Lesson(**{
    "id": "8ScnceL2",
    "name": "Cell Division",
    "courseId": "8Scnce", 
    "description": "8th Grade Science",
    "materials": [
        Video(**{
          "title":'Cell Division',
          "url":'https://www.youtube.com/watch?v=84mA-MzNJKA',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Three_cell_growth_types.png/400px-Three_cell_growth_types.png'
        }),
        Text(**{
          "title":'Cell Division',
          "text":'''Cell division is the process by which a cell, called the parent cell, divides into two cells, called daughter cells. 
            When the cell divides, everything inside it divides also. The nucleus and the chromosomes divide, and the mitochondria divide also.
            Mitosis is part of the cycle of cell division. The chromosomes of a cell are copied to make two identical sets of chromosomes,
            and the cell nucleus divides into two identical nuclei.
            Before mitosis, the cell creates an identical set of its own genetic information – this is called replication. 
            The genetic information is in the DNA of the chromosomes. At the beginning of mitosis the chromosomes wind up and 
            become visible with a light microscope. The chromosomes are now two chromatids joined at the centromere. 
            Since the two chromatids are identical to each other, they are called sister chromatids.
            Mitosis happens in all types of dividing cells in the human body except with sperm and ova. 
            The sperm and ova are gametes or sex cells. The gametes are produced by a different division method called meiosis.
            Meiosis is a special type of cell division. Unlike mitosis, the way normal body cells divide, 
            meiosis results in cells that only have half the usual number of chromosomes, one from each pair. 
            For that reason, meiosis is often called reduction division. In the long run, meiosis increases genetic 
            variation, in a way which will be explained later.''',
          "imageUri":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Three_cell_growth_types.png/400px-Three_cell_growth_types.png"
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  })
]

lesson_id_dict=dict()
for l in lessons:
  lesson_id_dict[l.id]=l

courses_id_dict=dict()
for l in lessons:
  if courses_id_dict.get(l.courseId) is None:
    courses_id_dict[l.courseId]=[]
  courses_id_dict[l.courseId].append(l)
  