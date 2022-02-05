import maya.cmds as cmds

# Controls shapes
QUIDDITCH_CTRL ='Quidditch CTRL'
KNEE_ELBOW_CTRL = 'Knee/Elbow CTRL'
BOX_CTRL ='Box CTRL'
CIRCLE_CTRL ='Circle CTRL'
EYES_MASK_CTRL = 'Eyes CTRL'
SHOULDER_CTRL = 'Shoulder CTRL'
ARROWS_CTRL = 'Arrows CTRL'

# Controls colors
COLORS = {
    "Red": (1,0,0),
    "Cian": (0,1,1),
    "Yellow": (1,1,0),
    "Pink": (1,0,1)
}

def createCustomWorkspaceControlUI(*args):
    cmds.columnLayout("root", adjustableColumn=True)
        
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(80, 75, 150), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
    cmds.text(label = "Control name")
    cmds.textField("Control_Name_tF", editable=True)
        
                
    cmds.separator(height=3, style="in", parent="root")
        
    cmds.optionMenu("Control_Color_oM", label="Select the control's color", parent="root")
    cmds.menuItem( label='Red')
    cmds.menuItem( label='Cian')
    cmds.menuItem( label='Yellow')
    cmds.menuItem( label='Pink')
        
    cmds.separator(height=3, style="in", parent="root")
        
    cmds.optionMenu("Control_Shape_oM", label="Select the control's shape", parent="root")
    cmds.menuItem( label=QUIDDITCH_CTRL)
    cmds.menuItem( label=KNEE_ELBOW_CTRL)
    cmds.menuItem( label=BOX_CTRL)
    cmds.menuItem( label=CIRCLE_CTRL)
    cmds.menuItem( label=EYES_MASK_CTRL)
    cmds.menuItem( label=SHOULDER_CTRL)
    cmds.menuItem( label=ARROWS_CTRL)

    stick_control = cmds.button("Create", command=create_control, parent="root")

        
def create_control(*args):
    """Create the control base on the kind and the color passed as params."""
    control_color = cmds.optionMenu("Control_Color_oM", q=1, v=1)
    control_shape = cmds.optionMenu("Control_Shape_oM", q=1, v=1)
    
    control_name = cmds.textField("Control_Name_tF", q=True, text=True)
    print(control_name)
    
    rgb_color = COLORS[control_color]
    
    final_CTRL = ""
    
    if(control_shape == QUIDDITCH_CTRL):
        print ("Control of type color %s and with %s shape"% (control_color, control_shape))
        circle = cmds.circle(center=[0,0,-5], normal=[0,1,0], sweep=360, radius=1, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        stick = cmds.curve(d=1, p=[(0,0,-4), (0,0,0)], k=[0,1])
        cmds.color(circle, rgb=rgb_color)
        cmds.color(stick, rgb=rgb_color)
        
        cmds.parent([cmds.listRelatives(stick, shapes=True)[0]], circle, r=True, s=True)
        cmds.delete(stick)
        
        final_CTRL = circle
            
    elif(control_shape == KNEE_ELBOW_CTRL):
        print ("Control of type color %s and with %s shape"% (control_color, control_shape))
        circle_1 = cmds.circle(center=[0,0,0], normal=[0,1,0], sweep=360, radius=1, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        circle_2 = cmds.circle(center=[0,0,0], normal=[1,0,0], sweep=360, radius=1, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        circle_3 = cmds.circle(center=[0,0,0], normal=[0,0,1], sweep=360, radius=1, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        
        cmds.color(circle_1, rgb=rgb_color)
        cmds.color(circle_2, rgb=rgb_color)
        cmds.color(circle_3, rgb=rgb_color)
        
        cmds.parent([cmds.listRelatives(circle_3, shapes=True)[0],cmds.listRelatives(circle_2, shapes=True)[0]], circle_1, r=True, s=True)
        cmds.delete(circle_3, circle_2)
        
        final_CTRL = circle_1
    
    elif(control_shape == BOX_CTRL):
        print ("Control of type color %s and with %s shape"% (control_color, control_shape))
        bottom_square = cmds.curve(d=1, p=[(-3,0,3),(-1,0,3),(1,0,3), (3,0,3),(3,0,1),(3,0,-1),(3,0,-3),(1,0,-3),(-1,0,-3),(-3,0,-3),(-3,0,-1),(-3,0,1),(-3,0,3)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12])
        top_square = cmds.curve(d=1, p=[(-3,6,3),(-1,6,3),(1,6,3),(3,6,3),(3,6,1),(3,6,-1),(3,6,-3),(1,6,-3),(-1,6,-3),(-3,6,-3),(-3,6,-1),(-3,6,1),(-3,6,3)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12])
        line_1 = cmds.curve(d=1, p=[(-3,0,3),(-3,2,3),(-3,4,3),(-3,6,3)], k=[0,1,2,3])
        line_2 = cmds.curve(d=1, p=[(3,0,3),(3,2,3),(3,4,3),(3,6,3)], k=[0,1,2,3])
        line_3 = cmds.curve(d=1, p=[(-3,0,-3),(-3,2,-3),(-3,4,-3),(-3,6,-3)], k=[0,1,2,3])
        line_4 = cmds.curve(d=1, p=[(3,0,-3),(3,2,-3),(3,4,-3),(3,6,-3)], k=[0,1,2,3])
        
        cmds.color(bottom_square, rgb=rgb_color)
        cmds.color(top_square, rgb=rgb_color)
        cmds.color(line_1, rgb=rgb_color)
        cmds.color(line_2, rgb=rgb_color)
        cmds.color(line_3, rgb=rgb_color)
        cmds.color(line_4, rgb=rgb_color)
        
        cmds.parent([
            cmds.listRelatives(top_square, shapes=True)[0],
            cmds.listRelatives(line_1, shapes=True)[0],
            cmds.listRelatives(line_2, shapes=True)[0],
            cmds.listRelatives(line_3, shapes=True)[0],
            cmds.listRelatives(line_4, shapes=True)[0]
            ], 
            bottom_square, r=True, s=True
        )
        
        cmds.delete(top_square, line_1, line_2, line_3, line_4)
        cmds.xform(bottom_square, cp=True)
        final_CTRL = bottom_square
        
    elif(control_shape == CIRCLE_CTRL):  
        print ("Control of type color %s and with %s shape"% (control_color, control_shape))
        circle = cmds.circle(center=[0,0,0], normal=[0,1,0], sweep=360, radius=2, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        cmds.color(circle, rgb=rgb_color)
        
        final_CTRL = circle
        
    elif(control_shape == EYES_MASK_CTRL):
        print ("Control of type color %s and with %s shape"% (control_color, control_shape))
        r_circle = cmds.circle(n="R_Eye_CTRL", center=[-2,0,0], normal=[0,1,0], sweep=360, radius=1, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        l_circle = cmds.circle(n="L_Eye_CTRL", center=[2,0,0], normal=[0,1,0], sweep=360, radius=1, degree=3, useTolerance=True, tolerance=0.01, sections=8, constructionHistory=False, o=True)
        mask = cmds.circle(n="Eyes_CTRL", center=[0,0,0], normal=[0,1,0], sweep=360, radius=2, degree=3, useTolerance=True, tolerance=0.01, sections=8, o=True)
    
        cmds.xform(mask, scale=[1.8, 1, 0.8], rotation=[90,0,0])
        cmds.makeIdentity(mask, apply=True)
        cmds.xform(r_circle, rotation=[90,0,0])
        cmds.makeIdentity(r_circle, apply=True)
        cmds.xform(l_circle, rotation=[90,0,0])
        cmds.makeIdentity(l_circle, apply=True)
        
        cmds.color(r_circle, rgb=COLORS["Red"])
        cmds.color(l_circle, rgb=COLORS["Cian"])
        cmds.color(mask, rgb=COLORS["Yellow"])
   
    elif(control_shape == SHOULDER_CTRL):
        line_1 = cmds.curve(d=1, p=[(-1,0,-2),(-1,0,2)], k=[0,1])
        line_2 = cmds.curve(d=1, p=[(1,0,-2),(1,0,2)], k=[0,1])
        top_circle = cmds.curve(p=[(-1,0,-2),(-2,0,-3),(-2,0,-4),(-1,0,-5),(1,0,-5),(2,0,-4),(2,0,-3),(1,0,-2)])
        bot_circle = cmds.curve(p=[(-1,0,-2),(-2,0,-3),(-2,0,-4),(-1,0,-5),(1,0,-5),(2,0,-4),(2,0,-3),(1,0,-2)])
        
        cmds.xform(bot_circle, rotation=[0,180,0])
        cmds.makeIdentity(bot_circle,apply=True)
        
        cmds.color(top_circle, rgb=rgb_color)
        cmds.color(bot_circle, rgb=rgb_color)
        cmds.color(line_1, rgb=rgb_color)
        cmds.color(line_2, rgb=rgb_color)
        
        cmds.parent([cmds.listRelatives(line_2, shapes=True)[0],cmds.listRelatives(line_1, shapes=True)[0],cmds.listRelatives(bot_circle, shapes=True)[0]], top_circle, r=True, s=True)
        cmds.delete(bot_circle, line_1, line_2)
        final_CTRL = top_circle   
        
    elif(control_shape == ARROWS_CTRL):
        line = cmds.curve(d=1, p=[(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),(1,0,-3),(1,0,-2),(2,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(2,0,1),(1,0,2),(1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,2),(-2,0,1),(-3,0,1),(-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-2,0,-1),(-1,0,-2),(-1,0,-3)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])  
        cmds.color(line, rgb=rgb_color)
        final_CTRL = line   
    
    if control_name and control_shape != EYES_MASK_CTRL:
        cmds.rename(final_CTRL, control_name)           


cmds.workspaceControl("Rig Controls", retain=False, floating=True, uiScript="createCustomWorkspaceControlUI()");