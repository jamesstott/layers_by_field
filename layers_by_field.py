############################################
#
# Split layers by field.
# Developed by James Stott
# 14/06/2013
# Based on the code of the Split Shapefile plugin.
#
###############################################


# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

import os
#from __init__ import mVersion
import resources
import layers_by_field_dialog
import inspect
from os import path

class layers_by_field( object ):

  def __init__( self, iface ):
    self.iface = iface

    try:
      self.QgisVersion = unicode( QGis.QGIS_VERSION_INT )
    except:
      self.QgisVersion = unicode( QGis.qgisVersion )[ 0 ]

    # For i18n support
    userPluginPath = QFileInfo( QgsApplication.qgisUserDbFilePath() ).path() + "/python/plugins/layers_by_field"
    systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/layers_by_field"

    overrideLocale = QSettings().value( "locale/overrideFlag", False)#.toBool()
    if not overrideLocale:
      locale = QLocale.system().name()[0:2]
      #locale = QSettings().value("locale/userLocale")[0:2]
    else:
      localeFullName = QSettings().value( "locale/userLocale", "" )#.toString()
      locale = QSettings().value("locale/userLocale")[0:2]

    if QFileInfo( userPluginPath ).exists():
      translationPath = userPluginPath + "/i18n/layers_by_field_" + locale + ".qm"
    else:
      translationPath = systemPluginPath + "/i18n/layers_by_field_" + locale + ".qm"

    self.localePath = translationPath
    if QFileInfo( self.localePath ).exists():
      self.translator = QTranslator()
      self.translator.load( self.localePath )
      if qVersion() > '4.3.3':
        QCoreApplication.installTranslator(self.translator)

  def initGui(self):
    
    self.actionRun = QAction(QIcon(":/plugins/layers_by_field/icon.png"), QCoreApplication.translate('SplitLayersByField','Split Layers By Field'), self.iface.mainWindow())
    self.actionRun.setStatusTip(QCoreApplication.translate('SplitLayersByField',"Split Layers By Field adds a layer for each unique value in a text field"))
    self.actionRun.setWhatsThis( QCoreApplication.translate('SplitLayersByField',"Split Layers By Field"))
    self.actionAbout = QAction(QIcon(":/plugins/layers_by_field/help.png"), \
                              QCoreApplication.translate('SplitLayersByField',"Help"), self.iface.mainWindow())
    self.actionAbout.setWhatsThis(QCoreApplication.translate('SplitLayersByField',"Split Layers By Field Help"))

    self.actionRun.triggered.connect(self.run)
    self.actionAbout.triggered.connect(self.about)

    if hasattr( self.iface, "addPluginToVectorMenu" ):
      self.iface.addPluginToVectorMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"), self.actionRun)
      self.iface.addPluginToVectorMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"), self.actionAbout )
    else:
      self.iface.addPluginToMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"), self.actionRun)
      self.iface.addPluginToMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"), self.actionAbout )

  def unload(self):
    if hasattr( self.iface, "addPluginToVectorMenu" ):
      self.iface.removePluginVectorMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"),self.actionRun)
      self.iface.removePluginVectorMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"), self.actionAbout )
    else:
      self.iface.removePluginMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"),self.actionRun)
      self.iface.removePluginMenu(QCoreApplication.translate('menu_items', "Split Layers By Field"), self.actionAbout )

  def about( self ):
      
    file = inspect.getsourcefile(layers_by_field)
    file = 'file://' + path.join(path.dirname(file),'help/index.html')
    file = file.replace("\\","/")
    self.iface.openURL(file, False)

  def run(self):
    
    if QgsMapLayerRegistry.instance().count() >= 1:
        self.dlg = layers_by_field_dialog.layers_by_field_dialog(self.iface)
        self.dlg.show()
        result = self.dlg.exec_()
        if result ==1:
            pass
    else:
        QMessageBox.information( self.iface.mainWindow(),"Info", QCoreApplication.translate("info_message","There are no layers loaded"))
        
    
