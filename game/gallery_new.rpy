##############################################################################
# Gallery

init offset = -2

define gui.thumbnail_size = (246, 186)

screen myGallery(resetY=None):
    tag menu
    modal True

    use std_frame("Title", 24, 0.0, size=(1140, 840)):
        style_prefix "gallery"

        frame:
            style "gallery_outer_frame"

            viewport:
                mousewheel True
                draggable True

                vbox:
                    $ r = 3
                    $ c = 3

                    grid c r:
                        style_prefix "gallery_cg"

                        for i in range(0, c * r):
                            add "ui/Frame_g02.png"

                    # Ending recaps
                    null height 5
                    use gallery_ending(0, "Recap", "ui/Frame_g02.png")

screen gallery_ending(chara, title, img):
    style_prefix "gallery_ending"
    vbox:
        # Divider
        frame:
            style "gallery_hr"
            null

        text title

        grid 3 2:
            for i in range(0, 6):
                button:
                    add "ui/gallery_ending_lock.png"
                    add "ui/gallery_ending_frame.png"
                    text "No.{}".format(i+1) style "gallery_ending_item_label"

style gallery_outer_frame is default

style gallery_outer_frame:
    ymargin 53
    xmargin 123

style gallery_cg_grid:
    spacing 53
    xalign 0.5

style gallery_hr is default

style gallery_hr:
    background Solid("#838383")
    top_margin 25
    top_padding 5
    xfill True

style gallery_ending_vbox:
    spacing 10

style gallery_ending_hbox:
    spacing 53

style gallery_ending_text:
    color "#FF9900" # TODO: move this to gui.rpy

style gallery_ending_grid:
    xfill True

style gallery_ending_button is default

style gallery_ending_button:
    background Solid("#FFFFFFCC")
    xysize (154, 67)

style gallery_ending_item_label:
    color "#555555"
    size 13

style gallery_ending_item_text is gallery_ending_item_label

style gallery_ending_item_text:
    text_align 0.5

style gallery_ending_grid:
    spacing 15
