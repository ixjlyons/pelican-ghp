:title: MyoSwim
:status: hidden

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

.. figure:: https://raw.githubusercontent.com/ixjlyons/myoswim/master/img/screenshot.png
   :width: 400px

.. figure:: {filename}/images/wsf-photo.jpg
   :width: 400px

.. _myoswim-gh: https://github.com/ixjlyons/myoswim
.. _World Science Festival: http://www.worldsciencefestival.com/
