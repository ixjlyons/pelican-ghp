:title: Kenneth R. Lyons
:URL:
:save_as: index.html


.. raw:: html

   <figure style="float: right">
       <img src="../images/north-coast.jpg" width=150 height=150/>
   </figure>

I am a PhD student in the Mechanical and Aerospace Engineering department at UC
Davis. I work in the `Robotics, Autonomous Systems, and Controls Laboratory
(RASCAL) <https://research.engineering.ucdavis.edu/rascal/>`_, where I develop
ways for humans with disabilities to control machines.

My primary research interests include electrophysiological signal acquisition
and processing, the combination of human and machine learning, and their use
for the control of computer and machine interfaces. In English: I'm fascinated
by the fact that our bodies produce electrical signals that can be detected,
understood, and used to control things.


Projects
========

AxoPy
-----

.. image:: https://raw.githubusercontent.com/ucdrascal/axopy/fee97fedd6e4630a2da3457c2180b22994d6c354/docs/_static/axopy.png
    :height: 1.5in
    :alt: AxoPy logo

AxoPy is a Python library aiming to make setting up human-computer interface
experiments as easy as possible.

- `AxoPy on GitHub <https://github.com/ucdrascal/axopy>`_

PyGesture
---------

.. image:: {filename}/images/pygesture-screenshot.png
   :height: 1.5in
   :alt: Screenshot of PyGesture

PyGesture is an open source myoelectric gesture recognition suite for
end-to-end prosthesis control experiments, written in Python. It includes data
acquisition, signal processing, classification, graphical user interface, and
communication with real-time simulation software. Predecessor of AxoPy.

- `PyGesture on GitHub <https://github.com/ixjlyons/pygesture>`_

Walk Again
----------

.. image:: {filename}/images/walkagain-led.jpg
   :height: 1.5in
   :alt: Photo of the Walk Again LED feedback system

Walk Again was an international effort to demonstrate a brain-controlled
exoskeleton at the 2014 World Cup opening ceremony in Brazil. I worked as
a part of the human-machine interface team and created an LED-based feedback
system to enable robust control during the demonstration.

This was a once-in-a-lifetime experience to work on an incredibly fast-paced
project involving academic and industry teams.

- `Mind in Motion`_
- `Article about the project in UC Davis News <walkagain-news_>`_
- `High-impact report on some findings from the project <walkagain-scireports_>`_
- `YouTube video about the project with me in it <https://youtube.com/watch?v=Lco3U600aS4>`_
- `YouTube video of more recent happenings <https://youtube.com/watch?v=PIIXhih5Qpg>`_

.. _Mind in Motion: http://www.nature.com/scientificamerican/journal/v307/n3/full/scientificamerican0912-58.html
.. _walkagain-news: https://www.ucdavis.edu/news/engineers-take-part-walk-again-effort-world-cup-help-disabled
.. _walkagain-scireports: http://www.nature.com/articles/srep30383

MyoSwim
-------

.. image:: https://github.com/ixjlyons/myoswim/raw/master/img/screenshot.png?raw=true
   :height: 1.5in
   :alt: Screenshot of MyoSwim

MyoSwim is a game for demonstrating computer interface control through surface
electromyography at the `World Science Festival`_ in 2015.

It uses the microphone as an input to the plane, allowing for myoelectric
control if an EMG sensor is plugged in to the microphone port (you could blow
or hum into the microphone for control otherwise). The RMS value is calculated
and put through a moving average filter to get the input value. This input
value is used to control the vertical speed of the player, working against
gravity.

It was a lot of fun to make, and demonstrating it at the World Science Festival
was a blast. For the entire day, we had kids of all ages lined up to try it
out.

- `MyoSwim on GitHub <myoswim-gh_>`_

.. _myoswim-gh: https://github.com/ixjlyons/myoswim
.. _World Science Festival: http://www.worldsciencefestival.com/

SecondEyes
----------

.. image:: {filename}/images/secondeyes.png
   :height: 1.5in
   :alt: SecondEyes logo

SecondEyes is a telepresence mobile robot meant to allow individuals with
severe mobility impairments to virtually view their surroundings.
A WiFi-enabled camera mounted on the robot streams video to a custom Android
application which acts as a noninvasive, hands-free control interface based on
a single electromyographic (EMG) sensor. This was my Capstone senior design
project in mechanical engineering which turned into my first graduate research
project.

The robot was first used in a case study in which a man with a high-level
spinal cord injury controlled the robot remotely and navigated a simple maze.
This was presented at the IEEE International Conference on Rehabilitation
Robotics (ICORR) in 2013.

- `ICORR paper <icorr-paper_>`_
- `ICORR poster <icorr-poster_>`_
- `Video of the robot moving around <secondeyes-youtube_>`_

.. _icorr-paper: https://doi.org/10.1109/ICORR.2013.6650428
.. _icorr-poster: https://doi.org/10.5281/zenodo.569066
.. _secondeyes-youtube: https://youtube.com/watch?v=x3-M-UELEkI


Publications
============

Papers
------

.. reference::
   :author: <strong>K. R. Lyons</strong> and S. S. Joshi
   :year: in press
   :title: Upper Limb Prosthesis Control for High-Level Amputees via Myoelectric Recognition of Leg Gestures
   :proc: IEEE Transactions on Neural Systems and Rehabilitation Engineering

.. reference::
    :author: <strong>K. R. Lyons</strong> and S. S. Joshi
    :year: 2016
    :title: Real-Time Evaluation of a Myoelectric Control Method for High-Level Upper Limb Amputees Based on Homologous Leg Movements
    :proc: Proceedings of the IEEE Engineering in Medicine and Biology Society Conference (EMBC)
    :address: Orlando, FL
    :paper: https://doi.org/10.1109/EMBC.2016.7592184

.. reference::
    :author: I. M. Skavhaug, <strong>K. R. Lyons</strong>, A. Nemchuk, S. Muroff, and S. Joshi
    :year: 2016
    :title: Learning to Modulate the Partial Powers of a Single sEMG Power Spectrum Through a Novel Human-Computer Interface
    :proc: Human Movement Science
    :volume: 47
    :pages: 60--69
    :paper: https://doi.org/10.1016/j.humov.2015.12.003

.. reference::
    :author: J. Varley, S. Sridhar, J. Weisz, E. Rand, <strong>K. Lyons</strong>, S. Joshi, J. Stein, and P. Allen
    :year: 2016
    :title: Human Robot Interface for Assistive Grasping
    :proc: Socially & Physically Assistive Robotics for Humanity (workshop at Robotics: Science and Systems)
    :address: Ann Arbor, MI
    :paper: https://allrobotshelping.files.wordpress.com/2016/06/varley2016human.pdf

.. reference::
    :author: <strong>K. R. Lyons</strong> and S. S. Joshi
    :year: 2015
    :title: A Case Study on Classification of Foot Gestures via Surface Electromyography
    :proc: Annual Conference of the Rehabiltation Engineering and Assistive Technology Society of North America (RESNA)
    :address: Denver, CO
    :paper: http://www.resna.org/sites/default/files/conference/2015/pdf_versions/mobility/student_scientific/130.pdf
    :poster: https://doi.org/10.5281/zenodo.569072

.. reference::
    :author: <strong>K. R. Lyons</strong> and S. S. Joshi
    :year: 2013
    :title: Paralyzed Subject Controls Telepresence Mobile Robot Using Novel sEMG Brain-Computer Interface: Case Study
    :proc: Proceedings of the IEEE International Conference on Rehabilitation Robotics (ICORR)
    :address: Seattle, WA
    :paper: https://doi.org/10.1109/ICORR.2013.6650428
    :poster: https://doi.org/10.5281/zenodo.569066

Conference Posters and Abstracts
--------------------------------

.. reference::
    :author: I. M. Skavhaug, <strong>K. R. Lyons</strong>, S. D. Muroff, H. Chen, L. Barry, B. Korte, and S. S. Joshi
    :year: 2016
    :title: Fitts' Law Evaluation of a Passive Rotation Paradigm for Two-Dimensional Cursor Control with a Single sEMG Signal
    :proc: Proceedings of the IEEE Engineering in Medicine and Biology Society Conference (EMBC)
    :address: Orlando, FL
    :poster: https://doi.org/10.5281/zenodo.569067

.. reference::
    :author: <strong>K. R. Lyons</strong> and S. S. Joshi
    :year: 2015
    :title: Real-Time Myoelectric Control of a Virtual Upper Limb Prosthesis via Lower Leg Gestures: Preliminary Results
    :proc: Annual Meeting of the Society for Neuroscience (SfN)
    :address: Chicago, IL
    :abstract: http://www.abstractsonline.com/Plan/ViewAbstract.aspx?sKey=2046f37c-cf96-4c66-a0f7-f5399c3fe08d&cKey=56dab28e-4cd3-4d8e-896e-9e7a3dacf560&mKey=d0ff4555-8574-4fbb-b9d4-04eec8ba0c84
    :poster: https://doi.org/10.5281/zenodo.569075

.. reference::
    :author: I. M. Skavhaug, <strong>K. R. Lyons</strong>, A. Nemchuk, S. Muroff, and S. Joshi
    :year: 2015
    :title: Control of a Cursor in Two Dimensions with One Single sEMG Signal: Learning of a Novel Motor Skill
    :proc: Annual Meeting of the Society for Neuroscience (SfN)
    :address: Chicago, IL
    :abstract: http://www.abstractsonline.com/Plan/ViewAbstract.aspx?sKey=09178b29-16b0-41f6-b923-0fcf29f512da&cKey=b717cbf1-ba51-4d32-9480-0eea713709d5&mKey=d0ff4555-8574-4fbb-b9d4-04eec8ba0c84

.. reference::
    :author: <strong>K. R. Lyons</strong> and S. S. Joshi
    :year: 2014
    :title: Arm Prosthetic Control Through Electromyographic Recognition of Leg Gestures
    :proc: Annual Meeting of the Society for Neuroscience (SfN)
    :address: Washington D.C.
    :abstract: http://www.abstractsonline.com/Plan/ViewAbstract.aspx?sKey=dcf68e43-c9ce-47e4-a9e8-7d6b8f22905c&cKey=8f80aa91-325b-4db2-82e0-b25f5dcb0da1&mKey=54c85d94-6d69-4b09-afaa-502c0e680ca7
    :poster: https://doi.org/10.5281/zenodo.569073

.. reference::
    :author: I. M. Skavhaug, C. Dao, <strong>K. R. Lyons</strong>, A. Powell, L. Davidson, and S. Joshi
    :year: 2014
    :title: Use of an Ear-Mounted Myoelectric Human-Computer Interface in the Home: A Pediatric Case Study with Tetra-Amelia Syndrome Subject
    :proc: Annual Meeting of the Society for Neuroscience (SfN)
    :address: Washington D.C.
    :abstract: http://www.abstractsonline.com/Plan/ViewAbstract.aspx?sKey=37142343-34d0-4aa6-bcd3-56b4e66fb646&cKey=c667f35e-402a-4e23-bcea-d4f5c52d2d87&mKey=54c85d94-6d69-4b09-afaa-502c0e680ca7

.. reference::
    :author: A. Lin, D. Schwarz, R. Sellaouti, S. Shokur,  R. C. Moioli, F. L. Brasil, K. R. Fast, N. A. Peretti, A. Takigami, S. Gallo, <strong>K. R. Lyons</strong>, P. Miettendorfer, M. Lebedev, S. Joshi, G. Cheng, E. Morya, A. Rudolf, and M. Nicolelis
    :year: 2014
    :title: The Walk Again Project: Brain-Controlled Exoskeleton Locomotion
    :proc: Annual Meeting of the Society for Neuroscience (SfN)
    :address: Washington D.C.
    :abstract: http://www.abstractsonline.com/Plan/ViewAbstract.aspx?sKey=88519dd5-ac98-4909-93c8-98ecda0435c6&cKey=72172c8b-154f-46b4-a7c4-5555c437f080&mKey=54c85d94-6d69-4b09-afaa-502c0e680ca7

.. reference::
    :author: F. L. Brasil, R. C. Moioli, S. Shokur, K. Fast, A. L. Lin, N. A. Peretti, A. Takigami, <strong>K. R. Lyons</strong>, D. J. Zielinski, L. Sawaki, S. Joshi, E. Morya, and M. A. P. Nicolelis
    :year: 2014
    :title: The Walk Again Project: An EEG/EMG Training Paradigm to Control Locomotion
    :proc: Annual Meeting of the Society for Neuroscience (SfN)
    :address: Washington D.C.
    :abstract: http://www.abstractsonline.com/Plan/ViewAbstract.aspx?sKey=88519dd5-ac98-4909-93c8-98ecda0435c6&cKey=2dd82c9a-c7fe-4903-be7e-d58ca8014603&mKey=54c85d94-6d69-4b09-afaa-502c0e680ca7


Other Interests
===============

Running
-------

I run around parks and occasionally the UC Davis arboretum in the mornings. I'd
consider myself a somewhat serious hobbyist runner. My favorite distance is
10 km, but I enjoy pushing my distance.

- `Runkeeper <https://runkeeper.com/user/ixjlyons>`_
- `Smashrun <http://smashrun.com/ixjlyons>`_
- `Strava <https://www.strava.com/athletes/15127545>`_

Linux
-----

I am a Linux enthusiast (`Linux From Scratch
<http://www.linuxfromscratch.org/>`_ is my idea of a fun weekend) and serve as
``typescript`` (secretary) for my local LUG (`LUGOD <http://www.lugod.org/>`_).

My setup generally includes the Arch Linux distribution, i3 tiling window
manager, fish, and vim. You can look at my `dotfiles
<https://github.com/ixjlyons/dotfiles>`_ if you want.

Electronics
-----------

Although I'm a mechanical engineer by training, I love taking electronic
devices apart. This started as an interest in robotics, but quickly became
a more general enthusiasm for microcontrollers and such. I'm mostly familiar
with Atmel's ATmega microcontrollers, but I've also done a little with TI's
MSP430 and ARM Cortex M3/M4 (though not enough to setup a toolchain on the
spot). I can do a pretty decent job with PCB layout and have had no total
failures arrive from `OSH Park <https://oshpark.com/>`_. At some point, I would
really like to build up some skills in designing and building guitar effects
pedals.

Other
-----

I enjoy craft beer. North Coast's Old Rasputin is my favorite (in the picture
above, I'm about to enjoy a flight at North Coast Brewing Co. in Fort Bragg,
CA).

I've been playing the guitar since 2003. I'm currently making my way through
Mick Goodrick's *The Advancing Guitarist*, which I should've bought a long time
ago.
