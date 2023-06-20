This is a code repository for a project created by Bartosz Brzeziński and Tomasz Sibicki.

Code dependencies:
numpy
statistics
scipy.stats
matplotlib
plotly

schemes.py holds the numerical basis of our project, plot_x_x.py files were used to create the plots for our paper. interactive_plot.py is used to create user generated interactive plot of particle diffusion. Examples of similar plots are in plots folder. In their naming scheme first number is -u, and the second number is D, for the standard naming in diffusion equation.

On the interactive plot, we decided to select 100 steps over the whole time T instead of letting the user select any step for the ease of use and memory usage.