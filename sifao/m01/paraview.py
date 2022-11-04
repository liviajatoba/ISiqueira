# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Paraview python script for exporting x3d scenes
# Tobias Holzmann
# February 2016
# Tobias.Holzmann@Holzmann-cfd.de
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

from paraview.simple import *

# Change 104 to the amount of timesteps
for num in range(0,104):
    print 'Export scene ' + str(num)

    renderView1 = GetActiveViewOrCreate('RenderView')
    renderView1.ViewSize = [1371, 775]

    # Build file name
    # Change to your folder
    name = '/home/liviajatoba/OpenFOAM/ISiqueira/sifao/m01/blendMe/x3d/blenderX3D_' + str(num) + '.x3d'
    print 'Save as ' + str(name) 
    ExportView(name, view=renderView1)

    animationScene1 = GetAnimationScene()

    animationScene1.GoToNext()
