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
# Change the number 104 to the timesteps you have
for num in range(104):
    # Open the file
    # Your file locations
    file = '/home/liviajatoba/OpenFOAM/ISiqueira/sifao/m01/blendMe/x3d/blenderX3D_%d.x3d' % num
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
    bpy.data.objects["ShapeIndexedFaceSet"].data.name = 'VinhoMesh'
    bpy.data.objects["ShapeIndexedFaceSet.001"].data.name = 'TacaMesh'

    for obj in bpy.context.scene.objects:
        if obj.name == 'ShapeIndexedFaceSet':
            obj.name = 'Vinho'
        if obj.name == 'ShapeIndexedFaceSet.001':
            obj.name = 'Taca'
    
    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')
    
    ######################
    ### Altera para modo Cycler de renderizacao
    ######################
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.world.horizon_color = (0.6, 0.8, 0.8)
    #bpy.context.space_data.context = 'RENDER_LAYER'
    bpy.context.scene.render.layers["RenderLayer"].samples = 200
    bpy.context.scene.render.layers["RenderLayer"].use_pass_shadow = True

    ######################
    ### Adiciona a camera
    ######################
    bpy.ops.object.camera_add(location=(0,-35,13),rotation=(0, 0, 0))
    bpy.ops.transform.rotate(value=-30, axis=(1,0,0))
    
    ######################
    ### Add a light
    ######################
    bpy.ops.mesh.primitive_plane_add(radius=1, location=(-8, 10, 25))
    bpy.ops.transform.rotate(value=80, axis=(0.7,0,-0.7))
    
    bpy.ops.mesh.primitive_plane_add(radius=1, location=(8, 10, 25))
    bpy.ops.transform.rotate(value=80, axis=(0.7,0,0.7))
    
    bpy.ops.mesh.primitive_plane_add(radius=1, location=(-8, -10, 25))
    bpy.ops.transform.rotate(value=80, axis=(-0.7,0,0.7))

    bpy.ops.mesh.primitive_plane_add(radius=1, location=(8, -10, 25))
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
    ### plano mesa
    ######################
    bpy.ops.mesh.primitive_plane_add(radius=1, location=(0, 0, 0))
    bpy.context.object.dimensions[0] = 50
    bpy.context.object.dimensions[1] = 50
    
        #edita a luz do plano
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane.004"]
 
    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialPlane")

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
    node_emission = TreeNodes.nodes.new(type='Diffuse BSDF')
    node_emission.location = 0,0
    node_emission.inputs[0].default_value = default_value = (0.8, 0.3, 0, 1)
    
    # Connect the guys
    links.new(node_emission.outputs[0], node_out.inputs[0])

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    ######################
    ### Edit wine
    ######################
    bpy.data.objects["Vinho"].select = True
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Vinho"]

    bpy.context.object.active_material_index = 0
    bpy.ops.object.material_slot_remove()
    bpy.ops.object.shade_smooth()

    # Create material
    mat = bpy.data.materials.new(name="MaterialVinho")
    # Assign it to object
    if len(bpy.context.active_object.data.materials):
        # assign to 1st material slot
        bpy.context.active_object.data.materials[0] = mat
    else:
        # no slots
        bpy.context.active_object.data.materials.append(mat)

    # Activated material -> mat
    ob = bpy.context.active_object
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

    # Glass BSDF
    node_glass = TreeNodes.nodes.new(type='ShaderNodeBsdfGlass')
    #node_glass.location =0,180
    #node_glass.distribution = 'GGX'
    node_glass.inputs['Color'].default_value= (0.94,0,0.025,1)
    node_glass.inputs['Roughness'].default_value=0
    node_glass.inputs['IOR'].default_value=1.33

    # Connect the guys
    links.new(node_glass.outputs[0], node_out.inputs[0])

    # Volume
    node_glass = TreeNodes.nodes.new(type='ShaderNodeVolumeAbsorption')
    node_glass.inputs['Density'].default_value=18

    # Connect the guys
    links.new(node_glass.outputs[0], node_out.inputs[1])

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    ######################
    ### Edit cup
    ######################
    bpy.data.objects["Taca"].select = True
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Taca"]
    bpy.context.object.active_material_index = 0
    bpy.ops.object.material_slot_remove()
    
    # Create material
    mat = bpy.data.materials.new(name="MaterialTaca")
    # Assign it to object
    if len(bpy.context.active_object.data.materials):
        # assign to 1st material slot
        bpy.context.active_object.data.materials[0] = mat
    else:
        # no slots
        bpy.context.active_object.data.materials.append(mat)

    # Activated material -> mat
    ob = bpy.context.active_object
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

    # Glass BSDF
    node_glass = TreeNodes.nodes.new(type='ShaderNodeBsdfGlass')
    #node_glass.location =0,180
    #node_glass.distribution = 'GGX'
    node_glass.inputs['Color'].default_value= (0.9,0.9,0.975,1)
    node_glass.inputs['Roughness'].default_value=0

    # Connect the guys
    links.new(node_glass.outputs[0], node_out.inputs[0])
        
    ############
    # For saving
    ############
    
    cam = bpy.data.objects['Camera']
    bpy.context.scene.camera = cam
    
    bpy.context.scene.cycles.samples = 200
    
    bpy.data.scenes['Scene'].render.filepath = '/home/liviajatoba/OpenFOAM/ISiqueira/sifao/m01/blendMe/animacao/blended-%d.png' % num
    bpy.ops.render.render( write_still = True )
  

    ###################
    # Delete everything
    ###################
    bpy.ops.object.select_all(action='TOGGLE') 
    bpy.ops.object.select_all(action='TOGGLE') 
    bpy.ops.object.delete()
