# -*- coding: utf-8 -*-
# vispy: gallery 30
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
"""
Simple use of SceneCanvas and ColorBarWidget to display a ColorBar.
"""
import sys
from vispy import scene
from vispy import app

canvas = scene.SceneCanvas(keys='interactive')
canvas.size = 800, 600
canvas.show()
grid = canvas.central_widget.add_grid(margin=10)


cbar_widget = scene.ColorBarWidget(halfdim=(100, 10), cmap="cool")
grid.add_widget(cbar_widget)

cbar_widget.pos = (300, 100)
cbar_widget.border_color = "#212121"
grid.bgcolor = "#ffffff"
grid.border_width = 1

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
