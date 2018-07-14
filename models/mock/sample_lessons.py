#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:54:16 2018

@author: praveen
"""

from models.common import *
from models.activities import *
from models.courses import Lesson

# glossary, answer definitional questions - done
# review messages and add ssml for naturalized tts - done
# implement basic search by title, should be invoked from fallback
# deep linking intents and fallback handling, talk to miss fiona about weather
# intelligent fallbacks, universals
# system events - actions_PLAY_GAME - snake words
# learning paths - recommendations
# push messages
lessons = [
  Lesson(**{
    "id": "8SoStdsL1",
    "name": "Our Solar System",
    "courseId": "8SoStds", 
    "description": "8th Grade Social Studies",
    "materials": [
        Video(**{
          "id":"v001",
          "title":'Video: Planets of our Solar System',
          "url":'https://www.youtube.com/watch?v=libKVRa01L8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/c/cb/Planets2013.svg'
        }),
        Text(**{
            "id":"t001",
            "title":'Read: Our Sun',
            "text":'''The Sun is a star like many others in our Milky Way galaxy. 
              It has existed for a little over 4.5 billion years, and is going to continue 
              for at least as long. The Sun is about a hundred times as wide as the Earth. 
              It is 333,000 times the mass of the Earth. 
              The Earth can also fit inside the Sun 1.3 million times.''',
            "ssmlText":'''<speak><s>The Sun is a star like many others in our Milky Way galaxy. </s>
              <s>It has existed for a little over 4.5 billion years, and is going to continue 
              for at least as long.</s> <s>The Sun is about a hundred times as wide as the Earth. </s>
              <s>It is 333,000 times the mass of the Earth. </s>
              <s>The Earth can also fit inside the Sun 1.3 million times.</s><speak>''',
            "imageUri":'https://upload.wikimedia.org/wikipedia/commons/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg'              
        }),
        Text(**{
            "id":"t002",
            "title":'Read: Our Solar System',
            "text":'''The Solar System is the Sun and all the objects that orbit around it. 
              The Sun is orbited by planets, asteroids, comets and other things. It is billions of years old.

              The Sun is a star. It contains 99.9 percent of the Solar System's mass. This means that it has strong gravity. 
              The other objects are pulled into orbit around the Sun. The sun is mostly made out of hydrogen and helium.

              There are eight planets in the Solar System. From closest to farthest from the Sun, 
              they are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. 
              The first four planets are called terrestrial planets. They are mostly made of rock and metal, and they are mostly solid. 
              The last four planets are called gas giants. This is because they are much larger than other planets and are mostly made of gas.

              The Solar System also contains other things. There are asteroids, mostly between Mars and Jupiter. 
              Further out than Neptune, there is the Kuiper belt and the scattered disc. These areas have dwarf planets, including Pluto. 
              There are thousands of very small objects in these areas. There are also comets, centaurs, and there is interplanetary dust.''',
            "imageUri":'https://upload.wikimedia.org/wikipedia/commons/9/9f/Solarmap.png'
        }),
        Link(**{
            "id":"l001",
            "title":'Link: NASA Science - Solar System Exploration',
            "url":'https://solarsystem.nasa.gov/planets/sun/indepth',
            "imageUri":'https://upload.wikimedia.org/wikipedia/commons/9/9f/Solarmap.png'
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/c/c3/Solar_sys8.jpg',
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
          "id":"v011",
          "title":'Video: Layers of Earth',
          "url":'https://www.youtube.com/watch?v=3xLiOFjemWQ',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/0/07/Earth_poster.svg'
        }),
        Text(**{
          "id":"t011",
          "title":'Read: Structure of the Earth',
          "text":'''The structure of the Earth is divided into layers. 
            These layers are both physically and chemically different. 
            The Earth has an outer solid crust, a highly viscous mantle, a liquid outer core, 
            and a solid inner core.The shape of the earth is an oblate spheroid, 
            because it is slightly flattened at the poles and bulging at the equator.
            The crust is the outermost layer of the Earth. It is made of solid rocks.
            The mantle is the layer of the Earth right below the crust. 
            The Earth's core is made of solid iron and nickel, and is about 5000–6000 centigrade.''',
          "imageUri":"https://upload.wikimedia.org/wikipedia/commons/e/ee/Earth-crust-cutaway-english.svg"
        }),
        Audio(**{
          "id":"a011",
          "title":'Recorded Audio - Earth\'s structure',
          "url":'https://gnext18-v5.appspot.com/play/Structure_of_earth.mp3',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/5/58/Slice_earth.svg'
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg',
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
          "id":"v021",
          "title":'Video: Cell structure and function',
          "url":'https://www.youtube.com/watch?v=URUJD5NEXC8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/5/5a/Average_prokaryote_cell-_en.svg'
        }),
        Text(**{
          "id":"t021",
          "title":'Read: The Cell',
          "text":'''The cell is the basic structural, functional, and biological unit of all known living organisms. 
            A cell is the smallest unit of life. Cells consist of cytoplasm enclosed within a membrane.
            Cells are of two types: eukaryotic, which contain a nucleus, and prokaryotic, which do not. 
            Prokaryotes are single-celled organisms, while eukaryotes can be either single-celled or multicellular.''',
          "imageUri":"https://upload.wikimedia.org/wikipedia/commons/8/83/Celltypes.svg"
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/a/a7/Structure_of_animal_cell.JPG',
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
          "id":"v031",
          "title":'Video: Cell Division',
          "url":'https://www.youtube.com/watch?v=84mA-MzNJKA',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/d/df/Three_cell_growth_types.svg'
        }),
        Text(**{
          "id":"t031",
          "title":'Read: Mitosis',
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
            ''',
          "imageUri":"https://upload.wikimedia.org/wikipedia/commons/e/e0/Major_events_in_mitosis.svg"
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/3/37/Wilson1900Fig2.jpg',
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

activity_id_dict=dict()
for l in lessons:
  for m in l.materials:
      activity_id_dict[m.id]=m
