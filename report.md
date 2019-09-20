# Making a clean database 

In order to make a clean database, I took all the cubes from the observations of year 2018 with SITELLE after detrend.
One can find on these images :

* saturated stars going in the negative values
* diffraction spikes
* bad columns
* satellites
* cosmic rays

that we want to get rid of.

For the saturated stars, I set all negative values below -500 to the saturation value (max found on the image).
The bad columns and diffraction spikes are delimited by regions in ds9 then saved under the .reg format.
The satellites are manually removed from the database.
The cosmis rays are detected and removed from the images using astroscrappy algorithm which is an edge detection algorithm hence the 
importance of having readjusted the negative values of saturated stars before this step.

