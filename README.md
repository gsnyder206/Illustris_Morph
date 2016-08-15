# Illustris_Morph

3Delong: creates a 3D scatter plot of mass vs radius with elongation denoted by color
AxisRatio: creates an axis ratio distribution for a whole population of Illustris galaxies given a redshift and filter
ColorElong2D: creates a 2D histogram of elongation vs color given a redshift and filter
ExampleGrid: my experimenting with using imshow to create a flat 3D plot
FilterCut: creates an axis ratio distribution for galaxies with a certain mass and/or SFR for a given redshift and filter
FilterElong2D: creates a 2D histogram of elongation vs mass or SFR for a given redshift and filter
Illustris_random_forest: this code runs the machine learning and random forest for the Illustris data; includes mapping data on a principal component space
MergerParameter: creates a flat 3D plot of parameter 1 vs parameter 2 and the number of mergers for a given redshift and filter
RF_Output: creates histograms for the various outputs from the random forest
RPCut: compares the axis ratio distribution for the whole Illustris population directly to a limited population for a given redshift and filter
RPDistribution: creates a distribution of the semi-minor axes and marks the PSF for a given redshift and filter
RPDistributionCompare: same as above but compares data from two cameras 
RPElong2D: creates a 2D histogram of petrosian radius vs elongation for a given redshift and filter
RPandFilterCut: creates an axis ratio distribution with galaxies that pass a radius and mass/SFR cut for a given redshift and filter
VariableCut: creates an axis ratio distribution with galaxies that pass a certain parameter cut
VariableElong2D: creates a 2D histogram of elongation vs a parameter for a given redshift and filter
comp_q: creates a direct comparison of the elongation as measured by galfit and photutils for the subpopulation of 110 Illustris galaxies
converting_image: this takes a mock fits image from Illustris and converts it into another fits files that has the correct units for galfit
galfit_input_file: creates input scripts for a list of Illustris galaxies to be run with galfit
image: reads in the final galfit output fits file and displays the orginial image, the model fit, and the residual all on the same color scale, for a list of Illustris galaxies
individual_halo_parameter: creates histograms of the qualities of the subpopulation used for galfit
intrinsic_projected_axisratios: directly compares a projected axis ratio to an intrinsic distribution for a population of simulated spheroidal, disk-like, and elongated galaxies
median: plots the evolution of the median of the 1/elongation
medianerror: uses bootstrap to create errors for the median of elongation for the whole population of Illustris galaxies
random_subpop: chooses 100 random galaxies from Illustris
selecting_subhalos: displays galaxies that have certain parameters to choose from to create a subpopulation of galaxies for galfit
subpopulation_params: gives the inverse of elongation for the subpopulation for galfit
