# -*- coding: utf-8 -*-
"""
Simple demonstration of CheckTable, which is an extension of QTableWidget
that automatically displays a variety of tabluar data formats.
"""
import initExample ## Add path to library (just for examples; you do not need this)
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

from pyqtgraph.widgets.FeedbackButton import FeedbackButton
# from .. import metaarray


app = pg.mkQApp("CheckTable Widget Example")

# w = pg.CheckTable(['Column 1','Column 2','Column 3'])
col_labels = ['pre', 'maze1', 'post1', 'maze2', 'post2']
w = pg.CheckTable(col_labels)
w.layout.setSpacing(10)

def on_add_row_clicked(evt):
    w.addRow('New')
    
window = QtWidgets.QWidget()
layout = QtGui.QVBoxLayout()
layout.addWidget(w)

addRowBtn = QtWidgets.QPushButton('Add Row')
addRowBtn.setObjectName("addRowBtn")
addRowBtn.clicked.connect(on_add_row_clicked)
    
layout.addWidget(addRowBtn)
window.setLayout(layout)

# w.show()
window.show()
window.resize(500,500)
window.setWindowTitle('pyqtgraph example: CheckTable')

# w.resize(500,500)
# w.setWindowTitle('pyqtgraph example: CheckTable')

rows_data = [f'row[{i}]' for i in np.arange(8)]
w.updateRows(rows_data)


# def add_button_row(w):
#     num_cols = len(w.columns)
#     num_rows = len(w.rowNames)

#     next_row_idx = num_rows + 1
#     half_num_cols = int(np.floor(float(num_cols) / 2.0))

#     print(f'num_cols: {num_cols}, num_rows: {num_rows}, next_row_idx: {next_row_idx}')

#     w.addRowBtn = QtWidgets.QPushButton('Add Row')
#     w.addRowBtn.setObjectName("addRowBtn")
#     # w.layout.addWidget(w.loadBtn, 1, half_num_cols, next_row_idx, 1)
#     w.layout.addWidget(w.addRowBtn, next_row_idx, 0, 1, half_num_cols)
#     w.addRowBtn.clicked.connect(on_add_row_clicked)
        
#     # w.saveBtn = FeedbackButton('Save')
#     # w.saveBtn.setObjectName("saveBtn")
#     # btn.clicked.connect(click)
#     # # w.layout.addWidget(w.saveBtn, 1, half_num_cols, next_row_idx, half_num_cols+1) # spans 2 rows and 1 column
#     # w.layout.addWidget(w.saveBtn, next_row_idx, half_num_cols+1, 1, half_num_cols) # spans 2 rows and 1 column
#     # # w.layout.addWidget(check, row, col)
    


# add_button_row(w)
# for a_row in rows_data:
#     w.addRow(a_row)

    
# data = np.array([
#     (1,   1.6,   'x'),
#     (3,   5.4,   'y'),
#     (8,   12.5,  'z'),
#     (443, 1e-12, 'w'),
#     ], dtype=[('Column 1', int), ('Column 2', float), ('Column 3', object)])
    
# w.setData(data)


# if __name__ == '__main__':
#     app = QtGui.QApplication([])
#     win = QtGui.QMainWindow()
#     t = TableWidget()
#     win.setCentralWidget(t)
#     win.resize(800,600)
#     win.show()
    
#     ll = [[1,2,3,4,5]] * 20
#     ld = [{'x': 1, 'y': 2, 'z': 3}] * 20
#     dl = {'x': list(range(20)), 'y': list(range(20)), 'z': list(range(20))}
    
#     a = np.ones((20, 5))
#     ra = np.ones((20,), dtype=[('x', int), ('y', int), ('z', int)])
    
#     t.setData(ll)
    
#     ma = metaarray.MetaArray(np.ones((20, 3)), info=[
#         {'values': np.linspace(1, 5, 20)}, 
#         {'cols': [
#             {'name': 'x'},
#             {'name': 'y'},
#             {'name': 'z'},
#         ]}
#     ])
#     t.setData(ma)
    


if __name__ == '__main__':
    pg.exec()
