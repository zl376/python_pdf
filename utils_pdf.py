#!/usr/bin/env python3
# Utility for generating pdf
#   based on pylatex

from pylatex import Document, Section, Subsection, \
                    MiniPage, LargeText, Description, Figure, SubFigure, Tabular, Tabu, \
                    NewLine
from pylatex.utils import bold, NoEscape
from pylatex.package import Package


newline = NoEscape(r'~\\')



def add_figure(doc, filename, caption=None):
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(filename, width=NoEscape(r'1.0\linewidth'))
        if caption:
            plot.add_caption(caption)
            
            

def add_2figure(doc, filename_left, filename_right, caption_left=None, caption_right=None):    
    with doc.create(Figure(position='H')) as plot:
        with doc.create(SubFigure(position='b', width=NoEscape(r'0.5\linewidth'))) as left_plot:
            left_plot.add_image(filename_left, width=NoEscape(r'1.0\linewidth'))
            if caption_left:
                left_plot.add_caption(caption_left)
        with doc.create(SubFigure(position='b', width=NoEscape(r'0.5\linewidth'))) as right_plot:
            right_plot.add_image(filename_right, width=NoEscape(r'1.0\linewidth'))
            if caption_right:
                right_plot.add_caption(caption_right)

                
                
def add_3figure(doc, filename_left, filename_middle, filename_right, 
                     caption_left=None, caption_middle=None, caption_right=None):    
    with doc.create(Figure(position='H')) as plot:
        with doc.create(SubFigure(position='b', width=NoEscape(r'0.33\linewidth'))) as left_plot:
            left_plot.add_image(filename_left, width=NoEscape(r'1.0\linewidth'))
            if caption_left:
                left_plot.add_caption(caption_left)
        with doc.create(SubFigure(position='b', width=NoEscape(r'0.33\linewidth'))) as middle_plot:
            middle_plot.add_image(filename_middle, width=NoEscape(r'1.0\linewidth'))
            if caption_middle:
                middle_plot.add_caption(caption_middle)
        with doc.create(SubFigure(position='b', width=NoEscape(r'0.33\linewidth'))) as right_plot:
            right_plot.add_image(filename_right, width=NoEscape(r'1.0\linewidth'))
            if caption_right:
                right_plot.add_caption(caption_right)
                
                
                
def add_table(doc, df, flag_index=False, flag_smallfont=False,
                       format_cell='{}', mapper_cell=None):
    n_col = df.shape[1]
    if flag_index:
        n_col += 1
        
    if flag_smallfont:
        doc.append(NoEscape(r'\scriptsize'))
        
    if mapper_cell is None:
        mapper = lambda x, y, z: format_cell.format(x)
    else:
        mapper = lambda x, y, z: format_cell.format(mapper_cell(x, index=y, column=z))
        
    with doc.create(Tabu('X[l]' + 'X[r]' * (n_col - 1))) as table:
        table.add_hline()
        table.add_row(([df.index.name] if flag_index else []) + 
                      list(df.columns), mapper=[bold])
        table.add_hline()
        for row in df.index:
            table.add_row( ([row] if flag_index else []) +
                           list(map(mapper, df.loc[row, :], [row] * df.shape[1], df.columns)))
        table.add_hline()  
    if flag_smallfont:
        doc.append(NoEscape(r'\normalsize'))