# Graphical Interface with Periodic Table!
import pygame
import os
from clean_CSV import clean_csv as scrub

pygame.init()

# each element in order of name, atomic num, symbol, weight, col, row
dataset = scrub()
fps = 60
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])   #created the display....
pygame.display.set_caption('Periodic Table!')       #gave the display name...
timer = pygame.time.Clock()

folder_path = 'C:\PROJECT_PERIODIC_TABLE\element_images'


#decleared the fonts...
font = pygame.font.SysFont('arial', 20,bold=True)
font1 = pygame.font.SysFont('arial', 18,bold=True)
midfont = pygame.font.SysFont('cambria', 35,bold=True)
bigfont = pygame.font.SysFont('arialblack', 35)
elefont = pygame.font.SysFont('cambria', 22,bold=True)
elefont1 = pygame.font.SysFont('arial',23,bold=True)
perfont = pygame.font.SysFont('cambria', 35,bold=True)

cols = 18
rows = 10
cell_width = WIDTH / cols
cell_height = HEIGHT / rows



highlight = False
# colors
colors = [('Alkali Metals', 'orchid'),
          ('Metalloids', 'yellow'),
          ('Actinides', 'darkorange'),
          ('Alkaline Earth Metals', 'crimson'),
          ('Reactive Nonmetals', (190,10,89)),
          ('Unknown Properties', 'tan'),
          ('Transition Metals', 'purple'),
          ('Post-transition Metals','mediumspringgreen'),
          ('Noble Gases', 'cyan'),
          ('Lanthanides', 'goldenrod')]

groups = [[3, 11, 19, 37, 55, 87],
          [5, 14, 32, 33, 51, 52],
          [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103],
          [4, 12, 20, 38, 56, 88],
          [1, 6, 7, 8, 9, 15, 16, 17, 34, 35, 53],
          [109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
          [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 39, 40, 41, 42, 43, 44,
           45, 46, 47, 48, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           104, 105, 106, 107, 108],
          [13, 31, 49, 50, 81, 82, 83, 84, 85],
          [2, 10, 18, 36, 54, 86],
          [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]]



def load_images_from_folder(folder_path):
    images = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                image_path = os.path.join(folder_path, filename)
                images[filename] = pygame.image.load(image_path)
            except pygame.error as e:
                print(f"Unable to load image {filename}: {e}")
    return images
images = load_images_from_folder(folder_path)

def get_image(images, key):
    return images.get(key)

def reshape_image(image, pic_width, pic_height):
    return pygame.transform.scale(image, (pic_width, pic_height))



def draw_screen(data):      #data=dataset
    element_list = []
    for i in range(len(data)):
        elem = data[i]
        # name, number, symbol, weight, col, row
        for q in range(len(groups)):
            if int(elem[1]) in groups[q]:
                 
                color = colors[q][1]
        if elem[4] < 3:
            x_pos = (elem[4] - 1) * cell_width 
        else:
            x_pos = (elem[4] - 2) * cell_width 
        y_pos = (elem[5] - 2) * cell_height
        if elem[4] == 4 and elem[5] in [7, 8]:
            x_pos = (elem[4] + 12) * cell_width
            y_pos = (elem[5] + 1) * cell_height
        box = pygame.draw.rect(screen, color,
                               [x_pos, y_pos, cell_width-4, cell_height - 6])
        pygame.draw.rect(screen, 'black',
                         [x_pos - 2, y_pos - 2, cell_width, cell_height], 3)
        #for atomic no.
        screen.blit(font.render(elem[1], True, 'black'), (x_pos + 2, y_pos + 2))
        #for element name
        screen.blit(elefont.render(elem[2], True, 'black'), (x_pos + 7, y_pos + 25))
        element_list.append((box, (i, color)))
        # lanths and acts explainers
        
        pygame.draw.rect(screen, 'goldenrod',
                         [cell_width * 2 , cell_height * 5 , cell_width-4, cell_height - 6])
        
        pygame.draw.rect(screen, 'darkorange',
                         [cell_width * 2 , cell_height * 6 , cell_width-4, cell_height - 6])
        pygame.draw.rect(screen, 'white',
                         [cell_width * 2 - 3, cell_height * 5 - 3, cell_width, cell_height], 3, 0)
        pygame.draw.rect(screen, 'white',
                         [cell_width * 2 - 3, cell_height * 6 - 3, cell_width, cell_height], 3, 0)


        #white line around lanths and act

        pygame.draw.rect(screen, 'white',
                         [cell_width * 2 - 3, cell_height * 8 - 3, cell_width * 15, 2 * cell_height], 3, 5)
        # pygame.draw.line(screen, 'white', (cell_width * 2 - 3, cell_height * 6), (cell_width * 2 - 3, cell_height * 9),
        #                  3)
        screen.blit(elefont1.render("56-71", True, 'black'), (cell_width*2, cell_height *5+5))
        screen.blit(elefont1.render("89-103", True, 'black'), (cell_width*2, cell_height *6+5))
        screen.blit(font.render("See", True, 'black'), (cell_width*2, cell_height *6+30))
        screen.blit(font1.render("Below", True, 'black'), (cell_width*2, cell_height *6+50))
        screen.blit(font.render("See", True, 'black'), (cell_width*2, cell_height *5+30))
        screen.blit(font1.render("Below", True, 'black'), (cell_width*2, cell_height *5+50))
        #  screen.blit(bigfont.render(information[1] + '-' + information[2], True,('black')),
        #         (cell_width * 3 + 5, cell_height * 0.5 + 10))
    return element_list

def draw_highlight1(stuff, mouse_x, mouse_y):  # stuff=info=element[e][1]
    
    image=None
    if(stuff[0]>=57 and stuff[0]<=118):
        desired_image_key = picture_name.get(stuff[0]+14)

    else:
        desired_image_key = picture_name.get(stuff[0])
    image = get_image(images, desired_image_key)
    
    line_spacing=20
    information = None
    information1 = None
    information2 = None

    if(stuff[0]>=57 and stuff[0]<=118):
        lines = data.get(stuff[0]+14)
        lines1 = melting.get(stuff[0]+14)
        lines2 = desity.get(stuff[0]+14)
    
    
    else:
        lines = data.get(stuff[0])
        lines1 = melting.get(stuff[0])
        lines2 = desity.get(stuff[0])


    information = lines.split('\n')
    information1 = lines1.split('\n')
    information2 = lines2.split('\n')

    # Adjust positions based on mouse coordinates with some offset
    rect_width = cell_width * 3.5
    rect_height = cell_height * 4
    rect_x = mouse_x
    rect_y = mouse_y

    # Ensure the rectangle doesn't go off the screen
    if rect_x + rect_width > screen.get_width():
        rect_x = screen.get_width() - rect_width
    if rect_y + rect_height > screen.get_height():
        rect_y = screen.get_height() - rect_height

    # Draw the top information rectangle
    pygame.draw.rect(screen, 'white', [rect_x, rect_y, rect_width, rect_height], 0, 0)
    pygame.draw.rect(screen, 'gray', [rect_x, rect_y, rect_width, rect_height], 4, 0)
    pygame.draw.rect(screen, 'black', [rect_x, rect_y, rect_width, rect_height], 3, 0)

    if image:
        new_width = cell_width*3.5
        new_height = cell_height*3
        image = reshape_image(image, new_width, new_height)
        # Blit the image
        screen.blit(image, (rect_x+0.5, rect_y))
        pygame.draw.rect(screen, 'black', [rect_x, rect_y, new_width, new_height], 3, 0)

    # Render the text at adjusted positions
    for i, information in enumerate(information):
        text_surface = font1.render('Boiling point:'+information, True, 'black')
        screen.blit(text_surface, (rect_x+10, rect_y+240 + i * line_spacing))

    for i, information1 in enumerate(information1):
        text_surface = font1.render('Melting Point:'+information1, True, 'black')
        screen.blit(text_surface, (rect_x+10, rect_y+265 + i * line_spacing))

    for i, information2 in enumerate(information2):
        text_surface = font1.render('Density:'+information2, True, 'black')
        screen.blit(text_surface, (rect_x+10, rect_y+290 + i * line_spacing))
def draw_highlight(stuff):
    classification = ''
    information = dataset[stuff[0]]
    for i in range(len(colors)):
        if colors[i][1] == stuff[1]:
            classification = colors[i][0]
    highlight_pic=pygame.image.load('C:\PROJECT_PERIODIC_TABLE\Highlight.png')
    highlight_pic= pygame.transform.scale(highlight_pic, (cell_width*7, cell_height*2))

    #this is the top information rectangle

    pygame.draw.rect(screen, 'white',
                     [cell_width * 4.5, cell_height * 0.5, cell_width * 7, cell_height * 2], 0, 10)
    
    #this is the top information black rectangle

    pygame.draw.rect(screen, 'black',
                     [cell_width * 4.5, cell_height * 1.5, cell_width * 7, cell_height * 0.8], 0, 10)
    
    #this is the top information white outline rectangle

    pygame.draw.rect(screen, 'white',
                     [cell_width * 4.5, cell_height * 0.5, cell_width * 7, cell_height * 2], 8, 10)
   
   


    screen.blit(highlight_pic,(cell_width * 4.5, cell_height * 0.5))


    pygame.draw.rect(screen, stuff[1],
                     [cell_width * 4.5, cell_height * 0.5, cell_width * 7, cell_height * 2], 6, 0)
    
    screen.blit(bigfont.render(information[1] + '-' + information[2], True,('black')),
                (cell_width * 4.5+7, cell_height * 0.5 + 10))
    screen.blit(midfont.render(information[0], True, 'black'),
                (cell_width * 7.5 + 10, cell_height * 0.5 + 10))
    screen.blit(midfont.render(information[3], True, 'black'),
                (cell_width * 7.5 + 10, cell_height * 0.9 + 10))
    screen.blit(perfont.render(classification, True, stuff[1]),
                (cell_width * 5.5 + 10, cell_height * 1.5 + 10))






#88
#57=105

data = {
    1: "(H2) 20.271K",2: "4.222K ",3: "1603K",4: "2742K",5: "4200K",6:"",7:"(N2) 77.355K​",8:"(O2) 90.188K",9:"(F2) 85.03K ​",10:"27.104K",11:"1156.090K",12:"1363K",13:"2743K ",14:"3538K",15:"553.7K",
    16:"717.8K",17:"(Cl2) 239.11K ",18:"87.302K",19:"1030.793K",20:"1757K",21:"3109K",22:"3560K",23:"3680K",24:"2944K",25:"2334K",26:"3134K",27:"3200K",28:"3003K",29:"2835K",30:"1180K",
    31:"2676K",32:"3106K",33:"",34:"958K",35:"(Br2) 332.0K",36:"119.93K",37:"961K",38:"1650K",39:"3203K",40:"4650K",41:"5017K",42:"4912K​",43:"4538K",44:"4423K",45:"3968K",
    46:"3236K",47:"2435K",48:"1040K",49:"2345K",50:"2875K",51:"1908K",52:"1261K",53:"(I2) 457.4K",54:"165.051K",55:"944K",56:"2118K",105:"3737K",106:"3716K",107:"3403K",108:"3347K",
    109:"3273K",110:"2173 K",111:"1802K",112:"3546K",113:"1629K",114:"2840K",115:"2873K",116:"3141K",117:"2223K",118:"1469K",71:"3675K",72:"4876K",73:"5731K",74:"6203K",75:"5903K",
    76:"5281K",77:"4403K",78:"4098K",79:"1337.33K",80:"629.88K",81:"1746K",82:"2022K",83:"1837K",84:"1235K",85:"",86:"211.5K",87:"950K",88:"2010K",
    

    #90=104
    89:"",  90:"5800K",91:"",92:"",93:"",94:"",95:"",96:"",97:"",98:"340 ± 10K",99:"1430K",100:"",101:"~1400K",102:"1035–1135K",103:"883K",104:"450 ± 10K",
    119:"3500±300K​",120:"5061K",121:"4300K",122:"4404K",123:"4447K",
    124:"3505K",125:"2880K",126:"3383K",127:"beta: 2900K",129:"1269K",130:"",131:"",132:"",128:"1743K",

}

melting={
    1: "(H2) 13.99K",2:"",3:"453.65K",4:"1560K",5:"2349K",6:"",7:"(N2) 63.23K ",8:"(O2) 54.36K",9:"	(F2) 53.48K",10:"24.56K",11:"370.944K",12:"923K",13:"933.47K",14:"1687K",15:"317.3K",
    16:"717.8K",17:"(Cl2) 171.6K",18:"83.81K",19:"336.7K",20:"1115K",21:"1814K",22:"1941K",23:"2183K",24:"2180K",25:"1519K",26:"1811K",27:"1768K",28:"1728K",29:"1357.77K",30:"692.68K",
    31:"302.9146K",32:"1211.40K",33:"",34:"494K",35:"(Br2) 265.8K",36:"115.78K",37:"312.45K",38:"1050K",39:"1799K",40:"2125K",41:"2750K",42:"2896K",43:"2430K",44:"2607K",45:"2237K",
    46:"1828.05K",47:"1234.93K",48:"594.22K",49:"429.7485K",50:"505.08K",51:"903.78K",52:"722.66 K",53:"(I2) 386.85K",54:"161.40K",55:"301.7K",56:"1000K",105:"1193K",106:"1068K",107:"1204K",108:"1295K",
    109:"1315K",110:"1345K",111:"1099K",112:"1585K",113:"1629K",114:"1680K",115:"1734K",116:"1802K",117:"1818K ",118:"1097K",71:"1925K",72:"2506K",73:"3290K",74:"3695K",75:"3459K",
    76:"3306K",77:"2719K",78:"2041.4K",79:"3243K",80:"234.3210 K",81:"577K",82:"600.61K",83:"544.7K",84:"527K",85:"",86:"202K",87:"300K",88:"973K",
    
    89:"1900K",  90:"2400K",91:"",92:"",93:"",94:"",95:"",96:"",97:"",98:"283 ± 11K",99:"700K",100:"284 ± 50K",101:"670K",102:"637–780K",103:"623–823K",104:"325 ± 15K",
    119:"1500K",120:"2023K",121:"1841K",122:"1405.3K",123:"	912±3K",
    124:"912.5K",125:"1449K",126:"1613K",127:"beta: 1259K",129:"1133K",130:"1800K",131:"1100K",132:"1100K",128:"1173K",
}

picture_name={
    1:'H.png',2:'He.png',3:'Li.png',4:'Be.png',5:'B.png',6:'C.png',7:'N.png',8:'O.png',9:'F.png',10:'Ne.png',11:'Na.png',12:'Mg.png',13:'Al.png',14:'Si.png',15:'P.png',
    16:'S.png',17:'Cl.png',18:'Ar.png',19:'K.png',20:'Ca.png',21:"Sc.png",22:"Ti.png",23:"V.png",24:"Cr.png",25:"Mn.png",26:"Fe.png",27:"Co.png",28:"Ni.png",29:"Cu.png",30:"Zn.png",
    31:"Ga.png",32:"Ge.png",33:"As.png",34:"Se.png",35:"Br.png",36:"Kr.png",37:"Rb.png",38:"Sr.png",39:"Y.png",40:"Zr.png",41:"Nb.png",42:"Mo.png",43:"Tc.png",44:"Ru.png",45:"Rh.png",
    46:"Pd.png",47:"Ag.png",48:"Cd.png",49:"In.png",50:"Sn.png",51:"Sb.png",52:"Te.png",53:"I.png",54:"Xe.png",55:"Cs.png",56:"Ba.png",
    71:"Lu.png",72:"Hf.png",73:"Ta.png",74:"W.png",75:"Re.png",76:"Os.png",77:"Ir.png",78:"Pt.png",79:"Au.png",80:"Hg.png",81:"Tl.png",82:"Pb.png",83:"Bi.png",84:"Po.png",85:"At.png",86:"Rn.png",87:"Fr.png",88:"Ra.png",
    89:"Lr.png",90:"Rf.png",91:"Db.png",92:"Sg.png",93:"Bh.png",94:"Hs.png",95:"Mt.png",96:"Ds.png",97:"Rg.png",98:"Cn.png",99:"Nh.png",100:"Fl.png",101:"Mc.png",102:"Lv.png",
    103:"Ts.png",104:"Og.png",105:"La.png",106:"Ce.png",107:"Pr.png",108:"Nd.png",109:"Pm.png",110:"Sm.png",111:"Eu.png",112:"Gd.png",113:"Tb.png",114:"Dy.png",115:"Ho.png",116:"Er.png",117:"Tm.png",118:"Yb.png",119:"Ac.png",120:"Th.png",121:"Pa.png",122:"U.png",123:"Np.png",
    124:"Pu.png",125:"Am.png",126:"Cm.png",127:"Bk.png",128:"Cf.png",129:"Es.png",130:"Fm.png",131:"Md.png",132:"No.png",
    
}

desity={
    1:'0.08988 g/L',2:'0.1786 g/L',3:'0.5334 g/cm3',4:'1.845 g/cm3',5:'2.08 g/cm3',6:"2.266 g/cm3",7:'1.2506 g/L',8:'1.429 g/L',9:'1.696 g/L',10:'0.9002 g/L',11:'0.9688 g/cm3',12:'1.737 g/cm3',13:'2.699 g/cm3',14:'2.329085 g/cm3',15:'white: 1.823 g/cm3',16:'2.07 g/cm3',17:'3.2 g/L',18:'1.784 g/L',19:'0.8590 g/cm3',20:'1.526 g/cm3',21:"2.989 g/cm3",22:"4.502 g/cm3",23:"6.099 g/cm3",24:"7.192 g/cm3",25:"7.476 g/cm3",26:"7.874 g/cm3",27:"8.834 g/cm3",28:"8.907 g/cm3",29:"8.935 g/cm3",30:"7.140 g/cm3",
    31:"5.907 g/cm3",32:"5.327 g/cm3",33:"5.782 g/cm3",34:"4.81 g/cm3",35:"Br2,liquid:3.1028 g/cm3",36:"3.749 g/L",37:"1.534 g/cm3",38:"2.582 g/cm3",39:"4.469 g/cm3",40:"6.505 g/cm3",41:"8.582 g/cm3",42:"10.223 g/cm3",43:"11.359 g/cm3",44:"12.364 g/cm3",45:"12.423 g/cm3",46:"12.007 g/cm3",47:"10.503 g/cm3",48:"8.649 g/cm3",49:"7.290 g/cm3",50:"7.289 g/cm3",51:"6.694 g/cm3",52:"6.237 g/cm3",53:"4.944 g/cm3",54:"3.408 g/cm3",55:"1.886 g/cm3",56:"3.594 g/cm3",71:"9.840 g/cm3",72:"13.281 g/cm3",73:"16.678 g/cm3",74:"19.254 g/cm3",75:"21.010 g/cm3",76:"22.587 g/cm3",77:"22.562 g/cm3",78:"21.452 g/cm3",79:"19.283 g/cm3",80:"13.546 g/cm3",81:"11.873 g/cm3",82:"11.348 g/cm3",83:"9.807 g/cm3",84:"9.196 g/cm3",85:"8.91–8.95 g/cm3",86:"9.73 g/L",87:"2.458 g/cm3",88:"5.5 g/cm3", 89:"14.4 g/cm3",90:"17 g/cm3",91:"21.6 g/cm3",92:"23–24 g/cm3",93:"26–27 g/cm3",94:"27–29 g/cm3",95:"27–28 g/cm3",96:"26–27 g/cm3",97:"22–24 g/cm3",98:"14.0 g/cm3",99:"16 g/cm3",100:"11.4 ± 0.3 g/cm3",101:"13.5 g/cm3",102:"12.9 g/cm3",103:"7.1–7.3 g/cm3",104:"7.2 g/cm3",105:"6.145 g/cm3",106:"β-Ce: 6.689 g/cm3",107:"6.773 g/cm3",108:"7.007 g/cm3",109:"7.149 g/cm3",110:"7.518 g/cm3",111:"5.246 g/cm3",112:"7.899 g/cm3",113:"8.229 g/cm3",114:"8.550 g/cm3",115:"8.795 g/cm3",116:"9.065 g/cm3",117:"9.320 g/cm3",118:"6.967 g/cm3",119:"10 g/cm3",120:"11.725 g/cm3",121:"15.43 g/cm3",122:"19.050 g/cm3",123:"20.48 g/cm3", 124:"19.85 g/cm3",125:"12 g/cm3",126:"13.51 g/cm3",127:"14.78 g/cm3",128:"15.1 g/cm3",129:"8.84 g/cm3",130:"9.7(1) g/cm3",131:"10.3(7) g/cm3",132:"9.9(4) g/cm3",   
}



run = True

#GAMELOOP....
while run:
    screen.fill('black')
    timer.tick(fps)
    elements = draw_screen(dataset)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if highlight==False:
        def_pic=pygame.image.load('C:\PROJECT_PERIODIC_TABLE\Def.png')
        def_pic=pygame.transform.scale(def_pic,(cell_width*8, cell_height*3))
        screen.blit(def_pic, (cell_width*3, 0))

    if highlight:
        draw_highlight1(info,mouse_x,mouse_y)
    if highlight:
        draw_highlight(info)
    highlight = False

  

    for e in range(len(elements)):
        if elements[e][0].collidepoint(mouse_pos):
            highlight = True
            info = elements[e][1]
    pygame.display.flip()
pygame.quit()