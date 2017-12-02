## Standard frame

init offset = -2

screen std_frame(title=None, title_size=20, title_align=0.5, pad=(25, 15), align=(0.5, 0.5), size=None, close_padding=(20, 20)):
    style_prefix "std_frame"
    frame:
        style "default"
        background "#000"

    frame:
        align align
        padding close_padding
        if size is not None:
            xysize size

        frame:
            style_prefix "std_frame_inner"
            padding pad

            vbox:
                if size is not None:
                    xsize (size[0] - pad[0] * 2)

                if title is not None:
                    text title size title_size xalign title_align
                
                transclude

style std_frame_frame:
    background Solid("#222")

style std_frame_inner_frame is default

style std_frame_inner_text:
    color "#FF9900"
