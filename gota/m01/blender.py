# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Blender python script for rendering x3d scenes
# Tobias Holzmann
# February 2016
# Tobias.Holzmann@Holzmann-cfd.de
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Adaptado de Tobias Holzmann por Livia Jatoba e Ivison Siqueira
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

import bpy

# Loop through all x3d files
# Change the number 101 to the timesteps you have
for num in range(101):
    
    # Open the file
    # Your file locations
    file = '/home/liviajatoba/OpenFOAM/ISiqueira/gota/m01/blendMe/x3d/blenderX3D_%d.x3d' % num
    print('Render %s' % file)
    bpy.ops.import_scene.x3d(filepath=file, axis_forward='Y', axis_up='Z')
    bpy.context.scene.world.horizon_color = (1, 1, 1)
    
    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')
   
    # Delete not necessary stuff
    for item in bpy.data.objects:
        if item.type != "MESH":
            bpy.data.objects[item.name].select = True
            bpy.ops.object.delete()
        else:
            if ( item.name == "Cube" ):
                bpy.data.objects[item.name].select = True
                bpy.ops.object.delete()
                               

    # Rename the left data
    bpy.data.objects["ShapeIndexedFaceSet"].data.name = 'GotaMesh'

    for obj in bpy.context.scene.objects:
        if obj.name == 'ShapeIndexedFaceSet':
            obj.name = 'Gota'
    
    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')
    
    ######################
    ### Adiciona a camera
    ######################
    bpy.ops.object.camera_add(location=(0,-3,0),rotation=(0, 0, 0))
    bpy.context.object.rotation_mode = 'AXIS_ANGLE'
    bpy.context.object.rotation_axis_angle[0] = 1.5708
    bpy.context.object.rotation_axis_angle[1] = 1
    bpy.context.object.rotation_axis_angle[2] = 0
    bpy.context.object.rotation_axis_angle[3] = 0
    #bpy.ops.transform.rotate(value=-25, axis=(1,0,0))
    
    ######################
    ### Altera para modo Cycler de renderizacao
    ######################
    bpy.context.scene.render.engine = 'CYCLES'
    #bpy.context.space_data.context = 'RENDER_LAYER'
    bpy.context.scene.render.layers["RenderLayer"].samples = 200
    bpy.context.scene.render.layers["RenderLayer"].use_pass_shadow = True
    
    ######################
    ### Add a light
    ######################
    bpy.ops.mesh.primitive_plane_add(radius=1, location=(-4, 5, 5))
    bpy.ops.transform.rotate(value=80, axis=(0.7,0,-0.7))

    bpy.ops.mesh.primitive_plane_add(radius=1, location=(4, 5, 5))
    bpy.ops.transform.rotate(value=80, axis=(0.7,0,0.7))
    
    bpy.ops.mesh.primitive_plane_add(radius=1, location=(-4, -5, 5))
    bpy.ops.transform.rotate(value=80, axis=(-0.7,0,0.7))

    bpy.ops.mesh.primitive_plane_add(radius=1, location=(4, -5, 5))
    bpy.ops.transform.rotate(value=80, axis=(-0.7,0,-0.7))

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    #edita a luz do plano
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane"]
 
    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialLight")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view 
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0
    
    # Emission
    node_emission = TreeNodes.nodes.new(type='ShaderNodeEmission')
    node_emission.location = 0,0
    node_emission.inputs[0].default_value = (1,1,1,1)  # white RGBA
    node_emission.inputs[1].default_value = 6.0 # strength

    # Connect the guys
    links.new(node_emission.outputs[0], node_out.inputs[0])

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    #edita a luz do plano 001
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane.001"]
 
    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialLight")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view 
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0
    
    # Emission
    node_emission = TreeNodes.nodes.new(type='ShaderNodeEmission')
    node_emission.location = 0,0
    node_emission.inputs[0].default_value = (1,1,1,1)  # white RGBA
    node_emission.inputs[1].default_value = 6.0 # strength

    # Connect the guys
    links.new(node_emission.outputs[0], node_out.inputs[0])

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')
     
    #edita a luz do plano 002
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane.002"]
 
    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialLight")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view 
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0
    
    # Emission
    node_emission = TreeNodes.nodes.new(type='ShaderNodeEmission')
    node_emission.location = 0,0
    node_emission.inputs[0].default_value = (1,1,1,1)  # white RGBA
    node_emission.inputs[1].default_value = 6.0 # strength

    # Connect the guys
    links.new(node_emission.outputs[0], node_out.inputs[0])

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    #edita a luz do plano 003
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane.003"]
 
    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialLight")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view 
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0
    
    # Emission
    node_emission = TreeNodes.nodes.new(type='ShaderNodeEmission')
    node_emission.location = 0,0
    node_emission.inputs[0].default_value = (1,1,1,1)  # white RGBA
    node_emission.inputs[1].default_value = 6.0 # strength

    # Connect the guys
    links.new(node_emission.outputs[0], node_out.inputs[0])

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    ######################
    ### Edita gota
    ######################
    bpy.data.objects["Gota"].select = True
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Gota"]
    bpy.context.object.active_material_index = 0
    bpy.ops.object.material_slot_remove()
    #bpy.ops.object.shade_smooth()

    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialWasser")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view 
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0

    # Glossy BSDF
#    node_glossy = TreeNodes.nodes.new(type='ShaderNodeBsdfGlossy')
#    node_glossy.location =0,180
#    node_glossy.inputs['Color'].default_value= (0.3,0.5,0.8,1)
#    node_glossy.inputs['Roughness'].default_value=0.34
    
    # Glass BSDF
    node_glass = TreeNodes.nodes.new(type='ShaderNodeBsdfGlass')
    node_glass.location =0,180
    node_glass.distribution = 'GGX'
    node_glass.inputs['Color'].default_value= (0.396,0.75,1,1)
    node_glass.inputs['Roughness'].default_value=0.05

    # Connect the guys
    links.new(node_glass.outputs[0], node_out.inputs[0])

    # Deselect everything
    #bpy.ops.object.select_all(action='TOGGLE')
        
    ############
    # For saving
    ############
    
    cam = bpy.data.objects['Camera']
    bpy.context.scene.camera = cam
    
    bpy.context.scene.cycles.samples = 200
    
    bpy.data.scenes['Scene'].render.filepath = '/home/liviajatoba/OpenFOAM/ISiqueira/gota/m01/blendMe/animacao/blended-%d.png' % num
    bpy.ops.render.render( write_still = True )
  
    ###################
    # Delete everything
    ###################
    bpy.ops.object.select_all(action='TOGGLE') 
    bpy.ops.object.select_all(action='TOGGLE') 
    bpy.ops.object.delete()
