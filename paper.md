title: 'ATLaS: An assistant software for researchers to use in calculations for the preparation of solutions'
tags:
  - ATLaS
  - Python
  - Tkinter
  - Pandas
  - solution
authors:
  - name: Ugur Comlekcioglu^
    orcid: 0000-0001-9093-4496
    affiliation: 1
  - name: Nazan Comlekcioglu^
    orcid: 0000-0001-7729-5271
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

# Software Description

ATLaS is platform-independent software that can be run under all operating systems. It has been licensed under MIT and freely available at https://github.com/cugur1978/ATLaS.
ATLaS was developed using Python 3.8.5, an interpreted object-oriented high-level programming language that has become broadly adopted in the scientific community due to its clean syntax with uncomplicated semantics that make it instictive to learn [7]. PyCharm 2020.3.2 was used as the coding editor. PyCharm offers a smart code editor and a powerful graphical debugger [11]. Tkinter package was used to design a graphical user interface for the ATLaS software. Tkinter library is used to construct the GUI that contain frames, buttons, text boxes etc. Tkinter supplies availability to link scripts and functions with press of buttons and display the result text on text viewer [10].

ATLaS is designed to consist of 5 main modules. The flow chart used in the design of the software is given in Figure 1. The modules used in the calculation of percent and molar solutions contain 3 functions each. These functions perform (1) calculation of percent / molar solutions, (2) dilution and (3) percent / molar conversions. Chemicals in Acid & Base and Buffer Modules are presented to the user as a list. Information such as empirical formula, formula weight of these chemicals are saved in Microsoft Excel files. ATLaS makes calculations by calling these values from the Excel files. Unit Converter module performs concentration conversions under volume, mass and density options. PyInstaller was used to convert ATLaS to standalone executable application. PyInstaller collect the packages used in the python software and converting them locally installed packages in the directory of the software where the software can retrieve any function from this packages on this directory instead of calling the packages and function on system.

Acid & Base Solution module in ATLaS contains 16 acids and bases.  The formulas, formula weights and equivalent values of these chemicals are called from the Excel file. The researcher could add more acid and bases to this Excel file, thus the chemical database could be expanded by the user. However, density and weight percentage values are requested from the user. This is because these values may differ according to the brands of chemicals used in laboratories. As an example, In Figure 5, when phosphoric acid is selected from the list and the relevant fields are filled, the outputs can be seen when the molarity or normality buttons are pressed. Instead of giving the calculated values directly to the user, the preparation of the solution comes as a recipe as more understandable laboratory instructions. For this, the calculated values are assigned to the defined variables and placed in the codes containing instructions. For example, the calculations required to prepare 0.5 M and 0.5 N phosphoric acid solutions are shown in the application in Figure 1.

# Discussion

Python was choosen to develop the ATLaS, because Python is a prominent programming language due to its open syntax, active developer community, free availability, widespread use in scientific communities such as bioinformatics, and many free libraries [8]. Open-source software development has had remarkable effect on scientific research. The open-source code of ATLaS enables the developers to be able to better understand the methodology and reproduce the results. Additionaly, the retainability of softwares after publication is presumably the most important problem faced by scientists who develop it [19], therefore ATLaS uploaded to GitHub which is a popular web-based hosting services for Git version control. GitHub provides an useful software development platform, wherein developers can upload their open-source projects. The most important issue in a repository is having a license that clearly defines the permissions and restrictions attached to the code and other files in the repository [17]. Since ATLaS was deposited in GitHub under the license of MIT which gives permissions without limitation to use, copy and modify, it is possible for other developers to develop this software.

The ultimate goal of ATLaS is to assist wet-lab scientist with various domains in laboratory researches. As a first domain in this software, we developed a calculator for preparing solutions in experimental studies. In this domain, we focused our attention on reducing calculation errors in solution preparation by researchers. Thus, this domain allows researchers to prevent time, labor and financial losses by hindering experimental errors raised from faulty calculations in solution preparation. Although solution calculations are made on various websites on the Internet, not every site can meet all the calculations needed. For this reason, the researcher may have to navigate various sites to make the calculation he wants. Also, the lab may not have stable internet access or internet connection speeds may be low. ATLaS collects the calculations that may be needed while preparing solutions by life scientists in a single software. It does not require internet connection with its stands-alone structure. The versatility of a program comes from the variety of functions it has. ATLaS includes a total of 10 functions under 5 modules. The modules and the overall functions of ATLaS were illustrated in Figure 2. A function is a block of code that expresses the solution to a small, independent problem or task. Structuring a program by functions also helps with the modularity and interpretability of the program code and ultimately simplifies the debugging process - an important consideration in all programming projects [7].

The modular development of ATLaS provided an advantage in debugging. The modules written separately were brought together after the errors were corrected. In this way, the codes can be read more easily for those who want to develop ATLaS by cloning. A good GUI makes an application intuitive and easy to use. Tkinter which is default graphical user interface widget set for Python, was used for GUI. Tkinter has was selected because of its availability on all operating systems [20]. Graphical user interfaces allow the user to send information into the program without accessing the code [16]. One of our main purposes was that ATLaS 'GUI had a simple interface. It can be confusing to present all parameters in a single interface, so ATLaS is designed modularly. Thus, even the first person to use the program can make calculations without difficulty. Taking into account the difference of the solutions or chemicals needed in different laboratories, ATLaS allows the researcher to create a chemical database in Acid-Base and Buffer solution modules. The information in these modules is called from the Microsoft Excel file located in the same folder as ATLaS. Python language uses the Pandas library for processing spreadsheet-format data such as Excel and therefore to read the data in Excel files, Pandas library was imported to ATLaS. If the researcher enters the informations of the chemicals required, depending on the format in the Excel file, ATLaS will use these information in calculations. Finally, calculation results are reported to the user as a recipe. Thus, the results were made more understandable especially for students and young researchers who start working in research laboratories.

# Conclusion

We took into account “Release early, release often” as an open-source mantra, and reported the first version of ATLaS in this study. We aim to present new versions to researchers by adding different modules to ATLaS. Scientific software development is an significant need that has to be fullfilled. As scientists, we need assistant softwares that will standardize laboratory protocols and calculations. Development of open-source software is a highly collective process and therefore our expectation is that different scientists and software developers will be involved in the development of ATLaS.

# Conflict of Interest

We wish to confirm that there are no known conflicts of interest associated with this publication and there has been no significant financial support for this work that could have influenced its outcome.
