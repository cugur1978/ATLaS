---
title: 'ATLaS: An assistant software for researchers to use in calculations for the preparation of solutions'
tags:
  - ATLaS
  - Python
  - Tkinter
  - Pandas
  - solution
authors:
  - name: Ugur Comlekcioglu^[Custom footnotes for e.g. denoting who the corresponding author is can be included like this.]
    orcid: 0000-0001-9093-4496
    affiliation: 1
  - name: Nazan Comlekcioglu
    affiliation: 2
affiliations:
 - name: Kahramanmaras Sutcu Imam University, Biotechnology Laboratory, Kahramanmaras, Turkey
   index: 1
 - name: Kahramanmaras Sutcu Imam University, Biology Department, Kahramanmaras, Turkey
   index: 2
date: 25 March 2021
bibliography: paper.bib

 
 # Summary
 
 Many solutions such as percentage, molar and buffer solutions are used in all experiments conducted in life science laboratories. 
 Although the preparation of the solutions is not difficult, miscalculations that can be made during intensive laboratory work negatively 
 affect the experimental results. In order for the experiments to work correctly, the solutions must be prepared completely correctly. 
 In this project, a software, ATLaS (Assistant Toolkit for Laboratory Solutions), has been developed to eliminate solution errors arising from 
 calculations.  Python programming language was used in the development of ATLaS. Tkinter and Pandas libraries were used in the program. 
 ATLaS contains five main modules (1) Percent Solutions, (2) Molar Solutions, (3) Acid-Base Solutions, (4) Buffer Solutions and (5) Unit Converter. 
 Main modules have sub-functions within themselves. With PyInstaller, the software was converted into an stand-alone executable file. 
 ATLaS is freely available for download at https://github.com/cugur1978/ATLaS. 
 
 # Statement of need 
 
 There is a high demand for computer-based support for diverse scientific research, but the software that suits the need cannot always be found [12, 14]. 
 While researchers lack the necessary programming skills to develop the required software, software developers are generally unfamiliar with scientific 
 research [21].  Although it is necessary to conduct interdisciplinary studies to solve this problem, it is important to train software developers who are 
 experts in certain  scientific fields [6, 5]. Because the cooperation to be achieved by the design, development and distribution of free software by 
 scientists will enable researchers to spend more time on their research [15]. 
 
 Using programming languages such as C ++, Python, Fortran or Pearl, a variety of software, pipelines and packages have been developed to meet all analysis 
 demands of scientific or industrial researchers. Examples of these software include  BioCoder [1], Tellurium [4], Biotite [13]. Various web-based tools 
 allow researchers to handle their studies outside of the command-line environment;  however, these programs need a stable internet connection and thus 
 hinder offline analysis. Internet-free software with a graphical user interface (GUI) has greatly helped researchers in their work [3].

The place of experimental study in laboratories has always supposed a high profile at all levels of science. However, errors in laboratory experiments can 
occur in any step of the process.  Casadevall et al. [2] reported that more than half of all error‐related retractions were attributed to laboratory error. 
Experimental errors have negative effects in terms of cost, time and effort. In addition, insufficient description of materials and methods limits the 
reproducibility of the scientific researches [18]. Methods reproducibility mentions to the providing of adequate detail about study protocols and data so 
the same protocols could, in theory or in actuality, be completely repeated [9]. Protocols need to be highly detailed in order to reduce experimental errors 
and increase the reproducibility of experiments. However, methods are explained in the literature without providing a complete and self-contained account 
of the steps taken [1]. 

In this study, we are introducing a stand-alone software ATLaS (Assistant Toolkit for Laboratory Solutions), which is an assistant 
tool that compresses simple and common calculations of solutions with a user-friendly GUI. This toolkit developed to save time and energy of wet-lab researchers 
from various calculations of preparing solutions. Additionally, the purpose of this software is to minimize calculation errors in solution preparation in experiments. 
ATLaS source code is freely available, where its code could be modified, extended or integrated in different laboratory software pipelines. ATLaS is a simple 
package software implements a variety of calculations to preparing common solutions on different scientific experiments. Considering that not every laboratory 
has access to the internet, ATLaS is intended to be a software independent from the internet.

 
