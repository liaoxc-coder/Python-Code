# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

# 数据，可自定义
x = np.linspace(-20, 20, 1000)
y = np.sin(x) / x  # sin
# y = np.cos(x) / x  #cos，省略

plot = pg.plot()
plot.setYRange(-1, 2)  # y轴取值范围
plot.setWindowTitle('pyqtgraph example: text')  # 表格名称
curve = plot.plot(x, y)

# 导入html格式的text静态标签，本次重点
text = pg.TextItem(
    html='<div style="text-align: center">\
          <span style="color: #FFF;">This is the</span>\
          <br><span style="color: #FF0; font-size: 16pt;">PEAK</span>\
          </div>', anchor=(-0.3, 0.5), angle=20, border='w', fill=(0, 0, 255, 100))
plot.addItem(text)
text.setPos(0, y.max())

# 画箭头
arrow = pg.ArrowItem(pos=(0, y.max()), angle=-45)
plot.addItem(arrow)

## 设置动画和曲线
curvePoint = pg.CurvePoint(curve)
plot.addItem(curvePoint)
# text2是动态显示text
text2 = pg.TextItem("test", anchor=(0.5, -1.0))
text2.setParentItem(curvePoint)
arrow2 = pg.ArrowItem(angle=90)
arrow2.setParentItem(curvePoint)

index = 0


def update():
    global curvePoint, index
    index = (index + 1) % len(x)
    curvePoint.setPos(float(index) / (len(x) - 1))
    text2.setText('[%0.1f, %0.1f]' % (x[index], y[index]))


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)  # every 10ms

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
