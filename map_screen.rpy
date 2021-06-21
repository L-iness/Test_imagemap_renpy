screen screen_map:
    imagemap:
        ground "map"
        xalign 0.05
        yalign 0.05
        hotspot(2, 24, 29, 63) action Jump("scene1")
        hotspot(49, 23, 51, 39) action Jump("scene2")
        hotspot(42, 77, 82, 41) action Jump("scene3")





    hbox align (.05,.95) spacing 20 :
        textbutton "{b}Accueil{/b}" action [Jump("fin")]
        textbutton "{b}Retour{/b}" action [Jump("start")] 


